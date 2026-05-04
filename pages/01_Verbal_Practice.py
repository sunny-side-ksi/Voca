"""GRE Verbal Reasoning Practice — Text Completion, Sentence Equivalence, Reading Comprehension"""
import json
from pathlib import Path

import streamlit as st

st.set_page_config(page_title="GRE Verbal Practice", page_icon="📝", layout="centered")

DATA_FILE = Path(__file__).parent.parent / "gre_content" / "practice_questions.json"

DIFFICULTY_LABELS = {"easy": "Easy", "medium": "Medium", "hard": "Hard"}
TYPE_LABELS = {
    "text_completion": "Text Completion (TC)",
    "sentence_equivalence": "Sentence Equivalence (SE)",
    "reading_comprehension": "Reading Comprehension (RC)",
}


@st.cache_data
def load_questions():
    with open(DATA_FILE, encoding="utf-8") as f:
        data = json.load(f)
    return data.get("verbal", [])


def reset_session():
    for key in list(st.session_state.keys()):
        if key.startswith("vp_"):
            del st.session_state[key]


# ── Init ───────────────────────────────────────────────────────────────────────
all_questions = load_questions()

st.title("📝 Verbal Reasoning Practice")

# ── Sidebar filters ────────────────────────────────────────────────────────────
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
        options=["text_completion", "sentence_equivalence", "reading_comprehension"],
        default=["text_completion", "sentence_equivalence", "reading_comprehension"],
        format_func=lambda x: TYPE_LABELS[x],
    )

    if st.button("Start / Restart", type="primary", use_container_width=True):
        reset_session()
        filtered = [
            q for q in all_questions
            if q["difficulty"] in selected_difficulties and q["type"] in selected_types
        ]
        st.session_state["vp_questions"] = filtered
        st.session_state["vp_idx"] = 0
        st.session_state["vp_answers"] = {}
        st.session_state["vp_submitted"] = {}
        st.session_state["vp_score"] = 0
        st.session_state["vp_done"] = False
        st.rerun()

    st.divider()
    st.caption("TC: 빈칸 완성 | SE: 문장 등가 | RC: 독해")

# ── Guard: quiz not started ────────────────────────────────────────────────────
if "vp_questions" not in st.session_state:
    st.info("사이드바에서 난이도·유형을 선택하고 **Start**를 눌러 시작하세요.")
    st.stop()

questions = st.session_state["vp_questions"]
if not questions:
    st.warning("선택한 조건에 해당하는 문제가 없습니다. 필터를 조정하세요.")
    st.stop()

idx = st.session_state["vp_idx"]
total = len(questions)

# ── Done screen ────────────────────────────────────────────────────────────────
if st.session_state.get("vp_done"):
    score = st.session_state["vp_score"]
    st.success(f"## 완료! 점수: {score} / {total}")
    pct = round(score / total * 100)
    st.progress(score / total)
    st.write(f"정답률 **{pct}%**")

    if st.button("다시 풀기", use_container_width=True):
        reset_session()
        st.rerun()
    st.stop()

# ── Progress bar ───────────────────────────────────────────────────────────────
st.progress((idx) / total)
st.caption(f"문제 {idx + 1} / {total}")

q = questions[idx]
q_id = q["id"]
submitted = st.session_state["vp_submitted"].get(q_id, False)

# ── Question header badge ──────────────────────────────────────────────────────
diff_color = {"easy": "🟢", "medium": "🟡", "hard": "🔴"}
type_short = {"text_completion": "TC", "sentence_equivalence": "SE", "reading_comprehension": "RC"}
st.markdown(
    f"{diff_color.get(q['difficulty'], '')} **{type_short.get(q['type'], q['type'])}** "
    f"· {DIFFICULTY_LABELS.get(q['difficulty'], q['difficulty'])}"
)

# ── Passage (RC) ───────────────────────────────────────────────────────────────
if q.get("passage"):
    with st.expander("지문 보기 (Passage)", expanded=True):
        st.markdown(q["passage"])
    st.markdown("---")

# ── Stem ──────────────────────────────────────────────────────────────────────
st.markdown(f"**{q['stem']}**" if q.get("stem") else "")


# ── Answer widgets by type ─────────────────────────────────────────────────────

