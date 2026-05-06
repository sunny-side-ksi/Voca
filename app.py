"""GRE Voca — Vocabulary Quiz"""
import json
import random
import re
from pathlib import Path

import streamlit as st

from utils import inject_css, esc

st.set_page_config(page_title="Voca", page_icon="📚", layout="centered")
inject_css()

DATA_FILE = Path(__file__).parent / "voca_data.json"


# ── Data helpers ───────────────────────────────────────────────────────────────
@st.cache_data(ttl=120)
def load_data():
    if not DATA_FILE.exists():
        return {}
    with open(DATA_FILE, encoding="utf-8") as f:
        return json.load(f)


def get_words_for_days(data, days):
    words = []
    for d in days:
        for e in data.get(str(d), []):
            if e.get("word") and (e.get("korean") or e.get("definition")):
                words.append(e)
    return words


def best_meaning(entry):
    k = entry.get("korean", "").strip()
    d = entry.get("definition", "").strip()
    if k and len(k) >= 2:
        m = re.match(r'^([\d\.\s가-힣\(\),;\-\/\'~～·]+)', k)
        if m and len(m.group(1).strip()) >= 2:
            return m.group(1).strip()[:120]
        return k[:120]
    return d[:120] if d else "—"


# ── Quiz generators ────────────────────────────────────────────────────────────
def make_ox_questions(words, n):
    pool = random.sample(words, min(n, len(words)))
    qs = []
    for entry in pool:
        is_correct = random.random() > 0.45
        if is_correct or len(words) < 2:
            qs.append({"type": "ox", "word": entry["word"],
                        "meaning": best_meaning(entry),
                        "pronunciation": entry.get("pronunciation", ""),
                        "answer": True, "correct_meaning": best_meaning(entry)})
        else:
            distractor = random.choice([w for w in words if w["word"] != entry["word"]])
            qs.append({"type": "ox", "word": entry["word"],
                        "meaning": best_meaning(distractor),
                        "pronunciation": entry.get("pronunciation", ""),
                        "answer": False, "correct_meaning": best_meaning(entry)})
    return qs


def make_choice_questions(words, n, mode):
    pool = random.sample(words, min(n, len(words)))
    qs = []
    for entry in pool:
        distractors = random.sample(
            [w for w in words if w["word"] != entry["word"]],
            min(3, len(words) - 1)
        )
        if mode == "meaning":
            choices = [best_meaning(entry)] + [best_meaning(d) for d in distractors]
            random.shuffle(choices)
            qs.append({"type": "choice_meaning", "word": entry["word"],
                        "pronunciation": entry.get("pronunciation", ""),
                        "choices": choices, "answer": best_meaning(entry)})
        else:
            choices = [entry["word"]] + [d["word"] for d in distractors]
            random.shuffle(choices)
            qs.append({"type": "choice_word", "meaning": best_meaning(entry),
                        "choices": choices, "answer": entry["word"]})
    return qs


def make_match_rounds(words, total_q):
    PAIRS = 6
    rounds = []
    shuffled = words[:]
    random.shuffle(shuffled)
    for i in range(0, min(total_q * PAIRS, len(shuffled)), PAIRS):
        batch = shuffled[i:i + PAIRS]
        if len(batch) < 2:
            break
        left = [e["word"] for e in batch]
        right = [best_meaning(e) for e in batch]
        pairs = dict(zip(left, right))
        right_shuffled = right[:]
        random.shuffle(right_shuffled)
        rounds.append({"type": "match", "left": left,
                        "right": right_shuffled, "pairs": pairs})
    return rounds


