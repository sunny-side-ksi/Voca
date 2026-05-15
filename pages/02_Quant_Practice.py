"""GRE Quantitative Reasoning Practice — QC / MC (Single·Multiple) / NE / DI"""
import json
import random
from pathlib import Path

import streamlit as st
from PIL import Image

from utils import inject_css, esc

DI_IMAGES_DIR = Path(__file__).parent.parent / "di_images"

st.set_page_config(page_title="Quant Practice", page_icon="🔢", layout="centered")
inject_css()

DATA_FILE = Path(__file__).parent.parent / "gre_content" / "practice_questions.json"

# ── Type / subtype → display info ─────────────────────────────────────────────
# key: (type, subtype)  value: (label, badge_css, short)
TYPE_META = {
    ("quantitative_comparison", None):      ("QC · Quantitative Comparison", "b-qc",  "QC"),
    ("multiple_choice",         "single_answer"):   ("MC · Single Answer",           "b-mc",  "MC·Single"),
    ("multiple_choice",         "multiple_answers"): ("MC · Multiple Answers",       "b-mcm", "MC·Multi"),
    ("numeric_entry",           None):      ("NE · Numeric Entry",                   "b-ne",  "NE"),
    ("data_interpretation",     None):      ("DI · Data Interpretation",             "b-test","DI"),
}

def q_meta(q):
    key = (q["type"], q.get("subtype"))
    return TYPE_META.get(key, TYPE_META.get((q["type"], None),
           ("Unknown", "b-mc", "?")))

QC_CHOICES = {
    "A": "Quantity A is greater.",
    "B": "Quantity B is greater.",
    "C": "The two quantities are equal.",
    "D": "The relationship cannot be determined from the information given.",
}

DIFF_LABEL = {"easy": "Easy", "medium": "Medium", "hard": "Hard"}
DIFF_CSS   = {"easy": "b-easy", "medium": "b-medium", "hard": "b-hard"}

FILTER_OPTIONS = [
    ("QC",       "QC · Quantitative Comparison"),
    ("MC·1",     "MC · Single Answer"),
    ("MC·M",     "MC · Multiple Answers"),
    ("NE",       "NE · Numeric Entry"),
    ("DI",       "DI · Data Interpretation"),
]
FILTER_TO_TYPE = {
    "QC":   lambda q: q["type"] == "quantitative_comparison",
    "MC·1": lambda q: q["type"] == "multiple_choice" and q.get("subtype") == "single_answer",
    "MC·M": lambda q: q["type"] == "multiple_choice" and q.get("subtype") == "multiple_answers",
    "NE":   lambda q: q["type"] == "numeric_entry",
    "DI":   lambda q: q["type"] == "data_interpretation",
}


@st.cache_data(ttl=120)
def load_questions():
    with open(DATA_FILE, encoding="utf-8") as f:
        return json.load(f)["quant"]


ALL_TYPES = [k for k, _ in FILTER_OPTIONS]
ALL_DIFFS = ["easy", "medium", "hard"]


def reset_session():
    for k in list(st.session_state.keys()):
        if k.startswith("qp_"):
            del st.session_state[k]


def reset_filters():
    """필터 세션 상태 초기화 — 옵션 목록이 바뀌었을 때 stale 값 제거."""
    st.session_state["qp_f_type"] = ALL_TYPES
    st.session_state["qp_f_diff"] = ALL_DIFFS


# 필터 세션 초기화: qp_f_type에 새 유형이 누락된 경우 전체 리셋
if "qp_f_type" not in st.session_state or not set(ALL_TYPES).issubset(set(st.session_state["qp_f_type"])):
    reset_filters()

all_questions = load_questions()

