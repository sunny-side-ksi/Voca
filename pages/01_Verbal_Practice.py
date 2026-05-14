"""GRE Verbal Reasoning Practice — TC, SE, RC"""
import json
import random
import time
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

from utils import inject_css, esc

st.set_page_config(page_title="Verbal Practice", page_icon="📝", layout="centered")
inject_css()

DATA_FILE = Path(__file__).parent.parent / "gre_content" / "practice_questions.json"

DIFF_LABEL = {"easy": "Easy", "medium": "Medium", "hard": "Hard"}
DIFF_CSS   = {"easy": "b-easy", "medium": "b-medium", "hard": "b-hard"}
TYPE_LABEL = {
    "text_completion":       "Text Completion",
    "sentence_equivalence":  "Sentence Equivalence",
    "reading_comprehension": "Reading Comprehension",
    "critical_reasoning":    "Critical Reasoning",
    "test":                  "Test (모의고사)",
}
TYPE_CSS = {
    "text_completion":       "b-tc",
    "sentence_equivalence":  "b-se",
    "reading_comprehension": "b-rc",
    "critical_reasoning":    "b-cr",
    "test":                  "b-test",
}
TYPE_SHORT = {
    "text_completion":    "TC",
    "sentence_equivalence": "SE",
    "reading_comprehension": "RC",
    "critical_reasoning": "CR",
    "test": "TEST",
}


@st.cache_data
def load_questions():
    with open(DATA_FILE, encoding="utf-8") as f:
        return json.load(f)["verbal"]


def build_items(filtered):
    """RC 문제를 지문별로 묶고, TC/SE는 개별 아이템으로 유지. 랜덤 셔플."""
    singles = []
    rc_map  = {}   # passage_text → [q, ...]
    rc_order = []  # insertion order

    for q in filtered:
        if q["type"] == "reading_comprehension" and q.get("passage"):
            p = q["passage"]
            if p not in rc_map:
                rc_map[p] = []
                rc_order.append(p)
            rc_map[p].append(q)
        else:
            singles.append(q)

    rc_groups = [
        {"type": "rc_group", "passage": p, "questions": rc_map[p]}
        for p in rc_order
    ]

    items = singles + rc_groups
    random.shuffle(items)
    return items


def count_total_q(items):
    """아이템 목록에서 개별 문항 총 개수 산출."""
    n = 0
    for item in items:
        n += len(item["questions"]) if item.get("type") == "rc_group" else 1
    return n


def build_test_items(all_q, n_test):
    """Test 모드: TC/SE/RC/CR 비례 샘플링 (12Q=5+2+4+1, 15Q=6+3+4+2)"""
    if n_test == 12:
        tc_n, se_n, rc_n, cr_n = 5, 2, 4, 1
    else:
        tc_n, se_n, rc_n, cr_n = 6, 3, 4, 2
    tc_pool = [q for q in all_q if q["type"] == "text_completion"]
    se_pool = [q for q in all_q if q["type"] == "sentence_equivalence"]
    rc_pool = [q for q in all_q if q["type"] == "reading_comprehension"]
    cr_pool = [q for q in all_q if q["type"] == "critical_reasoning"]
    sampled = (
        random.sample(tc_pool, min(tc_n, len(tc_pool))) +
        random.sample(se_pool, min(se_n, len(se_pool))) +
        random.sample(rc_pool, min(rc_n, len(rc_pool))) +
        random.sample(cr_pool, min(cr_n, len(cr_pool)))
    )
    return build_items(sampled)


def reset_session():
    for k in list(st.session_state.keys()):
        if k.startswith("vp_"):
            del st.session_state[k]


all_questions = load_questions()

st.title("📝 Verbal Reasoning Practice")

