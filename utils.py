"""Shared CSS design system and helpers for GRE app."""
import html as _html
import streamlit as st


def esc(text: str) -> str:
    return _html.escape(str(text)) if text else ""


CSS = """<style>
/* ── Layout ─────────────────────────────────────── */
.main .block-container {
    max-width: 720px;
    padding-top: 1.2rem;
    padding-bottom: 3rem;
}

/* ── Progress bar ────────────────────────────────── */
div[data-testid="stProgressBar"] > div {
    background: #E2E8F0 !important;
    border-radius: 6px !important;
    height: 8px !important;
}
div[data-testid="stProgressBar"] > div > div {
    background: linear-gradient(90deg, #4F46E5, #818CF8) !important;
    border-radius: 6px !important;
}

/* ── Buttons ─────────────────────────────────────── */
.stButton > button {
    border-radius: 9px !important;
    font-weight: 600 !important;
    letter-spacing: 0.01em;
    transition: all 0.15s ease;
}
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #4F46E5, #6D28D9) !important;
    border: none !important;
    box-shadow: 0 2px 10px rgba(79,70,229,0.28) !important;
}
.stButton > button[kind="primary"]:hover {
    box-shadow: 0 4px 16px rgba(79,70,229,0.38) !important;
    transform: translateY(-1px);
}
.stButton > button[kind="secondary"] {
    border-color: #C7D2FE !important;
    color: #4F46E5 !important;
}

/* ── Expander ────────────────────────────────────── */
[data-testid="stExpander"] {
    border: 1.5px solid #E2E8F0 !important;
    border-radius: 10px !important;
    background: white !important;
}
[data-testid="stExpander"] summary {
    font-weight: 600;
    color: #374151;
}

/* ── Radio / Checkbox ────────────────────────────── */
[data-testid="stRadio"] > label { font-weight: 600; }
[data-testid="stRadio"] div[role="radiogroup"] label {
    background: white;
    border: 1.5px solid #E2E8F0;
    border-radius: 8px;
    padding: 8px 14px;
    margin: 3px 0;
    transition: border-color 0.15s;
    cursor: pointer;
}
[data-testid="stRadio"] div[role="radiogroup"] label:hover {
    border-color: #A5B4FC;
}

/* ═══════════════════════════════════════════════════
   VOCA — Word display
═══════════════════════════════════════════════════ */
.word-hero {
    background: linear-gradient(135deg, #312E81 0%, #4F46E5 55%, #7C3AED 100%);
    border-radius: 18px;
    padding: 38px 28px;
    text-align: center;
    margin: 6px 0 22px;
    box-shadow: 0 6px 28px rgba(79,70,229,0.22);
}
.wh-word {
    font-size: 2.8rem;
    font-weight: 800;
    color: #fff;
    letter-spacing: -0.03em;
    line-height: 1.1;
}
.wh-pron {
    color: rgba(255,255,255,0.65);
    font-size: 0.97rem;
    margin-top: 8px;
    font-style: italic;
}
.meaning-hero {
    background: linear-gradient(135deg, #064E3B, #047857);
    border-radius: 18px;
    padding: 30px 28px;
    text-align: center;
    margin: 6px 0 18px;
    box-shadow: 0 6px 24px rgba(4,120,87,0.18);
}
.mh-text {
    font-size: 1.35rem;
    font-weight: 700;
    color: #fff;
    line-height: 1.55;
}
.meaning-box {
    background: #fff;
    border: 1.5px solid #E2E8F0;
    border-radius: 12px;
    padding: 20px 26px;
    font-size: 1.05rem;
    color: #1E293B;
    line-height: 1.7;
    margin-bottom: 18px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.05);
}
.quiz-tip {
    text-align: center;
    font-size: 0.76rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.09em;
    color: #94A3B8;
    margin-bottom: 16px;
}
.match-hdr {
    background: #F1F5F9;
    border-radius: 8px;
    text-align: center;
    padding: 7px 10px;
    font-size: 0.74rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #475569;
    margin-bottom: 6px;
}

/* ═══════════════════════════════════════════════════
   BADGES — type & difficulty
═══════════════════════════════════════════════════ */
.badge-row { display: flex; gap: 8px; align-items: center; margin-bottom: 16px; }
.badge {
    display: inline-block;
    padding: 4px 11px;
    border-radius: 20px;
    font-size: 0.71rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
}
.b-easy   { background: #D1FAE5; color: #065F46; }
.b-medium { background: #FEF3C7; color: #92400E; }
.b-hard   { background: #FEE2E2; color: #991B1B; }
.b-tc  { background: #EEF2FF; color: #3730A3; }
.b-se  { background: #ECFDF5; color: #065F46; }
.b-rc  { background: #FFF7ED; color: #9A3412; }
.b-qc  { background: #EEF2FF; color: #3730A3; }
.b-mc  { background: #ECFDF5; color: #065F46; }
.b-mcm { background: #FDF4FF; color: #6B21A8; }
.b-ne  { background: #FFF7ED; color: #9A3412; }
.b-test { background: #FDF4FF; color: #6B21A8; }

/* ═══════════════════════════════════════════════════
   VERBAL — passage & stem
═══════════════════════════════════════════════════ */
.passage-box {
    background: #FFFBEB;
    border-left: 4px solid #F59E0B;
    border-radius: 0 12px 12px 0;
    padding: 18px 22px;
    margin-bottom: 18px;
    font-size: 0.93rem;
    color: #374151;
    line-height: 1.9;
    white-space: pre-wrap;
}
.stem-box {
    background: #fff;
    border: 1.5px solid #E2E8F0;
    border-radius: 12px;
    padding: 16px 20px;
    font-size: 1.04rem;
    font-weight: 500;
    color: #1E293B;
    line-height: 1.78;
    margin-bottom: 20px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.04);
}

/* ═══════════════════════════════════════════════════
   QUANT — context & QC grid
═══════════════════════════════════════════════════ */
.context-box {
    background: #EFF6FF;
    border: 1.5px solid #BFDBFE;
    border-radius: 12px;
    padding: 14px 20px;
    color: #1E40AF;
    font-size: 0.93rem;
    line-height: 1.7;
    margin-bottom: 18px;
}
.qc-wrap {
    display: grid;
    grid-template-columns: 1fr 48px 1fr;
    margin: 14px 0 24px;
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 2px 10px rgba(0,0,0,0.07);
}
.qc-a-cell {
    background: #EEF2FF;
    border: 2px solid #C7D2FE;
    border-right: none;
    border-radius: 14px 0 0 14px;
    padding: 22px 16px;
    text-align: center;
}
.qc-b-cell {
    background: #F0FDF4;
    border: 2px solid #BBF7D0;
    border-left: none;
    border-radius: 0 14px 14px 0;
    padding: 22px 16px;
    text-align: center;
}
.qc-vs-cell {
    background: #F8FAFC;
    border-top: 2px solid #E2E8F0;
    border-bottom: 2px solid #E2E8F0;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1rem;
    font-weight: 800;
    color: #94A3B8;
}
.qc-label {
    font-size: 0.66rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    margin-bottom: 10px;
}
.qc-a-cell .qc-label { color: #3730A3; }
.qc-b-cell .qc-label { color: #166534; }
.qc-val {
    font-size: 1.2rem;
    font-weight: 700;
    color: #1E293B;
    line-height: 1.45;
}

/* ═══════════════════════════════════════════════════
   FEEDBACK
═══════════════════════════════════════════════════ */
.fb-correct {
    background: #D1FAE5;
    border: 1.5px solid #6EE7B7;
    border-radius: 10px;
    padding: 14px 20px;
    color: #065F46;
    font-weight: 700;
    margin: 14px 0;
    font-size: 0.97rem;
}
.fb-wrong {
    background: #FEE2E2;
    border: 1.5px solid #FCA5A5;
    border-radius: 10px;
    padding: 14px 20px;
    color: #991B1B;
    font-weight: 700;
    margin: 14px 0;
    font-size: 0.97rem;
}
.fb-detail {
    font-weight: 400;
    margin-top: 6px;
    font-size: 0.9rem;
    opacity: 0.85;
}

/* ═══════════════════════════════════════════════════
   RESULT SCREEN
═══════════════════════════════════════════════════ */
.result-hero {
    background: linear-gradient(135deg, #312E81, #4F46E5, #7C3AED);
    border-radius: 18px;
    padding: 36px 24px 30px;
    text-align: center;
    color: #fff;
    margin-bottom: 22px;
    box-shadow: 0 8px 28px rgba(79,70,229,0.24);
}
.rh-pct   { font-size: 4rem; font-weight: 800; line-height: 1; }
.rh-score { font-size: 1.05rem; opacity: 0.78; margin-top: 6px; }
.rh-msg   { font-size: 1rem; opacity: 0.65; margin-top: 4px; font-style: italic; }
.stat-row { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; margin: 18px 0; }
.stat-box {
    background: #fff;
    border: 1.5px solid #E2E8F0;
    border-radius: 12px;
    padding: 18px 10px;
    text-align: center;
    box-shadow: 0 1px 4px rgba(0,0,0,0.04);
}
.stat-val { font-size: 1.7rem; font-weight: 800; color: #4F46E5; }
.stat-lbl { font-size: 0.72rem; font-weight: 700; color: #6B7280; margin-top: 4px; text-transform: uppercase; letter-spacing: 0.06em; }
.wrong-list {
    background: #fff;
    border: 1.5px solid #FEE2E2;
    border-radius: 12px;
    overflow: hidden;
    margin-top: 16px;
}
.wrong-hdr {
    background: #FEF2F2;
    padding: 10px 18px;
    font-size: 0.78rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: #DC2626;
}
.wrong-item {
    display: flex;
    align-items: baseline;
    padding: 11px 18px;
    border-bottom: 1px solid #FEF2F2;
    font-size: 0.92rem;
}
.wrong-item:last-child { border-bottom: none; }
.wi-word { font-weight: 700; color: #DC2626; min-width: 130px; flex-shrink: 0; }
.wi-sep  { color: #CBD5E1; margin: 0 10px; }
.wi-ans  { color: #374151; flex: 1; }

/* ── Answer card (오답 피드백) ───────────────────── */
.answer-card {
    background: #EFF6FF;
    border: 1.5px solid #BFDBFE;
    border-radius: 10px;
    padding: 12px 18px;
    margin: 10px 0 0;
    font-size: 0.94rem;
    line-height: 1.65;
    display: flex;
    align-items: baseline;
    flex-wrap: wrap;
    gap: 4px;
}
.ac-label { font-size: 0.7rem; font-weight: 700; text-transform: uppercase;
             letter-spacing: 0.07em; color: #93C5FD; margin-right: 4px; }
.ac-word  { font-weight: 800; font-size: 1.05rem; color: #1E3A8A; }
.ac-sep   { color: #93C5FD; margin: 0 6px; font-weight: 400; }
.ac-meaning { color: #1E40AF; }

/* ── Divider ─────────────────────────────────────── */
.sdiv { border: none; border-top: 1px solid #E2E8F0; margin: 22px 0; }
</style>"""


def inject_css():
    st.markdown(CSS, unsafe_allow_html=True)
