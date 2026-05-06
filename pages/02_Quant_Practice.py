"""GRE Quantitative Reasoning Practice — QC, MC, MCM, NE"""
import json
import random
from pathlib import Path

import streamlit as st

from utils import inject_css, esc

st.set_page_config(page_title="Quant Practice", page_icon="🔢", layout="centered")
inject_css()

DATA_FILE = Path(__file__).parent.parent / "gre_content" / "practice_questions.json"

DIFF_LABEL = {"easy": "Easy", "medium": "Medium", "hard": "Hard"}
DIFF_CSS   = {"easy": "b-easy", "medium": "b-medium", "hard": "b-hard"}
TYPE_LABEL = {
    "quantitative_comparison":   "Quantitative Comparison",
    "multiple_choice":           "Multiple Choice",
    "multiple_choice_select_all":"Multiple Choice — Select All",
    "numeric_entry":             "Numeric Entry",
}
TYPE_CSS   = {
    "quantitative_comparison":   "b-qc",
    "multiple_choice":           "b-mc",
    "multiple_choice_select_all":"b-mcm",
    "numeric_entry":             "b-ne",
}
TYPE_SHORT = {
    "quantitative_comparison":   "QC",
    "multiple_choice":           "MC",
    "multiple_choice_select_all":"MCM",
    "numeric_entry":             "NE",
}

QC_CHOICES = {
    "A": "Quantity A is greater.",
    "B": "Quantity B is greater.",
    "C": "The two quantities are equal.",
    "D": "The relationship cannot be determined from the information given.",
}


@st.cache_data
def load_questions():
    with open(DATA_FILE, encoding="utf-8") as f:
        return json.load(f)["quant"]


def reset_session():
    for k in list(st.session_state.keys()):
        if k.startswith("qp_"):
            del st.session_state[k]


all_questions = load_questions()

st.title("🔢 Quantitative Reasoning Practice")

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🔢 Quant")
    st.markdown('<hr class="sdiv">', unsafe_allow_html=True)

    sel_diff = st.multiselect(
        "난이도", options=["easy", "medium", "hard"],
        default=["easy", "medium", "hard"],
        format_func=lambda x: DIFF_LABEL[x],
    )
    sel_type = st.multiselect(
        "문제 유형",
        options=["quantitative_comparison", "multiple_choice",
                 "multiple_choice_select_all", "numeric_entry"],
        default=["quantitative_comparison", "multiple_choice",
                 "multiple_choice_select_all", "numeric_entry"],
        format_func=lambda x: TYPE_LABEL[x],
    )
    st.markdown('<hr class="sdiv">', unsafe_allow_html=True)
    if st.button("🚀  Start / Restart", type="primary", use_container_width=True):
        reset_session()
        filtered = [q for q in all_questions
                    if q["difficulty"] in sel_diff and q["type"] in sel_type]
        random.shuffle(filtered)
        st.session_state.update({
            "qp_questions": filtered, "qp_idx": 0,
            "qp_answers": {}, "qp_submitted": {},
            "qp_score": 0, "qp_done": False,
        })
        st.rerun()
    st.caption("QC: Qty 비교 | MC: 5지선다 | MCM: 복수선택 | NE: 숫자입력")