# ── Sidebar ─────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 📝 Verbal")
    st.markdown('<hr class="sdiv">', unsafe_allow_html=True)

    sel_type = st.multiselect(
        "문제 유형",
        options=["text_completion", "sentence_equivalence", "reading_comprehension", "critical_reasoning", "test"],
        default=["text_completion", "sentence_equivalence", "reading_comprehension", "critical_reasoning"],
        format_func=lambda x: TYPE_LABEL[x],
    )
    is_test_only = set(sel_type) == {"test"}

    if is_test_only:
        n_test = st.radio(
            "세트 크기",
            options=[12, 15],
            format_func=lambda x: f"{x}문제 ({'18' if x == 12 else '23'}분)",
            horizontal=True,
        )
        sel_diff = ["easy", "medium", "hard"]
    else:
        n_test = None
        sel_diff = st.multiselect(
            "난이도", options=["easy", "medium", "hard"],
            default=["easy", "medium", "hard"],
            format_func=lambda x: DIFF_LABEL[x],
        )

    st.markdown('<hr class="sdiv">', unsafe_allow_html=True)

    if st.button("🚀  Start / Restart", type="primary", use_container_width=True):
        reset_session()
        if is_test_only:
            duration = 18 * 60 if n_test == 12 else 23 * 60
            items = build_test_items(all_questions, n_test)
            st.session_state.update({
                "vp_questions": items,
                "vp_total_q":   count_total_q(items),
                "vp_idx":       0,
                "vp_answers":   {},
                "vp_submitted": {},
                "vp_score":     0,
                "vp_done":      False,
                "vp_is_test":   True,
                "vp_test_end":  int(time.time()) + duration,
            })
        else:
            filtered = [q for q in all_questions
                        if q["difficulty"] in sel_diff and q["type"] in sel_type]
            items = build_items(filtered)
            st.session_state.update({
                "vp_questions": items,
                "vp_total_q":   count_total_q(items),
                "vp_idx":       0,
                "vp_answers":   {},
                "vp_submitted": {},
                "vp_score":     0,
                "vp_done":      False,
                "vp_is_test":   False,
            })
        st.rerun()
    st.caption("TC: 빈칸 완성 | SE: 문장 등가 | RC: 독해 | CR: 논리 추론 | TEST: 모의고사")

