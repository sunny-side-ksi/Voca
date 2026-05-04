"""GRE Quantitative Reasoning Practice — QC, MC, Multi-select, Numeric Entry"""
import json
from pathlib import Path

import streamlit as st

st.set_page_config(page_title="GRE Quant Practice", page_icon="🔢", layout="centered")

DATA_FILE = Path(__file__).parent.parent / "gre_content" / "practice_questions.json"

DIFFICULTY_LABELS = {"easy": "Easy", "medium": "Medium", "hard": "Hard"}
TYPE_LABELS = {
    "quantitative_comparison": "Quantitative Comparison (QC)",
    "multiple_choice": "Multiple Choice (MC)",
    "multiple_choice_select_all": "Multiple Choice — Select All (MCM)",
    "numeric_entry": "Numeric Entry (NE)",
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
        data = json.load(f)
    return data.get("quant", [])


def reset_session():
    for key in list(st.session_state.keys()):
        if key.startswith("qp_"):
            del st.session_state[key]


# ── Init ───────────────────────────────────────────────────────────────────────
all_questions = load_questions()

st.title("🔢 Quantitative Reasoning Practice")

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("Settings")

    selected_difficulties = st.multiselect(
        "Difficulty",
        options=["easy", "medium", "hard"],
        default=["easy", "medium", "hard"],
        format_func=lambda x: DIFFICULTY_LABELS[x],
    )

    selected_types = st.multiselect(
        "Question Type",
        options=["quantitative_comparison", "multiple_choice", "multiple_choice_select_all", "numeric_entry"],
        default=["quantitative_comparison", "multiple_choice", "multiple_choice_select_all", "numeric_entry"],
        format_func=lambda x: TYPE_LABELS[x],
    )

    if st.button("Start / Restart", type="primary", use_container_width=True):
        reset_session()
        filtered = [
            q for q in all_questions
            if q["difficulty"] in selected_difficulties and q["type"] in selected_types
        ]
        st.session_state["qp_questions"] = filtered
        st.session_state["qp_idx"] = 0
        st.session_state["qp_answers"] = {}
        st.session_state["qp_submitted"] = {}
        st.session_state["qp_score"] = 0
        st.session_state["qp_done"] = False
        st.rerun()

    st.divider()
    st.caption("QC: Qty 비교 | MC: 5지선다 | MCM: 복수선택 | NE: 숫자 입력")

# ── Guard ──────────────────────────────────────────────────────────────────────
if "qp_questions" not in st.session_state:
    st.info("사이드바에서 난이도·유형을 선택하고 **Start**를 눌러 시작하세요.")
    st.stop()

questions = st.session_state["qp_questions"]
if not questions:
    st.warning("선택한 조건에 해당하는 문제가 없습니다. 필터를 조정하세요.")
    st.stop()

idx = st.session_state["qp_idx"]
total = len(questions)

# ── Done screen ────────────────────────────────────────────────────────────────
if st.session_state.get("qp_done"):
    score = st.session_state["qp_score"]
    st.success(f"## 완료! 점수: {score} / {total}")
    st.progress(score / total)
    pct = round(score / total * 100)
    st.write(f"정답률 **{pct}%**")
    if st.button("다시 풀기", use_container_width=True):
        reset_session()
        st.rerun()
    st.stop()

# ── Progress ───────────────────────────────────────────────────────────────────
st.progress(idx / total)
st.caption(f"문제 {idx + 1} / {total}")

q = questions[idx]
q_id = q["id"]
submitted = st.session_state["qp_submitted"].get(q_id, False)

# ── Badge ──────────────────────────────────────────────────────────────────────
diff_color = {"easy": "🟢", "medium": "🟡", "hard": "🔴"}
type_short = {
    "quantitative_comparison": "QC",
    "multiple_choice": "MC",
    "multiple_choice_select_all": "MCM",
    "numeric_entry": "NE",
}
st.markdown(
    f"{diff_color.get(q['difficulty'], '')} **{type_short.get(q['type'], q['type'])}** "
    f"· {DIFFICULTY_LABELS.get(q['difficulty'], q['difficulty'])}"
)

# ── Context block ──────────────────────────────────────────────────────────────
if q.get("context"):
    st.info(q["context"])

# ── QC-specific layout ─────────────────────────────────────────────────────────
if q["type"] == "quantitative_comparison":
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("**Quantity A**")
        st.markdown(f"### {q.get('quantity_a', '')}")
    with col_b:
        st.markdown("**Quantity B**")
        st.markdown(f"### {q.get('quantity_b', '')}")
    st.markdown("---")

# ── Stem ──────────────────────────────────────────────────────────────────────
if q.get("stem"):
    st.markdown(f"**{q['stem']}**")


# ── Answer widgets ─────────────────────────────────────────────────────────────
def render_answer_widget(q, q_id, submitted):
    user_answers = st.session_state["qp_answers"].get(q_id, {})
    q_type = q["type"]
    blanks = q.get("blanks", [])

    if q_type == "quantitative_comparison":
        choices = QC_CHOICES
        prev = user_answers.get("QC")
        prev_idx = list(choices.keys()).index(prev) if prev in choices else None
        selected = st.radio(
            "정답 선택",
            options=list(choices.keys()),
            format_func=lambda k: f"{k}. {choices[k]}",
            index=prev_idx,
            key=f"{q_id}_QC",
            disabled=submitted,
        )
        user_answers["QC"] = selected

    elif q_type == "multiple_choice":
        choices = blanks[0]["choices"] if blanks else {}
        option_keys = list(choices.keys())
        prev = user_answers.get("MC")
        prev_idx = option_keys.index(prev) if prev in option_keys else None
        selected = st.radio(
            "정답 선택",
            options=option_keys,
            format_func=lambda k, c=choices: f"{k}. {c[k]}",
            index=prev_idx,
            key=f"{q_id}_MC",
            disabled=submitted,
        )
        user_answers["MC"] = selected

    elif q_type == "multiple_choice_select_all":
        choices = blanks[0]["choices"] if blanks else {}
        st.caption("해당하는 것을 모두 선택하세요.")
        selected = []
        for k, v in choices.items():
            prev_checked = k in user_answers.get("MCM", [])
            checked = st.checkbox(
                f"{k}. {v}",
                value=prev_checked,
                key=f"{q_id}_MCM_{k}",
                disabled=submitted,
            )
            if checked:
                selected.append(k)
        user_answers["MCM"] = selected

    elif q_type == "numeric_entry":
        label = blanks[0].get("label", "Answer") if blanks else "Answer"
        prev_val = user_answers.get("NE", "")
        value = st.text_input(
            label,
            value=prev_val,
            placeholder="숫자를 입력하세요",
            key=f"{q_id}_NE",
            disabled=submitted,
        )
        user_answers["NE"] = value.strip()

    st.session_state["qp_answers"][q_id] = user_answers
    return user_answers


user_answers = render_answer_widget(q, q_id, submitted)


def get_user_answer_list(q, user_answers):
    q_type = q["type"]
    if q_type == "quantitative_comparison":
        ans = user_answers.get("QC")
        return [ans] if ans else []
    elif q_type == "multiple_choice":
        ans = user_answers.get("MC")
        return [ans] if ans else []
    elif q_type == "multiple_choice_select_all":
        return sorted(user_answers.get("MCM", []))
    elif q_type == "numeric_entry":
        ans = user_answers.get("NE", "").strip()
        return [ans] if ans else []
    return []


def check_correct(q, user_list):
    correct = q.get("correct", [])
    if q["type"] == "numeric_entry":
        try:
            user_val = float(user_list[0]) if user_list else None
            correct_val = float(correct[0]) if correct else None
            if user_val is None or correct_val is None:
                return False
            return abs(user_val - correct_val) < 0.005
        except ValueError:
            return user_list == correct
    return sorted(user_list) == sorted(correct)


# ── Submit / Next ──────────────────────────────────────────────────────────────
col1, col2 = st.columns([1, 1])

with col1:
    if not submitted:
        if st.button("제출 (Submit)", type="primary", use_container_width=True):
            user_list = get_user_answer_list(q, user_answers)
            if not user_list or (len(user_list) == 1 and not user_list[0]):
                st.warning("답을 선택하거나 입력하세요.")
            else:
                st.session_state["qp_submitted"][q_id] = True
                if check_correct(q, user_list):
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
    user_list = get_user_answer_list(q, user_answers)
    is_correct = check_correct(q, user_list)
    correct = q.get("correct", [])

    if is_correct:
        st.success(f"✅ 정답! 정답: **{', '.join(correct)}**")
    else:
        q_type = q["type"]
        if q_type == "quantitative_comparison":
            correct_labels = [f"**{k}. {QC_CHOICES.get(k, '')}**" for k in correct]
        elif q_type in ("multiple_choice", "multiple_choice_select_all"):
            blanks = q.get("blanks", [])
            choices = blanks[0]["choices"] if blanks else {}
            correct_labels = [f"**{k}. {choices.get(k, '')}**" for k in correct]
        else:
            correct_labels = [f"**{k}**" for k in correct]

        st.error(f"❌ 오답. 정답: {', '.join(correct_labels)}")

    with st.expander("해설 보기 (Explanation)"):
        st.write(q.get("explanation", "해설이 없습니다."))
