"""GRE Vocabulary Quiz — Streamlit App"""
import json
import random
import re
from datetime import date, datetime
from pathlib import Path

import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="GRE Voca Quiz",
    page_icon="📚",
    layout="centered",
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* Quiz card */
.quiz-card {
    background: #f8f9fa;
    border-radius: 16px;
    padding: 2rem 2.5rem;
    margin: 1rem 0;
    border: 2px solid #e9ecef;
    text-align: center;
}
.quiz-word {
    font-size: 2.4rem;
    font-weight: 700;
    color: #1a1a2e;
    letter-spacing: 1px;
    margin-bottom: 0.3rem;
}
.quiz-pronunciation {
    font-size: 1rem;
    color: #6c757d;
    margin-bottom: 1rem;
}
.quiz-meaning-display {
    font-size: 1.25rem;
    color: #2c3e50;
    margin-top: 0.5rem;
}
/* Progress */
.progress-text {
    font-size: 0.9rem;
    color: #6c757d;
    margin-bottom: 0.5rem;
}
/* Score badge */
.score-badge {
    display: inline-block;
    background: #4CAF50;
    color: white;
    padding: 4px 14px;
    border-radius: 20px;
    font-weight: 600;
}
/* Result cards */
.result-correct {
    border-left: 5px solid #4CAF50;
    background: #f0fff0;
    padding: 10px 16px;
    border-radius: 8px;
    margin: 6px 0;
}
.result-wrong {
    border-left: 5px solid #f44336;
    background: #fff0f0;
    padding: 10px 16px;
    border-radius: 8px;
    margin: 6px 0;
}
/* Match table */
.match-row {
    display: flex;
    gap: 12px;
    margin-bottom: 8px;
    align-items: center;
}
.match-cell {
    flex: 1;
    padding: 10px 14px;
    border-radius: 10px;
    border: 2px solid #dee2e6;
    cursor: pointer;
    font-size: 1rem;
    transition: all 0.2s;
}
.match-cell-selected {
    border-color: #4361ee;
    background: #eef2ff;
    font-weight: 600;
}
.match-cell-matched {
    border-color: #4CAF50;
    background: #f0fff0;
    font-weight: 600;
}
/* OX buttons */
div[data-testid="column"] button {
    width: 100%;
    height: 80px;
    font-size: 2rem;
    font-weight: 700;
}
/* Sidebar */
section[data-testid="stSidebar"] {
    background: #1a1a2e;
}
section[data-testid="stSidebar"] * {
    color: #e0e0e0 !important;
}
section[data-testid="stSidebar"] .stSelectbox label,
section[data-testid="stSidebar"] .stMultiSelect label,
section[data-testid="stSidebar"] .stRadio label,
section[data-testid="stSidebar"] .stSlider label {
    color: #adb5bd !important;
}
</style>
""", unsafe_allow_html=True)

# ── Data loading ──────────────────────────────────────────────────────────────
DATA_FILE = Path(__file__).parent / "voca_data.json"


@st.cache_data(ttl=120)
def load_data() -> dict[str, list[dict]]:
    if not DATA_FILE.exists():
        return {}
    with open(DATA_FILE, encoding="utf-8") as f:
        return json.load(f)


def get_words_for_days(data: dict, days: list[int]) -> list[dict]:
    words = []
    for d in days:
        entries = data.get(str(d), [])
        # Only include entries that have at least a word and some meaning
        for e in entries:
            if e.get("word") and (e.get("korean") or e.get("definition")):
                words.append(e)
    return words


def best_meaning(entry: dict) -> str:
    """Return the most readable Korean meaning, falling back to English definition."""
    k = entry.get("korean", "").strip()
    d = entry.get("definition", "").strip()
    if k and len(k) >= 2:
        # Extract just the Korean portion (strip trailing English definitions)
        # Pattern: Korean + Korean punctuation, stop before pure English sentence
        m = re.match(r'^([\d\.\s가-힣\(\),;\-\/\'~～·]+)', k)
        if m and len(m.group(1).strip()) >= 2:
            return m.group(1).strip()[:120]
        return k[:120]
    return d[:120] if d else "—"


# ── Obsidian wrong-word tracking ─────────────────────────────────────────────

def add_to_daily_wrong(word: str, meaning: str):
    timestamp = datetime.now().strftime("%H:%M")
    existing = {e["word"] for e in st.session_state.daily_wrong_words}
    if word not in existing:
        st.session_state.daily_wrong_words.append({
            "word": word,
            "meaning": meaning,
            "time": timestamp,
        })


def render_obsidian_export(wrong_words: list):
    today = date.today().strftime("%Y-%m-%d")
    filename = f"{today}_오답노트.md"

    if not wrong_words:
        st.button("📥 오답 노트 다운로드", disabled=True, use_container_width=True)
        st.caption("아직 틀린 단어가 없습니다.")
        return

    lines = [f"### 퀴즈 오답 기록 ({today})\n"]
    for e in wrong_words:
        lines.append(f"- [{e['time']}] **{e['word']}** — {e['meaning']}")
    content = "\n".join(lines)

    st.download_button(
        label=f"📥 오답 노트 다운로드 ({len(wrong_words)}개)",
        data=content.encode("utf-8"),
        file_name=filename,
        mime="text/markdown",
        use_container_width=True,
        type="primary",
    )
    st.caption(f"다운로드 후 옵시디언 볼트 폴더에 넣으세요. (`{filename}`)")


# ── GitHub sync for Obsidian ──────────────────────────────────────────────────
# 환경 설정 안내:
#   1) requirements.txt에 추가: PyGithub>=1.59.0
#   2) Streamlit Cloud 앱 대시보드 → Settings → Secrets 에 아래 형식으로 입력:
#        GITHUB_TOKEN = "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
#        GITHUB_REPO  = "sunny-side-ksi/Voca"   # 선택사항 — 생략하면 기본값 사용
#   저장 경로: 04.English/GRE/Voca/YYYY-MM-DD_오답노트.md

def push_to_github(wrong_words: list):
    """오답 목록을 GitHub wrong_notes/ 폴더에 마크다운 파일로 Push (없으면 생성, 있으면 Append)."""
    from github import Github, GithubException  # PyGithub

    try:
        token = st.secrets["GITHUB_TOKEN"]
    except KeyError:
        st.error("GITHUB_TOKEN이 Streamlit Cloud Secrets에 설정되지 않았습니다.")
        return

    repo_name = st.secrets.get("GITHUB_REPO", "sunny-side-ksi/Voca")
    today = date.today().strftime("%Y-%m-%d")
    now = datetime.now().strftime("%H:%M")
    file_path = f"04.English/GRE/Voca/{today}_오답노트.md"

    lines = [f"\n## 퀴즈 오답 기록 ({now})\n"]
    for e in wrong_words:
        lines.append(f"- [{e['time']}] **{e['word']}** — {e['meaning']}")
    new_block = "\n".join(lines)

    g = Github(token)
    repo = g.get_repo(repo_name)

    try:
        existing = repo.get_contents(file_path)
        old_content = existing.decoded_content.decode("utf-8")
        repo.update_file(
            path=file_path,
            message=f"오답노트 업데이트: {today} {now}",
            content=old_content + new_block,
            sha=existing.sha,
        )
    except GithubException as exc:
        if exc.status == 404:
            repo.create_file(
                path=file_path,
                message=f"오답노트 생성: {today} {now}",
                content=f"# {today} 오답노트" + new_block,
            )
        else:
            raise


# ── Quiz generators ───────────────────────────────────────────────────────────

def make_ox_questions(words: list[dict], n: int) -> list[dict]:
    pool = random.sample(words, min(n, len(words)))
    qs = []
    for entry in pool:
        is_correct = random.random() > 0.45
        if is_correct or len(words) < 2:
            qs.append({
                "type": "ox",
                "word": entry["word"],
                "meaning": best_meaning(entry),
                "pronunciation": entry.get("pronunciation", ""),
                "answer": True,
                "correct_meaning": best_meaning(entry),
                "entry": entry,
            })
        else:
            distractor = random.choice([w for w in words if w["word"] != entry["word"]])
            qs.append({
                "type": "ox",
                "word": entry["word"],
                "meaning": best_meaning(distractor),
                "pronunciation": entry.get("pronunciation", ""),
                "answer": False,
                "correct_meaning": best_meaning(entry),
                "entry": entry,
            })
    return qs


def make_choice_questions(words: list[dict], n: int, mode: str) -> list[dict]:
    """mode: 'meaning' → show word, choose meaning | 'word' → show meaning, choose word"""
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
            qs.append({
                "type": "choice_meaning",
                "word": entry["word"],
                "pronunciation": entry.get("pronunciation", ""),
                "choices": choices,
                "answer": best_meaning(entry),
                "entry": entry,
            })
        else:  # 'word'
            choices = [entry["word"]] + [d["word"] for d in distractors]
            random.shuffle(choices)
            qs.append({
                "type": "choice_word",
                "meaning": best_meaning(entry),
                "choices": choices,
                "answer": entry["word"],
                "entry": entry,
            })
    return qs


def make_match_rounds(words: list[dict], total_q: int) -> list[dict]:
    """Each 'question' is a round of 6 pairs."""
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
        pairs = dict(zip(left, right))  # correct mapping
        right_shuffled = right[:]
        random.shuffle(right_shuffled)
        rounds.append({
            "type": "match",
            "left": left,            # ordered words
            "right": right_shuffled, # shuffled meanings
            "pairs": pairs,          # word → correct meaning
        })
    return rounds


# ── Session state initializer ─────────────────────────────────────────────────

def init_state():
    defaults = {
        "quiz_started": False,
        "quiz_type": "ox",
        "selected_days": [],
        "questions": [],
        "current_idx": 0,
        "score": 0,
        "answers": [],
        "show_result": False,
        # OX / choice
        "answered": False,
        "last_correct": None,
        # Match
        "match_selected_side": None,  # 'left' or 'right'
        "match_selected_idx": None,
        "match_user_pairs": {},       # word → meaning (user's pairs)
        "match_submitted": False,
        # Obsidian export
        "daily_wrong_words": [],
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


init_state()

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.title("📚 GRE Voca Quiz")
    st.markdown("---")

    data = load_data()
    available_days = sorted(int(k) for k in data.keys() if data[k])

    if not available_days:
        st.warning("단어 데이터가 없습니다.\n\n`parse_voca.py`를 먼저 실행하세요.")
        st.code("python parse_voca.py", language="bash")
        st.stop()

    st.markdown("**Day 선택** (최대 3개)")
    selected_days = st.multiselect(
        label="Day",
        options=available_days,
        default=st.session_state.selected_days or [available_days[0]],
        max_selections=3,
        format_func=lambda d: f"Day {d}",
        label_visibility="collapsed",
    )

    if len(selected_days) > 3:
        st.warning("최대 3개까지 선택 가능합니다.")
        selected_days = selected_days[:3]

    st.markdown("---")
    st.markdown("**퀴즈 유형**")
    quiz_type = st.radio(
        label="quiz_type",
        options=["ox", "meaning", "word", "match"],
        format_func=lambda x: {
            "ox": "⭕❌  OX 퀴즈",
            "meaning": "🔤→🇰🇷  단어 뜻 맞추기",
            "word": "🇰🇷→🔤  단어 맞추기",
            "match": "🔗  짝 맞추기",
        }[x],
        index=["ox", "meaning", "word", "match"].index(st.session_state.quiz_type),
        label_visibility="collapsed",
    )

    st.markdown("---")
    words_available = len(get_words_for_days(data, selected_days))
    max_q = min(50, words_available) if quiz_type != "match" else min(10, words_available // 6)
    max_q = max(max_q, 1)

    n_questions = st.slider("문제 수", min_value=5, max_value=max_q, value=min(20, max_q))

    st.markdown("---")
    if st.button("🚀 퀴즈 시작", use_container_width=True, type="primary"):
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
            "quiz_started": True,
            "quiz_type": quiz_type,
            "selected_days": selected_days,
            "questions": questions,
            "current_idx": 0,
            "score": 0,
            "answers": [],
            "show_result": False,
            "answered": False,
            "last_correct": None,
            "match_selected_side": None,
            "match_selected_idx": None,
            "match_user_pairs": {},
            "match_submitted": False,
        })
        st.rerun()

    if st.session_state.quiz_started:
        st.markdown("---")
        total = len(st.session_state.questions)
        done = st.session_state.current_idx
        score = st.session_state.score
        pct = int(score / max(done, 1) * 100) if done > 0 else 0
        st.metric("현재 점수", f"{score}/{done}", f"{pct}%")

        if st.button("🔄 초기화", use_container_width=True):
            st.session_state.quiz_started = False
            st.rerun()

    st.markdown("---")
    n_wrong = len(st.session_state.daily_wrong_words)
    st.caption(f"📝 오늘 누적 오답: **{n_wrong}**개 | 내보내기는 결과 화면에서")

    if st.button("☁️ 오답 노트를 깃허브로 전송", use_container_width=True):
        if n_wrong == 0:
            st.warning("아직 오답이 없습니다.")
        else:
            with st.spinner("GitHub에 업로드 중..."):
                try:
                    push_to_github(st.session_state.daily_wrong_words)
                    st.success("GitHub 전송 완료! 옵시디언에서 Pull 하세요.")
                except Exception as exc:
                    st.error(f"전송 실패: {exc}")


# ── Main area ─────────────────────────────────────────────────────────────────

if not st.session_state.quiz_started:
    # Welcome screen
    st.markdown("""
    <div style='text-align:center; padding: 3rem 1rem;'>
        <div style='font-size:4rem;'>📚</div>
        <h1 style='font-size:2.5rem; font-weight:800; color:#1a1a2e;'>GRE Voca Quiz</h1>
        <p style='font-size:1.1rem; color:#6c757d;'>
            왼쪽 사이드바에서 Day를 선택하고 퀴즈를 시작하세요.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if available_days:
        st.markdown("### 📊 단어 현황")
        cols = st.columns(5)
        for i, d in enumerate(available_days):
            cnt = len(data.get(str(d), []))
            cols[i % 5].metric(f"Day {d}", f"{cnt}단어")
    st.stop()