# ── Session state ──────────────────────────────────────────────────────────────
def init_state():
    defaults = {
        "quiz_started": False, "quiz_type": "ox", "selected_days": [],
        "questions": [], "current_idx": 0, "score": 0, "answers": [],
        "show_result": False, "answered": False, "last_correct": None,
        "match_selected_side": None, "match_selected_idx": None,
        "match_user_pairs": {}, "match_submitted": False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


init_state()

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 📚 Voca")
    st.markdown('<hr class="sdiv">', unsafe_allow_html=True)

    data = load_data()
    available_days = sorted(int(k) for k in data.keys() if data[k])

    if not available_days:
        st.warning("단어 데이터가 없습니다.")
        st.stop()

    selected_days = st.multiselect(
        "Day 선택 (최대 3개)",
        options=available_days,
        default=st.session_state.selected_days or [available_days[0]],
        max_selections=3,
        format_func=lambda d: f"Day {d}",
    )

    quiz_type = st.radio(
        "퀴즈 유형",
        options=["ox", "meaning", "word", "match"],
        format_func=lambda x: {
            "ox": "⭕❌  OX 퀴즈",
            "meaning": "🔤  단어 → 뜻",
            "word": "💡  뜻 → 단어",
            "match": "🔗  짝 맞추기",
        }[x],
        index=["ox", "meaning", "word", "match"].index(st.session_state.quiz_type),
    )

    words_available = len(get_words_for_days(data, selected_days))
    max_q = min(50, words_available) if quiz_type != "match" else min(10, words_available // 6)
    max_q = max(max_q, 1)
    n_questions = st.slider("문제 수", min_value=5, max_value=max_q, value=min(20, max_q))

    st.markdown('<hr class="sdiv">', unsafe_allow_html=True)
    if st.button("🚀  퀴즈 시작", use_container_width=True, type="primary"):
        words = get_words_for_days(data, selected_days)
        random.shuffle(words)
        if quiz_type == "ox":
            questions = make_ox_questions(words, n_questions)
        elif quiz_type == "meaning":
            questions = make_choice_questions(words, n_questions, "meaning")
        elif quiz_type == "word":
            questions = make_choice_questions(words, n_questions, "word")
        else:
            questions = make_match_rounds(words, n_questions)
        st.session_state.update({
            "quiz_started": True, "quiz_type": quiz_type,
            "selected_days": selected_days, "questions": questions,
            "current_idx": 0, "score": 0, "answers": [],
            "show_result": False, "answered": False, "last_correct": None,
            "match_selected_side": None, "match_selected_idx": None,
            "match_user_pairs": {}, "match_submitted": False,
        })
        st.rerun()

# ── Guard ──────────────────────────────────────────────────────────────────────
if not st.session_state.quiz_started:
    st.markdown("""
    <div style="text-align:center; padding: 60px 20px;">
      <div style="font-size:4rem;">📚</div>
      <h2 style="color:#1E293B; margin-top:12px;">GRE Vocabulary Quiz</h2>
      <p style="color:#64748B; font-size:1rem;">사이드바에서 Day와 유형을 선택하고<br><strong>퀴즈 시작</strong>을 눌러보세요.</p>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

questions = st.session_state.questions
idx = st.session_state.current_idx
total = len(questions)


# ── Result screen ──────────────────────────────────────────────────────────────
if idx >= total or st.session_state.show_result:
    score = st.session_state.score
    pct = int(score / total * 100) if total > 0 else 0
    wrong_count = total - score

    if pct == 100:
        msg = "완벽해요! 🎉"
    elif pct >= 80:
        msg = "훌륭합니다!"
    elif pct >= 60:
        msg = "잘 하셨어요!"
    else:
        msg = "다시 도전해보세요"

    st.markdown(f"""
    <div class="result-hero">
        <div class="rh-pct">{pct}%</div>
        <div class="rh-score">{score} / {total} 정답</div>
        <div class="rh-msg">{msg}</div>
    </div>
    <div class="stat-row">
        <div class="stat-box"><div class="stat-val">{score}</div><div class="stat-lbl">정답</div></div>
        <div class="stat-box"><div class="stat-val">{wrong_count}</div><div class="stat-lbl">오답</div></div>
        <div class="stat-box"><div class="stat-val">{total}</div><div class="stat-lbl">전체</div></div>
    </div>
    """, unsafe_allow_html=True)

    wrongs = [a for a in st.session_state.answers if not a["correct"]]
    if wrongs:
        items_html = "".join(
            f'<div class="wrong-item">'
            f'<span class="wi-word">{esc(a.get("word", a.get("meaning", "")))}</span>'
            f'<span class="wi-sep">→</span>'
            f'<span class="wi-ans">{esc(a.get("correct_meaning", ""))}</span>'
            f'</div>'
            for a in wrongs
        )
        st.markdown(
            f'<div class="wrong-list">'
            f'<div class="wrong-hdr">오답 목록 ({len(wrongs)}개)</div>'
            f'{items_html}</div>',
            unsafe_allow_html=True,
        )
    else:
        st.success("모두 맞혔습니다! 🎉")

    st.markdown('<hr class="sdiv">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄  다시 풀기", use_container_width=True, type="primary"):
            words = get_words_for_days(data, st.session_state.selected_days)
            qt = st.session_state.quiz_type
            if qt == "ox":
                qs = make_ox_questions(words, total)
            elif qt == "meaning":
                qs = make_choice_questions(words, total, "meaning")
            elif qt == "word":
                qs = make_choice_questions(words, total, "word")
            else:
                qs = make_match_rounds(words, total)
            st.session_state.update({
                "questions": qs, "current_idx": 0, "score": 0,
                "answers": [], "show_result": False, "answered": False,
                "last_correct": None, "match_user_pairs": {}, "match_submitted": False,
            })
            st.rerun()
    with col2:
        if st.button("← 처음으로", use_container_width=True):
            st.session_state.quiz_started = False
            st.rerun()
    st.stop()


# ── Progress ───────────────────────────────────────────────────────────────────
st.progress(idx / total)
st.caption(f"문제 {idx + 1} / {total}   ·   현재 점수 {st.session_state.score}점")

q = questions[idx]


# ══════════════════════════════════════════════════════════════════════════════
# OX QUIZ
# ══════════════════════════════════════════════════════════════════════════════
if q["type"] == "ox":
    pron = q.get("pronunciation", "")
    pron_html = f'<div class="wh-pron">[{esc(pron)}]</div>' if pron else ""
    st.markdown(
        f'<div class="word-hero"><div class="wh-word">{esc(q["word"])}</div>{pron_html}</div>',
        unsafe_allow_html=True,
    )
    st.markdown(f'<div class="meaning-box">{esc(q["meaning"])}</div>', unsafe_allow_html=True)
    st.markdown('<div class="quiz-tip">위의 뜻이 이 단어와 맞으면 ⭕, 틀리면 ❌</div>', unsafe_allow_html=True)

    if not st.session_state.answered:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⭕  맞아요", use_container_width=True, type="primary"):
                correct = q["answer"] is True
                st.session_state.answered = True
                st.session_state.last_correct = correct
                if correct:
                    st.session_state.score += 1
                st.session_state.answers.append({
                    "word": q["word"], "answer": "O" if q["answer"] else "X",
                    "user_answer": "O", "correct": correct,
                    "correct_meaning": q["correct_meaning"],
                })
                st.rerun()
        with col2:
            if st.button("❌  틀려요", use_container_width=True):
                correct = q["answer"] is False
                st.session_state.answered = True
                st.session_state.last_correct = correct
                if correct:
                    st.session_state.score += 1
                st.session_state.answers.append({
                    "word": q["word"], "answer": "O" if q["answer"] else "X",
                    "user_answer": "X", "correct": correct,
                    "correct_meaning": q["correct_meaning"],
                })
                st.rerun()
    else:
        if st.session_state.last_correct:
            detail = f'<div class="fb-detail">정답: {"⭕" if q["answer"] else "❌"}</div>'
            st.markdown(f'<div class="fb-correct">✅ 정답!{detail}</div>', unsafe_allow_html=True)
        else:
            detail = f'<div class="fb-detail">정답: {"⭕" if q["answer"] else "❌"}</div>'
            st.markdown(
                f'<div class="fb-wrong">❌ 오답{detail}</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                f'<div class="answer-card">'
                f'<span class="ac-label">정답</span>'
                f'<span class="ac-word">{esc(q["word"])}</span>'
                f'<span class="ac-sep">—</span>'
                f'<span class="ac-meaning">{esc(q["correct_meaning"])}</span>'
                f'</div>',
                unsafe_allow_html=True,
            )
        if st.button("다음 →", use_container_width=True, type="primary"):
            st.session_state.current_idx += 1
            st.session_state.answered = False
            st.session_state.last_correct = None
            if st.session_state.current_idx >= total:
                st.session_state.show_result = True
            st.rerun()


# ══════════════════════════════════════════════════════════════════════════════
# 단어 → 뜻
# ══════════════════════════════════════════════════════════════════════════════
elif q["type"] == "choice_meaning":
    pron = q.get("pronunciation", "")
    pron_html = f'<div class="wh-pron">[{esc(pron)}]</div>' if pron else ""
    st.markdown(
        f'<div class="word-hero"><div class="wh-word">{esc(q["word"])}</div>{pron_html}</div>',
        unsafe_allow_html=True,
    )
    st.markdown('<div class="quiz-tip">이 단어의 뜻은?</div>', unsafe_allow_html=True)

    NUMS = ["①", "②", "③", "④"]
    for i, choice in enumerate(q["choices"]):
        label = f"{NUMS[i]}  {choice}"
        if st.session_state.answered:
            if choice == q["answer"]:
                st.success(label)
            elif choice == st.session_state.get("user_choice"):
                st.error(label)
            else:
                st.write(label)
        else:
            if st.button(label, use_container_width=True, key=f"cm_{i}"):
                correct = (choice == q["answer"])
                st.session_state.answered = True
                st.session_state.last_correct = correct
                st.session_state["user_choice"] = choice
                if correct:
                    st.session_state.score += 1
                st.session_state.answers.append({
                    "word": q["word"], "answer": q["answer"],
                    "user_answer": choice, "correct": correct,
                    "correct_meaning": q["answer"],
                })
                st.rerun()

    if st.session_state.answered:
        if st.session_state.last_correct:
            st.markdown('<div class="fb-correct">✅ 정답!</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="fb-wrong">❌ 오답</div>', unsafe_allow_html=True)
            st.markdown(
                f'<div class="answer-card">'
                f'<span class="ac-label">정답</span>'
                f'<span class="ac-word">{esc(q["word"])}</span>'
                f'<span class="ac-sep">—</span>'
                f'<span class="ac-meaning">{esc(q["answer"])}</span>'
                f'</div>',
                unsafe_allow_html=True,
            )
        if st.button("다음 →", use_container_width=True, type="primary"):
            st.session_state.current_idx += 1
            st.session_state.answered = False
            st.session_state.last_correct = None
            st.session_state.pop("user_choice", None)
            if st.session_state.current_idx >= total:
                st.session_state.show_result = True
            st.rerun()


# ══════════════════════════════════════════════════════════════════════════════
# 뜻 → 단어
# ══════════════════════════════════════════════════════════════════════════════
elif q["type"] == "choice_word":
    st.markdown(
        f'<div class="meaning-hero"><div class="mh-text">{esc(q["meaning"])}</div></div>',
        unsafe_allow_html=True,
    )
    st.markdown('<div class="quiz-tip">이 뜻에 해당하는 단어는?</div>', unsafe_allow_html=True)

    NUMS = ["①", "②", "③", "④"]
    for i, choice in enumerate(q["choices"]):
        label = f"{NUMS[i]}  {choice}"
        if st.session_state.answered:
            if choice == q["answer"]:
                st.success(label)
            elif choice == st.session_state.get("user_choice"):
                st.error(label)
            else:
                st.write(label)
        else:
            if st.button(label, use_container_width=True, key=f"cw_{i}"):
                correct = (choice == q["answer"])
                st.session_state.answered = True
                st.session_state.last_correct = correct
                st.session_state["user_choice"] = choice
                if correct:
                    st.session_state.score += 1
                st.session_state.answers.append({
                    "meaning": q["meaning"], "answer": q["answer"],
                    "user_answer": choice, "correct": correct,
                    "correct_meaning": q["meaning"],
                })
                st.rerun()

    if st.session_state.answered:
        if st.session_state.last_correct:
            st.markdown('<div class="fb-correct">✅ 정답!</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="fb-wrong">❌ 오답</div>', unsafe_allow_html=True)
            st.markdown(
                f'<div class="answer-card">'
                f'<span class="ac-label">정답</span>'
                f'<span class="ac-word">{esc(q["answer"])}</span>'
                f'<span class="ac-sep">—</span>'
                f'<span class="ac-meaning">{esc(q["meaning"])}</span>'
                f'</div>',
                unsafe_allow_html=True,
            )
        if st.button("다음 →", use_container_width=True, type="primary"):
            st.session_state.current_idx += 1
            st.session_state.answered = False
            st.session_state.last_correct = None
            st.session_state.pop("user_choice", None)
            if st.session_state.current_idx >= total:
                st.session_state.show_result = True
            st.rerun()


# ══════════════════════════════════════════════════════════════════════════════
# 짝 맞추기
# ══════════════════════════════════════════════════════════════════════════════
elif q["type"] == "match":
    left_words = q["left"]
    right_meanings = q["right"]
    correct_pairs = q["pairs"]
    user_pairs = st.session_state.match_user_pairs
    submitted = st.session_state.match_submitted
    sel_side = st.session_state.match_selected_side
    sel_idx = st.session_state.match_selected_idx

    paired_words = set(user_pairs.keys())
    paired_meanings = set(user_pairs.values())

    col_w, col_m = st.columns(2)
    with col_w:
        st.markdown('<div class="match-hdr">단어</div>', unsafe_allow_html=True)
        for i, word in enumerate(left_words):
            is_paired = word in paired_words
            is_selected = (sel_side == "left" and sel_idx == i)
            if submitted:
                if user_pairs.get(word) == correct_pairs.get(word):
                    st.success(f"✓ {word}")
                else:
                    st.error(f"✗ {word}")
                    st.caption(f"→ {correct_pairs.get(word, '')[:55]}")
            elif is_paired:
                st.info(f"✓ {word}", icon=None)
            else:
                btn_label = f"▶ {word}" if is_selected else word
                if st.button(btn_label, key=f"left_{i}", use_container_width=True,
                             type="primary" if is_selected else "secondary"):
                    if sel_side == "left" and sel_idx == i:
                        st.session_state.match_selected_side = None
                        st.session_state.match_selected_idx = None
                    elif sel_side == "right" and sel_idx is not None:
                        st.session_state.match_user_pairs[word] = right_meanings[sel_idx]
                        st.session_state.match_selected_side = None
                        st.session_state.match_selected_idx = None
                    else:
                        st.session_state.match_selected_side = "left"
                        st.session_state.match_selected_idx = i
                    st.rerun()

    with col_m:
        st.markdown('<div class="match-hdr">뜻</div>', unsafe_allow_html=True)
        for j, meaning in enumerate(right_meanings):
            is_paired = meaning in paired_meanings
            is_selected = (sel_side == "right" and sel_idx == j)
            if submitted:
                matched_word = next((w for w, m in user_pairs.items() if m == meaning), None)
                if matched_word and correct_pairs.get(matched_word) == meaning:
                    st.success(f"✓ {meaning[:50]}")
                else:
                    actual_word = next((w for w, m in correct_pairs.items() if m == meaning), "?")
                    st.error(f"✗ {meaning[:50]}")
                    st.caption(f"→ 정답: {actual_word}")
            elif is_paired:
                st.info(f"✓ {meaning[:50]}", icon=None)
            else:
                btn_label = f"▶ {meaning[:44]}" if is_selected else meaning[:44]
                if st.button(btn_label, key=f"right_{j}", use_container_width=True,
                             type="primary" if is_selected else "secondary"):
                    if sel_side == "right" and sel_idx == j:
                        st.session_state.match_selected_side = None
                        st.session_state.match_selected_idx = None
                    elif sel_side == "left" and sel_idx is not None:
                        st.session_state.match_user_pairs[left_words[sel_idx]] = meaning
                        st.session_state.match_selected_side = None
                        st.session_state.match_selected_idx = None
                    else:
                        st.session_state.match_selected_side = "right"
                        st.session_state.match_selected_idx = j
                    st.rerun()

    st.markdown('<hr class="sdiv">', unsafe_allow_html=True)

    if not submitted:
        col1, col2 = st.columns([1, 2])
        with col1:
            if user_pairs and st.button("↩  취소", use_container_width=True):
                last_key = list(user_pairs.keys())[-1]
                del st.session_state.match_user_pairs[last_key]
                st.rerun()
        with col2:
            all_paired = len(user_pairs) == len(left_words)
            if st.button(
                "✅  채점하기" if all_paired else f"짝 맞추기 중… ({len(user_pairs)}/{len(left_words)})",
                use_container_width=True,
                type="primary" if all_paired else "secondary",
                disabled=not all_paired,
            ):
                st.session_state.match_submitted = True
                correct_count = sum(1 for w, m in user_pairs.items() if correct_pairs.get(w) == m)
                round_perfect = correct_count == len(left_words)
                st.session_state.score += 1 if round_perfect else 0
                st.session_state.answers.append({
                    "word": f"짝맞추기 라운드 {idx + 1}",
                    "answer": f"{len(left_words)}/{len(left_words)}",
                    "user_answer": f"{correct_count}/{len(left_words)}",
                    "correct": round_perfect,
                    "correct_meaning": "",
                })
                st.rerun()
    else:
        correct_count = sum(1 for w, m in user_pairs.items() if correct_pairs.get(w) == m)
        total_in_round = len(left_words)
        if correct_count == total_in_round:
            st.markdown('<div class="fb-correct">✅ 완벽! 모두 맞혔습니다 🎉</div>', unsafe_allow_html=True)
        else:
            st.markdown(
                f'<div class="fb-wrong">❌ {correct_count}/{total_in_round} 정답</div>',
                unsafe_allow_html=True,
            )
        if st.button("다음 라운드 →", use_container_width=True, type="primary"):
            st.session_state.current_idx += 1
            st.session_state.match_user_pairs = {}
            st.session_state.match_submitted = False
            st.session_state.match_selected_side = None
            st.session_state.match_selected_idx = None
            if st.session_state.current_idx >= total:
                st.session_state.show_result = True
            st.rerun()