# ── Guard ───────────────────────────────────────────────────────────────────────
if "vp_questions" not in st.session_state:
    st.markdown("""
    <div style="text-align:center; padding:60px 20px;">
      <div style="font-size:3.5rem;">📝</div>
      <h2 style="color:#1E293B; margin-top:12px;">Verbal Reasoning</h2>
      <p style="color:#64748B;">사이드바에서 난이도·유형을 선택하고<br><strong>Start</strong>를 눌러 시작하세요.</p>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

questions = st.session_state["vp_questions"]
if not questions:
    st.warning("선택한 조건에 해당하는 문제가 없습니다.")
    st.stop()

idx      = st.session_state["vp_idx"]
n_items  = len(questions)
total_q  = st.session_state.get("vp_total_q", n_items)

# ── Done screen ─────────────────────────────────────────────────────────────────
if st.session_state.get("vp_done"):
    score = st.session_state["vp_score"]
    pct   = round(score / total_q * 100) if total_q else 0
    wrong = total_q - score
    msg   = ("완벽해요! 🎉" if pct == 100 else
             "훌륭합니다!"   if pct >= 80 else
             "잘 하셨어요!"  if pct >= 60 else
             "다시 도전해보세요")

    st.markdown(f"""
    <div class="result-hero">
        <div class="rh-pct">{pct}%</div>
        <div class="rh-score">{score} / {total_q} 정답</div>
        <div class="rh-msg">{msg}</div>
    </div>
    <div class="stat-row">
        <div class="stat-box"><div class="stat-val">{score}</div><div class="stat-lbl">정답</div></div>
        <div class="stat-box"><div class="stat-val">{wrong}</div><div class="stat-lbl">오답</div></div>
        <div class="stat-box"><div class="stat-val">{total_q}</div><div class="stat-lbl">전체</div></div>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.get("vp_is_test"):
        components.html("""<script>(function(){
            var p=window.parent;
            if(p._greTimerInterval){clearInterval(p._greTimerInterval);p._greTimerInterval=null;}
            var el=p.document.getElementById('gre-countdown');
            if(el)el.remove();
        })();</script>""", height=0)

    if st.button("다시 풀기", use_container_width=True, type="primary"):
        reset_session()
        st.rerun()
    st.stop()

# ── Timer (test mode) ────────────────────────────────────────────────────────────
if st.session_state.get("vp_is_test") and not st.session_state.get("vp_done"):
    end_ts = st.session_state.get("vp_test_end", 0)
    components.html(f"""<script>(function(){{
        var endTime={end_ts};
        var p=window.parent;
        if(p._greTimerInterval){{clearInterval(p._greTimerInterval);}}
        var el=p.document.getElementById('gre-countdown');
        if(!el){{
            el=p.document.createElement('div');
            el.id='gre-countdown';
            el.style.cssText='position:fixed;top:60px;right:20px;background:#1E293B;color:white;padding:8px 18px;border-radius:10px;font-size:1.15rem;font-weight:700;font-family:monospace;z-index:99999;box-shadow:0 4px 12px rgba(0,0,0,0.3)';
            p.document.body.appendChild(el);
        }}
        function update(){{
            var r=endTime-Math.floor(Date.now()/1000);
            if(r<=0){{el.textContent='⏰ 00:00';el.style.background='#DC2626';clearInterval(p._greTimerInterval);return;}}
            var m=Math.floor(r/60),s=r%60;
            el.textContent='⏱ '+String(m).padStart(2,'0')+':'+String(s).padStart(2,'0');
            el.style.background=r<=120?'#DC2626':r<=300?'#D97706':'#1E293B';
        }}
        update();
        p._greTimerInterval=setInterval(update,1000);
    }})();</script>""", height=0)

# ── Progress ────────────────────────────────────────────────────────────────────
st.progress(idx / n_items)
st.caption(f"세트 {idx + 1} / {n_items}   ·   점수 {st.session_state['vp_score']} / {total_q}")

item = questions[idx]


# ── Shared helpers ───────────────────────────────────────────────────────────────
def render_answer(q, q_id, submitted):
    blanks       = q.get("blanks", [])
    user_answers = st.session_state["vp_answers"].get(q_id, {})
    q_type       = q["type"]

    if q_type == "text_completion":
        for blank in blanks:
            label   = blank.get("label") or "Blank"
            choices = blank["choices"]
            keys    = list(choices.keys())
            prev    = user_answers.get(label)
            prev_i  = keys.index(prev) if prev in keys else None
            sel = st.radio(
                f"**{label}**",
                options=keys,
                format_func=lambda k, c=choices: f"{k}.  {c[k]}",
                index=prev_i,
                key=f"{q_id}_{label}",
                disabled=submitted,
                horizontal=len(keys) <= 3,
            )
            user_answers[label] = sel

    elif q_type == "sentence_equivalence":
        choices = blanks[0]["choices"] if blanks else {}
        st.caption("✏️  정답 **2개**를 선택하세요.")
        selected = []
        for k, v in choices.items():
            prev_c  = k in user_answers.get("SE", [])
            checked = st.checkbox(f"{k}.  {v}", value=prev_c,
                                  key=f"{q_id}_SE_{k}", disabled=submitted)
            if checked:
                selected.append(k)
        user_answers["SE"] = selected

    elif q_type == "reading_comprehension":
        subtype = q.get("subtype", "single_answer")
        choices = blanks[0]["choices"] if blanks else {}
        if subtype == "multi_answer":
            st.caption("✏️  해당하는 것을 **모두** 선택하세요.")
            selected = []
            for k, v in choices.items():
                prev_c  = k in user_answers.get("RC", [])
                checked = st.checkbox(f"{k}.  {v}", value=prev_c,
                                      key=f"{q_id}_RC_{k}", disabled=submitted)
                if checked:
                    selected.append(k)
            user_answers["RC"] = selected
        else:
            keys   = list(choices.keys())
            prev   = user_answers.get("RC_single")
            prev_i = keys.index(prev) if prev in keys else None
            sel    = st.radio(
                "정답 선택",
                options=keys,
                format_func=lambda k, c=choices: f"{k}.  {c[k]}",
                index=prev_i,
                key=f"{q_id}_RC_single",
                disabled=submitted,
            )
            user_answers["RC_single"] = sel

    elif q_type == "critical_reasoning":
        choices = blanks[0]["choices"] if blanks else {}
        keys    = list(choices.keys())
        prev    = user_answers.get("CR_single")
        prev_i  = keys.index(prev) if prev in keys else None
        sel     = st.radio(
            "정답 선택",
            options=keys,
            format_func=lambda k, c=choices: f"{k}.  {c[k]}",
            index=prev_i,
            key=f"{q_id}_CR_single",
            disabled=submitted,
        )
        user_answers["CR_single"] = sel

    st.session_state["vp_answers"][q_id] = user_answers
    return user_answers


def get_user_list(q, ua):
    qt = q["type"]
    if qt == "text_completion":
        return [ua.get(b.get("label") or "Blank") for b in q.get("blanks", [])]
    if qt == "sentence_equivalence":
        return sorted(ua.get("SE", []))
    if qt == "reading_comprehension":
        if q.get("subtype") == "multi_answer":
            return sorted(ua.get("RC", []))
        a = ua.get("RC_single")
        return [a] if a else []
    if qt == "critical_reasoning":
        a = ua.get("CR_single")
        return [a] if a else []
    return []


def is_correct(q, user_list):
    return sorted(u for u in user_list if u) == sorted(q.get("correct", []))


def render_feedback(q, ua):
    ul      = get_user_list(q, ua)
    correct = q.get("correct", [])
    ok      = is_correct(q, ul)

    if ok:
        st.markdown(
            f'<div class="fb-correct">✅ 정답!<div class="fb-detail">정답: {", ".join(correct)}</div></div>',
            unsafe_allow_html=True,
        )
    else:
        blanks  = q.get("blanks", [])
        q_type  = q.get("type", "")
        details = []
        if q_type == "text_completion":
            for i, k in enumerate(correct):
                b = blanks[i] if i < len(blanks) else {}
                v = b.get("choices", {}).get(k, "")
                details.append(f"{k}. {v}" if v else k)
        else:
            choices = blanks[0]["choices"] if blanks else {}
            for k in correct:
                v = choices.get(k, "")
                details.append(f"{k}. {v}" if v else k)
        st.markdown(
            f'<div class="fb-wrong">❌ 오답<div class="fb-detail">정답: {esc(", ".join(details))}</div></div>',
            unsafe_allow_html=True,
        )

    with st.expander("💡 해설 보기"):
        st.write(q.get("explanation", "해설이 없습니다."))


# ── RC Group 렌더링 ──────────────────────────────────────────────────────────────
if item.get("type") == "rc_group":
    group_qs  = item["questions"]
    group_id  = f"rcg_{idx}"
    submitted = st.session_state["vp_submitted"].get(group_id, False)

    n_q = len(group_qs)
    st.markdown(
        f'<div class="badge-row">'
        f'<span class="badge b-rc">RC</span>'
        f'<span class="badge b-medium">{n_q}문항</span>'
        f'</div>',
        unsafe_allow_html=True,
    )

    # 지문 한 번만 출력
    st.markdown(
        f'<div class="passage-box">{esc(item["passage"])}</div>',
        unsafe_allow_html=True,
    )

    # 각 문항 출력
    for i, gq in enumerate(group_qs):
        st.markdown(f'<div class="stem-box"><strong>Q{i + 1}.</strong> {esc(gq.get("stem", ""))}</div>',
                    unsafe_allow_html=True)
        render_answer(gq, gq["id"], submitted)
        if submitted:
            render_feedback(gq, st.session_state["vp_answers"].get(gq["id"], {}))
        st.markdown("---")

    # 제출 / 다음
    col1, col2 = st.columns(2)
    with col1:
        if not submitted:
            if st.button("제출 (Submit)", type="primary", use_container_width=True):
                missing = any(
                    not get_user_list(gq, st.session_state["vp_answers"].get(gq["id"], {}))
                    or any(a is None for a in get_user_list(gq, st.session_state["vp_answers"].get(gq["id"], {})))
                    for gq in group_qs
                )
                if missing:
                    st.warning("모든 문항을 선택하세요.")
                else:
                    st.session_state["vp_submitted"][group_id] = True
                    for gq in group_qs:
                        ua = st.session_state["vp_answers"].get(gq["id"], {})
                        if is_correct(gq, get_user_list(gq, ua)):
                            st.session_state["vp_score"] += 1
                    st.rerun()
    with col2:
        if submitted:
            label = "다음 문제 →" if idx + 1 < n_items else "결과 보기"
            if st.button(label, type="primary", use_container_width=True):
                if idx + 1 < n_items:
                    st.session_state["vp_idx"] += 1
                else:
                    st.session_state["vp_done"] = True
                st.rerun()

# ── TC / SE / 단독 RC 렌더링 ────────────────────────────────────────────────────
else:
    q         = item
    q_id      = q["id"]
    submitted = st.session_state["vp_submitted"].get(q_id, False)

    tc = TYPE_CSS.get(q["type"], "b-tc")
    dc = DIFF_CSS.get(q["difficulty"], "b-easy")
    ts = TYPE_SHORT.get(q["type"], q["type"])
    dl = DIFF_LABEL.get(q["difficulty"], q["difficulty"])
    st.markdown(
        f'<div class="badge-row">'
        f'<span class="badge {tc}">{ts}</span>'
        f'<span class="badge {dc}">{dl}</span>'
        f'</div>',
        unsafe_allow_html=True,
    )

    if q.get("passage"):
        st.markdown(
            f'<div class="passage-box">{esc(q["passage"])}</div>',
            unsafe_allow_html=True,
        )

    if q.get("stem"):
        st.markdown(f'<div class="stem-box">{esc(q["stem"])}</div>', unsafe_allow_html=True)

    user_answers = render_answer(q, q_id, submitted)

    col1, col2 = st.columns(2)
    with col1:
        if not submitted:
            if st.button("제출 (Submit)", type="primary", use_container_width=True):
                ul = get_user_list(q, user_answers)
                if not ul or any(a is None for a in ul):
                    st.warning("모든 빈칸을 선택하세요.")
                else:
                    st.session_state["vp_submitted"][q_id] = True
                    if is_correct(q, ul):
                        st.session_state["vp_score"] += 1
                    st.rerun()
    with col2:
        if submitted:
            label = "다음 문제 →" if idx + 1 < n_items else "결과 보기"
            if st.button(label, type="primary", use_container_width=True):
                if idx + 1 < n_items:
                    st.session_state["vp_idx"] += 1
                else:
                    st.session_state["vp_done"] = True
                st.rerun()

    if submitted:
        render_feedback(q, user_answers)