st.title("🔢 Quantitative Reasoning Practice")

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🔢 Quant")
    st.markdown('<hr class="sdiv">', unsafe_allow_html=True)

    sel_type_keys = st.multiselect(
        "문제 유형",
        options=ALL_TYPES,
        default=ALL_TYPES,
        format_func=lambda k: dict(FILTER_OPTIONS)[k],
        key="qp_f_type",
    )

    sel_diff = st.multiselect(
        "난이도",
        options=ALL_DIFFS,
        default=ALL_DIFFS,
        format_func=lambda x: DIFF_LABEL[x],
        key="qp_f_diff",
    )

    # 항상 최신 데이터 기준으로 topic 목록 생성 (DI 포함)
    fresh_for_topics = load_questions()
    topics_available = sorted({str(q.get("set", "기타")) for q in fresh_for_topics if q.get("set")})
    sel_topic = st.multiselect(
        "토픽/출처",
        options=topics_available,
        default=topics_available,
        key="qp_f_topic",
    )

    n_max = st.slider("최대 문제 수", 5, 50, 20)

    st.markdown('<hr class="sdiv">', unsafe_allow_html=True)
    if st.button("🚀  Start / Restart", type="primary", use_container_width=True):
        reset_session()
        fresh_q = load_questions()
        type_fns = [FILTER_TO_TYPE[k] for k in sel_type_keys if k in FILTER_TO_TYPE]
        filtered = [
            q for q in fresh_q
            if any(fn(q) for fn in type_fns)
            and q["difficulty"] in sel_diff
            and str(q.get("set", "")) in sel_topic
            and q.get("correct")
        ]
        random.shuffle(filtered)
        filtered = filtered[:n_max]
        st.session_state.update({
            "qp_questions": filtered, "qp_idx": 0,
            "qp_answers": {}, "qp_submitted": {},
            "qp_score": 0, "qp_done": False,
        })
        st.rerun()

    st.caption(
        "**QC** Qty 비교  |  **MC·1** 5지선다  |  "
        "**MC·M** 복수선택  |  **NE** 숫자입력  |  **DI** 자료해석"
    )