# ── Active quiz ───────────────────────────────────────────────────────────────
questions = st.session_state.questions
idx = st.session_state.current_idx
total = len(questions)

if idx >= total or st.session_state.show_result:
    # ── Result screen ──────────────────────────────────────────────────────────
    score = st.session_state.score
    pct = int(score / total * 100) if total > 0 else 0

    st.markdown(f"""
    <div class='quiz-card'>
        <div style='font-size:3rem;'>{'🏆' if pct >= 80 else '📝'}</div>
        <h2>퀴즈 완료!</h2>
        <div style='font-size:2.5rem; font-weight:800; color:{"#4CAF50" if pct>=80 else "#f44336"};'>
            {score} / {total}
        </div>
        <div style='font-size:1.2rem; color:#6c757d;'>{pct}% 정답률</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 📋 오답 노트")
    wrongs = [a for a in st.session_state.answers if not a["correct"]]
    if not wrongs:
        st.success("모두 맞혔습니다! 완벽해요 🎉")
    else:
        for a in wrongs:
            meaning_line = f"<br><span style='color:#555; font-size:0.9em;'>뜻: {a['correct_meaning']}</span>" if a.get('correct_meaning') else ""
            st.markdown(f"""
            <div class='result-wrong'>
                <strong>{a.get('word', a.get('meaning', ''))}</strong><br>
                <span style='color:#666;'>정답: {a['answer']}</span>{meaning_line}<br>
                <span style='color:#999; font-size:0.9em;'>내 답: {a['user_answer']}</span>
            </div>
            """, unsafe_allow_html=True)

    # ── Obsidian export ────────────────────────────────────────────────────────
    st.markdown("---")
    daily = st.session_state.daily_wrong_words
    st.markdown(f"### 📤 옵시디언으로 내보내기  <span style='font-size:1rem;font-weight:400;color:#6c757d;'>({len(daily)}개 누적)</span>", unsafe_allow_html=True)
    if daily:
        st.caption(f"볼트 폴더를 선택하면 `{date.today().strftime('%Y-%m-%d')}_오답노트.md` 에 추가됩니다. (Chrome/Edge 전용)")
    render_obsidian_export(daily)
    if daily:
        if st.button("🗑️ 오늘 오답 목록 초기화", use_container_width=True):
            st.session_state.daily_wrong_words = []
            st.rerun()

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 다시 풀기", use_container_width=True, type="primary"):
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


# ── Progress bar ───────────────────────────────────────────────────────────────
progress = idx / total
st.markdown(f"""
<div class='progress-text'>문제 {idx + 1} / {total} &nbsp;|&nbsp;
점수 <span class='score-badge'>{st.session_state.score}</span></div>
""", unsafe_allow_html=True)
st.progress(progress)

q = questions[idx]

# ══════════════════════════════════════════════════════════════════════════════
# OX QUIZ
# ══════════════════════════════════════════════════════════════════════════════
if q["type"] == "ox":
    pron = q.get("pronunciation", "")
    st.markdown(f"""
    <div class='quiz-card'>
        <div class='quiz-word'>{q['word']}</div>
        {'<div class="quiz-pronunciation">[' + pron + ']</div>' if pron else ''}
        <div class='quiz-meaning-display'>{q['meaning']}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("이 단어의 뜻이 맞나요?")

    if not st.session_state.answered:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⭕  맞아요", use_container_width=True, type="primary"):
                correct = q["answer"] is True
                st.session_state.answered = True
                st.session_state.last_correct = correct
                if correct:
                    st.session_state.score += 1
                else:
                    add_to_daily_wrong(q["word"], q["correct_meaning"])
                st.session_state.answers.append({
                    "word": q["word"],
                    "answer": "O" if q["answer"] else "X",
                    "user_answer": "O",
                    "correct": correct,
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
                else:
                    add_to_daily_wrong(q["word"], q["correct_meaning"])
                st.session_state.answers.append({
                    "word": q["word"],
                    "answer": "O" if q["answer"] else "X",
                    "user_answer": "X",
                    "correct": correct,
                    "correct_meaning": q["correct_meaning"],
                })
                st.rerun()
    else:
        if st.session_state.last_correct:
            st.success("정답! 🎉")
            if not q["answer"]:
                st.info(f"📝 **{q['word']}** 의 올바른 뜻: {q['correct_meaning']}")
        else:
            st.error(f"오답 😢  정답: {'⭕' if q['answer'] else '❌'}")
            st.info(f"📝 **{q['word']}** 의 뜻: {q['correct_meaning']}")

        if st.button("다음 →", use_container_width=True, type="primary"):
            st.session_state.current_idx += 1
            st.session_state.answered = False
            st.session_state.last_correct = None
            if st.session_state.current_idx >= total:
                st.session_state.show_result = True
            st.rerun()


# ══════════════════════════════════════════════════════════════════════════════
# 단어 뜻 맞추기 (word → meaning)
# ══════════════════════════════════════════════════════════════════════════════
elif q["type"] == "choice_meaning":
    pron = q.get("pronunciation", "")
    st.markdown(f"""
    <div class='quiz-card'>
        <div style='font-size:1rem; color:#6c757d; margin-bottom:0.5rem;'>이 단어의 뜻은?</div>
        <div class='quiz-word'>{q['word']}</div>
        {'<div class="quiz-pronunciation">[' + pron + ']</div>' if pron else ''}
    </div>
    """, unsafe_allow_html=True)

    for i, choice in enumerate(q["choices"]):
        label = f"{['①','②','③','④'][i]}  {choice}"
        disabled = st.session_state.answered

        if st.session_state.answered:
            if choice == q["answer"]:
                st.success(label)
            elif choice == st.session_state.get("user_choice"):
                st.error(label)
            else:
                st.markdown(f"<div style='padding:8px; color:#999;'>{label}</div>", unsafe_allow_html=True)
        else:
            if st.button(label, use_container_width=True, key=f"choice_{i}"):
                correct = (choice == q["answer"])
                st.session_state.answered = True
                st.session_state.last_correct = correct
                st.session_state["user_choice"] = choice
                if correct:
                    st.session_state.score += 1
                else:
                    add_to_daily_wrong(q["word"], q["answer"])
                st.session_state.answers.append({
                    "word": q["word"],
                    "answer": q["answer"],
                    "user_answer": choice,
                    "correct": correct,
                    "correct_meaning": q["answer"],
                })
                st.rerun()

    if st.session_state.answered:
        if st.session_state.last_correct:
            st.success("정답! 🎉")
        else:
            st.error("오답 😢")
            st.info(f"📝 **{q['word']}** 의 뜻: {q['answer']}")
        if st.button("다음 →", use_container_width=True, type="primary"):
            st.session_state.current_idx += 1
            st.session_state.answered = False
            st.session_state.last_correct = None
            st.session_state.pop("user_choice", None)
            if st.session_state.current_idx >= total:
                st.session_state.show_result = True
            st.rerun()


# ══════════════════════════════════════════════════════════════════════════════
# 단어 맞추기 (meaning → word)
# ══════════════════════════════════════════════════════════════════════════════
elif q["type"] == "choice_word":
    st.markdown(f"""
    <div class='quiz-card'>
        <div style='font-size:1rem; color:#6c757d; margin-bottom:0.5rem;'>이 뜻에 해당하는 단어는?</div>
        <div class='quiz-meaning-display' style='font-size:1.4rem;'>{q['meaning']}</div>
    </div>
    """, unsafe_allow_html=True)

    for i, choice in enumerate(q["choices"]):
        label = f"{['①','②','③','④'][i]}  {choice}"

        if st.session_state.answered:
            if choice == q["answer"]:
                st.success(label)
            elif choice == st.session_state.get("user_choice"):
                st.error(label)
            else:
                st.markdown(f"<div style='padding:8px; color:#999;'>{label}</div>", unsafe_allow_html=True)
        else:
            if st.button(label, use_container_width=True, key=f"wc_{i}"):
                correct = (choice == q["answer"])
                st.session_state.answered = True
                st.session_state.last_correct = correct
                st.session_state["user_choice"] = choice
                if correct:
                    st.session_state.score += 1
                else:
                    add_to_daily_wrong(q["answer"], q["meaning"])
                st.session_state.answers.append({
                    "meaning": q["meaning"],
                    "answer": q["answer"],
                    "user_answer": choice,
                    "correct": correct,
                    "correct_meaning": q["meaning"],
                })
                st.rerun()

    if st.session_state.answered:
        if st.session_state.last_correct:
            st.success("정답! 🎉")
        else:
            st.error("오답 😢")
            st.info(f"📝 정답 단어: **{q['answer']}** — {q['meaning']}")
        if st.button("다음 →", use_container_width=True, type="primary"):
            st.session_state.current_idx += 1
            st.session_state.answered = False
            st.session_state.last_correct = None
            st.session_state.pop("user_choice", None)
            if st.session_state.current_idx >= total:
                st.session_state.show_result = True
            st.rerun()


# ══════════════════════════════════════════════════════════════════════════════
# 짝 맞추기 (matching)
# ══════════════════════════════════════════════════════════════════════════════
elif q["type"] == "match":
    left_words = q["left"]
    right_meanings = q["right"]
    correct_pairs = q["pairs"]
    user_pairs = st.session_state.match_user_pairs  # word → meaning
    submitted = st.session_state.match_submitted
    sel_side = st.session_state.match_selected_side
    sel_idx = st.session_state.match_selected_idx

    paired_words = set(user_pairs.keys())
    paired_meanings = set(user_pairs.values())

    st.markdown("**단어와 뜻을 짝지어 보세요!**")
    st.markdown("<br>", unsafe_allow_html=True)

    col_w, col_m = st.columns(2)

    with col_w:
        st.markdown("**단어**")
        for i, word in enumerate(left_words):
            is_paired = word in paired_words
            is_selected = (sel_side == "left" and sel_idx == i)

            if submitted:
                my_meaning = user_pairs.get(word)
                if my_meaning == correct_pairs.get(word):
                    st.success(f"✓ {word}")
                else:
                    st.error(f"✗ {word}")
                    st.caption(f"→ 실제 뜻: {correct_pairs.get(word, '')[:60]}")
            elif is_paired:
                st.markdown(f"""
                <div style='padding:10px 14px; border:2px solid #4CAF50; border-radius:10px;
                     background:#f0fff0; margin-bottom:8px; font-weight:600;'>
                    ✓ {word}
                </div>""", unsafe_allow_html=True)
            else:
                btn_label = f"▶ {word}" if is_selected else word
                if st.button(btn_label, key=f"left_{i}", use_container_width=True):
                    if sel_side == "left" and sel_idx == i:
                        # Deselect
                        st.session_state.match_selected_side = None
                        st.session_state.match_selected_idx = None
                    elif sel_side == "right" and sel_idx is not None:
                        # Pair this word with the already-selected meaning
                        selected_meaning = right_meanings[sel_idx]
                        st.session_state.match_user_pairs[word] = selected_meaning
                        st.session_state.match_selected_side = None
                        st.session_state.match_selected_idx = None
                    else:
                        st.session_state.match_selected_side = "left"
                        st.session_state.match_selected_idx = i
                    st.rerun()

    with col_m:
        st.markdown("**뜻**")
        for j, meaning in enumerate(right_meanings):
            is_paired = meaning in paired_meanings
            is_selected = (sel_side == "right" and sel_idx == j)

            if submitted:
                # Find which word this meaning was paired with
                matched_word = next((w for w, m in user_pairs.items() if m == meaning), None)
                if matched_word and correct_pairs.get(matched_word) == meaning:
                    st.success(f"✓ {meaning[:60]}")
                else:
                    actual_word = next((w for w, m in correct_pairs.items() if m == meaning), "?")
                    st.error(f"✗ {meaning[:60]}")
                    st.caption(f"→ 정답: {actual_word}")
            elif is_paired:
                st.markdown(f"""
                <div style='padding:10px 14px; border:2px solid #4CAF50; border-radius:10px;
                     background:#f0fff0; margin-bottom:8px;'>
                    ✓ {meaning[:60]}
                </div>""", unsafe_allow_html=True)
            else:
                btn_label = f"▶ {meaning[:50]}" if is_selected else meaning[:50]
                if st.button(btn_label, key=f"right_{j}", use_container_width=True):
                    if sel_side == "right" and sel_idx == j:
                        st.session_state.match_selected_side = None
                        st.session_state.match_selected_idx = None
                    elif sel_side == "left" and sel_idx is not None:
                        # Pair the selected left word with this meaning
                        selected_word = left_words[sel_idx]
                        st.session_state.match_user_pairs[selected_word] = meaning
                        st.session_state.match_selected_side = None
                        st.session_state.match_selected_idx = None
                    else:
                        st.session_state.match_selected_side = "right"
                        st.session_state.match_selected_idx = j
                    st.rerun()

    st.markdown("---")

    if not submitted:
        # Undo last pair
        col1, col2 = st.columns([1, 2])
        with col1:
            if user_pairs and st.button("↩ 마지막 취소", use_container_width=True):
                last_key = list(user_pairs.keys())[-1]
                del st.session_state.match_user_pairs[last_key]
                st.rerun()
        with col2:
            all_paired = len(user_pairs) == len(left_words)
            if st.button(
                "✅ 채점하기" if all_paired else f"짝 맞추기 ({len(user_pairs)}/{len(left_words)})",
                use_container_width=True,
                type="primary" if all_paired else "secondary",
                disabled=not all_paired,
            ):
                st.session_state.match_submitted = True
                # Score this round: binary (all correct = 1, else 0)
                correct_count = sum(
                    1 for w, m in user_pairs.items() if correct_pairs.get(w) == m
                )
                total_in_round = len(left_words)
                round_perfect = correct_count == total_in_round
                st.session_state.score += 1 if round_perfect else 0
                for w, m in user_pairs.items():
                    if correct_pairs.get(w) != m:
                        add_to_daily_wrong(w, correct_pairs.get(w, ""))
                st.session_state.answers.append({
                    "word": f"짝맞추기 라운드 {idx+1}",
                    "answer": f"{total_in_round}/{total_in_round} 완벽",
                    "user_answer": f"{correct_count}/{total_in_round}",
                    "correct": round_perfect,
                })
                st.rerun()
    else:
        correct_count = sum(
            1 for w, m in user_pairs.items() if correct_pairs.get(w) == m
        )
        total_in_round = len(left_words)
        if correct_count == total_in_round:
            st.success(f"완벽! {correct_count}/{total_in_round} 모두 정답 🎉")
        else:
            st.warning(f"{correct_count}/{total_in_round} 정답")

        if st.button("다음 라운드 →", use_container_width=True, type="primary"):
            st.session_state.current_idx += 1
            st.session_state.match_user_pairs = {}
            st.session_state.match_submitted = False
            st.session_state.match_selected_side = None
            st.session_state.match_selected_idx = None
            if st.session_state.current_idx >= total:
                st.session_state.show_result = True
            st.rerun()