def render_answer_widget(q, q_id, submitted):
    """Render the appropriate answer widget and return user answer dict or list."""
    q_type = q["type"]
    blanks = q.get("blanks", [])
    user_answers = st.session_state["vp_answers"].get(q_id, {})

    if q_type == "text_completion":
        for blank in blanks:
            label = blank.get("label") or "Blank"
            choices = blank["choices"]
            option_keys = list(choices.keys())
            option_labels = [f"{k}. {v}" for k, v in choices.items()]
            prev = user_answers.get(label)
            prev_idx = option_keys.index(prev) if prev in option_keys else None

            selected = st.radio(
                label,
                options=option_keys,
                format_func=lambda k, c=choices: f"{k}. {c[k]}",
                index=prev_idx,
                key=f"{q_id}_{label}",
                disabled=submitted,
                horizontal=len(option_keys) <= 3,
            )
            user_answers[label] = selected

    elif q_type == "sentence_equivalence":
        choices = blanks[0]["choices"] if blanks else {}
        st.caption("정답 2개를 선택하세요.")
        selected = []
        for k, v in choices.items():
            prev_checked = k in user_answers.get("SE", [])
            checked = st.checkbox(
                f"{k}. {v}",
                value=prev_checked,
                key=f"{q_id}_SE_{k}",
                disabled=submitted,
            )
            if checked:
                selected.append(k)
        user_answers["SE"] = selected

    elif q_type == "reading_comprehension":
        subtype = q.get("subtype", "single_answer")
        choices = blanks[0]["choices"] if blanks else {}

        if subtype == "multi_answer":
            st.caption("해당하는 것을 모두 선택하세요.")
            selected = []
            for k, v in choices.items():
                prev_checked = k in user_answers.get("RC", [])
                checked = st.checkbox(
                    f"{k}. {v}",
                    value=prev_checked,
                    key=f"{q_id}_RC_{k}",
                    disabled=submitted,
                )
                if checked:
                    selected.append(k)
            user_answers["RC"] = selected
        else:
            option_keys = list(choices.keys())
            prev = user_answers.get("RC_single")
            prev_idx = option_keys.index(prev) if prev in option_keys else None
            selected = st.radio(
                "정답 선택",
                options=option_keys,
                format_func=lambda k, c=choices: f"{k}. {c[k]}",
                index=prev_idx,
                key=f"{q_id}_RC_single",
                disabled=submitted,
            )
            user_answers["RC_single"] = selected

    st.session_state["vp_answers"][q_id] = user_answers
    return user_answers


user_answers = render_answer_widget(q, q_id, submitted)


def get_user_answer_list(q, user_answers):
    """Convert user_answers dict to sorted list of selected keys."""
    q_type = q["type"]
    if q_type == "text_completion":
        blanks = q.get("blanks", [])
        result = []
        for blank in blanks:
            label = blank.get("label") or "Blank"
            ans = user_answers.get(label)
            if ans:
                result.append(ans)
        return result
    elif q_type == "sentence_equivalence":
        return sorted(user_answers.get("SE", []))
    elif q_type == "reading_comprehension":
        subtype = q.get("subtype", "single_answer")
        if subtype == "multi_answer":
            return sorted(user_answers.get("RC", []))
        else:
            ans = user_answers.get("RC_single")
            return [ans] if ans else []
    return []


def check_correct(q, user_list):
    correct = sorted(q.get("correct", []))
    return sorted(user_list) == correct


# ── Submit / Next buttons ──────────────────────────────────────────────────────
col1, col2 = st.columns([1, 1])

with col1:
    if not submitted:
        if st.button("제출 (Submit)", type="primary", use_container_width=True):
            user_list = get_user_answer_list(q, user_answers)
            if not user_list or any(a is None for a in user_list):
                st.warning("모든 빈칸을 선택하세요.")
            else:
                st.session_state["vp_submitted"][q_id] = True
                if check_correct(q, user_list):
                    st.session_state["vp_score"] += 1
                st.rerun()

with col2:
    if submitted:
        label = "다음 문제 →" if idx + 1 < total else "결과 보기"
        if st.button(label, type="primary", use_container_width=True):
            if idx + 1 < total:
                st.session_state["vp_idx"] += 1
            else:
                st.session_state["vp_done"] = True
            st.rerun()

# ── Feedback ───────────────────────────────────────────────────────────────────
if submitted:
    user_list = get_user_answer_list(q, user_answers)
    is_correct = check_correct(q, user_list)
    correct_keys = q.get("correct", [])

    if is_correct:
        st.success(f"✅ 정답! 정답: **{', '.join(correct_keys)}**")
    else:
        blanks = q.get("blanks", [])
        correct_labels = []
        for i, key in enumerate(correct_keys):
            if i < len(blanks):
                blank = blanks[i]
                choices = blank.get("choices", {})
                val = choices.get(key, "")
                correct_labels.append(f"**{key}. {val}**")
            else:
                correct_labels.append(f"**{key}**")
        st.error(f"❌ 오답. 정답: {', '.join(correct_labels)}")

    with st.expander("해설 보기 (Explanation)"):
        st.write(q.get("explanation", "해설이 없습니다."))