# ── Guard ──────────────────────────────────────────────────────────────────────
if "qp_questions" not in st.session_state:
    st.markdown("""
    <div style="text-align:center; padding:60px 20px;">
      <div style="font-size:3.5rem;">🔢</div>
      <h2 style="color:#1E293B; margin-top:12px;">Quantitative Reasoning</h2>
      <p style="color:#64748B;">사이드바에서 유형·난이도·출처를 선택하고<br><strong>Start</strong>를 눌러 시작하세요.</p>
      <div style="margin-top:24px; display:flex; gap:8px; justify-content:center; flex-wrap:wrap;">
        <span class="badge b-qc">QC</span>
        <span class="badge b-mc">MC·Single</span>
        <span class="badge b-mcm">MC·Multi</span>
        <span class="badge b-ne">NE</span>
        <span class="badge b-test">DI</span>
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

questions = st.session_state["qp_questions"]
if not questions:
    st.warning("선택한 조건에 해당하는 문제가 없습니다. 필터를 조정해 보세요.")
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

    wrongs = [
        (q, a) for q, a in zip(
            st.session_state.get("qp_q_list", []),
            st.session_state.get("qp_ans_list", [])
        ) if not a["correct"]
    ]
    if wrongs:
        items_html = ""
        for wq, wa in wrongs:
            stem = wq.get("stem") or wq.get("quantity_a", "")
            items_html += (
                f'<div class="wrong-item">'
                f'<span class="wi-word">{esc(stem[:60])}</span>'
                f'<span class="wi-sep">→</span>'
                f'<span class="wi-ans">정답: {esc(", ".join(wq.get("correct",[])))}</span>'
                f'</div>'
            )
        st.markdown(
            f'<div class="wrong-list">'
            f'<div class="wrong-hdr">오답 목록 ({len(wrongs)}개)</div>'
            f'{items_html}</div>',
            unsafe_allow_html=True,
        )

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
label, badge_css, short = q_meta(q)
dc = DIFF_CSS.get(q["difficulty"], "b-easy")
dl = DIFF_LABEL.get(q["difficulty"], q["difficulty"])
st.markdown(
    f'<div class="badge-row">'
    f'<span class="badge {badge_css}">{short}</span>'
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

# ── DI chart image ────────────────────────────────────────────────────────────
if q.get("di_image"):
    img_path = DI_IMAGES_DIR / q["di_image"]
    if img_path.exists():
        di_title = q.get("di_title", "")
        if di_title:
            st.markdown(
                f'<div class="di-title">{esc(di_title)}</div>',
                unsafe_allow_html=True,
            )
        st.image(str(img_path), use_container_width=True)

# ── QC grid ───────────────────────────────────────────────────────────────────
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
    sub    = q.get("subtype")

    if qt == "quantitative_comparison":
        keys  = list(QC_CHOICES.keys())
        prev  = ua.get("sel")
        prev_i = keys.index(prev) if prev in keys else None
        sel = st.radio(
            "정답 선택",
            options=keys,
            format_func=lambda k: f"{k}.  {QC_CHOICES[k]}",
            index=prev_i,
            key=f"{q_id}_QC",
            disabled=submitted,
        )
        ua["sel"] = sel

    elif qt == "multiple_choice" and sub == "single_answer":
        choices = blanks[0]["choices"] if blanks else {}
        keys    = list(choices.keys())
        prev    = ua.get("sel")
        prev_i  = keys.index(prev) if prev in keys else None
        sel = st.radio(
            "정답 선택",
            options=keys,
            format_func=lambda k, c=choices: f"{k}.  {c[k]}",
            index=prev_i,
            key=f"{q_id}_MC",
            disabled=submitted,
        )
        ua["sel"] = sel

    elif qt == "multiple_choice" and sub == "multiple_answers":
        choices = blanks[0]["choices"] if blanks else {}
        st.caption("✏️  해당하는 것을 **모두** 선택하세요 (Indicate all such answers).")
        selected = []
        for k, v in choices.items():
            checked = st.checkbox(
                f"{k}.  {v}", value=(k in ua.get("sel", [])),
                key=f"{q_id}_MA_{k}", disabled=submitted,
            )
            if checked:
                selected.append(k)
        ua["sel"] = selected

    elif qt == "numeric_entry":
        label = blanks[0].get("label", "Answer") if blanks else "Answer"
        val = st.text_input(
            f"**{label}**", value=ua.get("sel", ""),
            placeholder="숫자 또는 분수 입력 (예: 7, 3/2, 0.5)",
            key=f"{q_id}_NE", disabled=submitted,
        )
        ua["sel"] = val.strip()

    elif qt == "data_interpretation":
        choices = blanks[0]["choices"] if blanks else {}
        if sub == "multiple_answers":
            st.caption("✏️  해당하는 것을 **모두** 선택하세요 (Indicate all such answers).")
            selected = []
            for k, v in choices.items():
                checked = st.checkbox(
                    f"{k}.  {v}", value=(k in ua.get("sel", [])),
                    key=f"{q_id}_DI_MA_{k}", disabled=submitted,
                )
                if checked:
                    selected.append(k)
            ua["sel"] = selected
        else:
            keys   = list(choices.keys())
            prev   = ua.get("sel")
            prev_i = keys.index(prev) if prev in keys else None
            sel = st.radio(
                "정답 선택",
                options=keys,
                format_func=lambda k, c=choices: f"{k}.  {c[k]}",
                index=prev_i,
                key=f"{q_id}_DI",
                disabled=submitted,
            )
            ua["sel"] = sel

    st.session_state["qp_answers"][q_id] = ua
    return ua


user_answers = render_answer(q, q_id, submitted)


def get_user_list(q, ua):
    sel = ua.get("sel")
    if isinstance(sel, list):
        return sorted(sel)
    if sel is not None and str(sel).strip():
        return [str(sel)]
    return []


def is_correct(q, ul):
    correct = q.get("correct", [])
    if not correct:
        return False
    if q["type"] == "numeric_entry":
        try:
            if "/" in (ul[0] if ul else ""):
                n, d = ul[0].split("/")
                uv = float(n) / float(d)
            else:
                uv = float(ul[0]) if ul else None
            cv = float(correct[0])
            return uv is not None and abs(uv - cv) < 0.005
        except (ValueError, ZeroDivisionError, IndexError):
            pass
        return sorted(ul) == sorted(correct)
    return sorted(ul) == sorted(correct)


# ── Submit / Next ──────────────────────────────────────────────────────────────
col1, col2 = st.columns(2)
with col1:
    if not submitted:
        if st.button("제출 (Submit)", type="primary", use_container_width=True):
            ul = get_user_list(q, user_answers)
            if not ul:
                st.warning("답을 선택하거나 입력하세요.")
            else:
                ok = is_correct(q, ul)
                st.session_state["qp_submitted"][q_id] = True
                if ok:
                    st.session_state["qp_score"] += 1
                # record for wrong-list on result screen
                st.session_state.setdefault("qp_q_list", []).append(q)
                st.session_state.setdefault("qp_ans_list", []).append(
                    {"correct": ok, "user": ul}
                )
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
    qt      = q["type"]
    sub     = q.get("subtype")

    def fmt_correct():
        if qt == "quantitative_comparison":
            return ", ".join(f"{k}. {QC_CHOICES.get(k,'')}" for k in correct)
        if qt in ("multiple_choice", "data_interpretation"):
            choices = blanks[0]["choices"] if blanks else {}
            return ", ".join(f"{k}. {choices.get(k,'')}" for k in correct)
        return ", ".join(correct)

    if ok:
        st.markdown(
            f'<div class="fb-correct">✅ 정답!<div class="fb-detail">정답: {esc(fmt_correct())}</div></div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f'<div class="fb-wrong">❌ 오답<div class="fb-detail">정답: {esc(fmt_correct())}</div></div>',
            unsafe_allow_html=True,
        )

    if q.get("explanation"):
        with st.expander("💡 해설 보기"):
            st.write(q["explanation"])