# ── Guard ──────────────────────────────────────────────────────────────────────
if "qp_questions" not in st.session_state:
    st.markdown("""
    <div style="text-align:center; padding:60px 20px;">
      <div style="font-size:3.5rem;">🔢</div>
      <h2 style="color:#1E293B; margin-top:12px;">Quantitative Reasoning</h2>
      <p style="color:#64748B;">사이드바에서 난이도·유형을 선택하고<br><strong>Start</strong>를 눌러 시작하세요.</p>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

questions = st.session_state["qp_questions"]
if not questions:
    st.warning("선택한 조건에 해당하는 문제가 없습니다.")
    st.stop()

idx   = st.session_state["qp_idx"]
total = len(questions)

# ── Done screen ────────────────────────────────────────────────────────────────
if st.session_state.get("qp_done"):
    score = st.session_state["qp_score"]
    pct   = round(score / total * 100)
    wrong = total - score
    msg   = "완벽해요! 🎉" if pct == 100 else "훌륭합니다!" if pct >= 80 else "잘 하셨어요!" if pct >= 60 else "다시 도전해보세요"

    st.markdown(f"""
    <div class="result-hero">
        <div class="rh-pct">{pct}%</div>
        <div class="rh-score">{score} / {total} 정답</div>
        <div class="rh-msg">{msg}</div>
    </div>
    <div class="stat-row">
        <div class="stat-box"><div class="stat-val">{score}</div><div class="stat-lbl">정답</div></div>
        <div class="stat-box"><div class="stat-val">{wrong}</div><div class="stat-lbl">오답</div></div>
        <div class="stat-box"><div class="stat-val">{total}</div><div class="stat-lbl">전체</div></div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("다시 풀기", use_container_width=True, type="primary"):
        reset_session()
        st.rerun()
    st.stop()

# ── Progress ───────────────────────────────────────────────────────────────────
st.progress(idx / total)
st.caption(f"문제 {idx + 1} / {total}   ·   점수 {st.session_state['qp_score']}")

q      = questions[idx]
q_id   = q["id"]
submitted = st.session_state["qp_submitted"].get(q_id, False)

# ── Badge row ──────────────────────────────────────────────────────────────────
tc = TYPE_CSS.get(q["type"], "b-mc")
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

# ── Context ────────────────────────────────────────────────────────────────────
if q.get("context"):
    st.markdown(
        f'<div class="context-box">📋  {esc(q["context"])}</div>',
        unsafe_allow_html=True,
    )

# ── QC comparison grid ─────────────────────────────────────────────────────────
if q["type"] == "quantitative_comparison":
    qa = esc(q.get("quantity_a", "—"))
    qb = esc(q.get("quantity_b", "—"))
    st.markdown(f"""
    <div class="qc-wrap">
        <div class="qc-a-cell">
            <div class="qc-label">Quantity A</div>
            <div class="qc-val">{qa}</div>
        </div>
        <div class="qc-vs-cell">vs</div>
        <div class="qc-b-cell">
            <div class="qc-label">Quantity B</div>
            <div class="qc-val">{qb}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── Stem ──────────────────────────────────────────────────────────────────────
if q.get("stem"):
    st.markdown(f'<div class="stem-box">{esc(q["stem"])}</div>', unsafe_allow_html=True)


# ── Answer widgets ─────────────────────────────────────────────────────────────
def render_answer(q, q_id, submitted):
    ua     = st.session_state["qp_answers"].get(q_id, {})
    blanks = q.get("blanks", [])
    qt     = q["type"]

    if qt == "quantitative_comparison":
        keys   = list(QC_CHOICES.keys())
        prev   = ua.get("QC")
        prev_i = keys.index(prev) if prev in keys else None
        sel    = st.radio(
            "정답 선택",
            options=keys,
            format_func=lambda k: f"{k}.  {QC_CHOICES[k]}",
            index=prev_i,
            key=f"{q_id}_QC",
            disabled=submitted,
        )
        ua["QC"] = sel

    elif qt == "multiple_choice":
        choices = blanks[0]["choices"] if blanks else {}
        keys    = list(choices.keys())
        prev    = ua.get("MC")
        prev_i  = keys.index(prev) if prev in keys else None
        sel     = st.radio(
            "정답 선택",
            options=keys,
            format_func=lambda k, c=choices: f"{k}.  {c[k]}",
            index=prev_i,
            key=f"{q_id}_MC",
            disabled=submitted,
        )
        ua["MC"] = sel

    elif qt == "multiple_choice_select_all":
        choices = blanks[0]["choices"] if blanks else {}
        st.caption("✏️  해당하는 것을 **모두** 선택하세요.")
        selected = []
        for k, v in choices.items():
            prev_c  = k in ua.get("MCM", [])
            checked = st.checkbox(f"{k}.  {v}", value=prev_c,
                                  key=f"{q_id}_MCM_{k}", disabled=submitted)
            if checked:
                selected.append(k)
        ua["MCM"] = selected

    elif qt == "numeric_entry":
        label  = blanks[0].get("label", "Answer") if blanks else "Answer"
        prev_v = ua.get("NE", "")
        val    = st.text_input(
            f"**{label}**", value=prev_v,
            placeholder="숫자를 입력하세요",
            key=f"{q_id}_NE", disabled=submitted,
        )
        ua["NE"] = val.strip()

    st.session_state["qp_answers"][q_id] = ua
    return ua


user_answers = render_answer(q, q_id, submitted)


def get_user_list(q, ua):
    qt = q["type"]
    if qt == "quantitative_comparison":
        a = ua.get("QC"); return [a] if a else []
    if qt == "multiple_choice":
        a = ua.get("MC"); return [a] if a else []
    if qt == "multiple_choice_select_all":
        return sorted(ua.get("MCM", []))
    if qt == "numeric_entry":
        a = ua.get("NE", "").strip(); return [a] if a else []
    return []


def is_correct(q, ul):
    correct = q.get("correct", [])
    if q["type"] == "numeric_entry":
        try:
            uv = float(ul[0]) if ul else None
            cv = float(correct[0]) if correct else None
            return uv is not None and cv is not None and abs(uv - cv) < 0.005
        except ValueError:
            return ul == correct
    return sorted(ul) == sorted(correct)


# ── Submit / Next ──────────────────────────────────────────────────────────────
col1, col2 = st.columns(2)
with col1:
    if not submitted:
        if st.button("제출 (Submit)", type="primary", use_container_width=True):
            ul = get_user_list(q, user_answers)
            if not ul or (len(ul) == 1 and not ul[0]):
                st.warning("답을 선택하거나 입력하세요.")
            else:
                st.session_state["qp_submitted"][q_id] = True
                if is_correct(q, ul):
                    st.session_state["qp_score"] += 1
                st.rerun()
with col2:
    if submitted:
        label = "다음 문제 →" if idx + 1 < total else "결과 보기"
        if st.button(label, type="primary", use_container_width=True):
            if idx + 1 < total:
                st.session_state["qp_idx"] += 1
            else:
                st.session_state["qp_done"] = True
            st.rerun()

# ── Feedback ───────────────────────────────────────────────────────────────────
if submitted:
    ul      = get_user_list(q, user_answers)
    correct = q.get("correct", [])
    ok      = is_correct(q, ul)
    blanks  = q.get("blanks", [])

    if ok:
        st.markdown(
            f'<div class="fb-correct">✅ 정답!<div class="fb-detail">정답: {esc(", ".join(correct))}</div></div>',
            unsafe_allow_html=True,
        )
    else:
        qt = q["type"]
        if qt == "quantitative_comparison":
            details = [f"{k}. {QC_CHOICES.get(k, '')}" for k in correct]
        elif qt in ("multiple_choice", "multiple_choice_select_all"):
            choices = blanks[0]["choices"] if blanks else {}
            details = [f"{k}. {choices.get(k, '')}" for k in correct]
        else:
            details = correct
        st.markdown(
            f'<div class="fb-wrong">❌ 오답<div class="fb-detail">정답: {esc(", ".join(details))}</div></div>',
            unsafe_allow_html=True,
        )

    with st.expander("💡 해설 보기"):
        st.write(q.get("explanation", "해설이 없습니다."))
