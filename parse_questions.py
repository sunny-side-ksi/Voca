"""
GRE Official Guide — Question Parser
Input : gre_content/gre_pages.json
Output: gre_content/verbal_questions.json
        gre_content/quant_questions.json
"""
import re
import json
from pathlib import Path

BASE = Path(__file__).parent
CONTENT = BASE / "gre_content"
PAGES = json.loads((CONTENT / "gre_pages.json").read_text(encoding="utf-8"))

# ── Regex patterns ─────────────────────────────────────────────────────────────

# Choice line: handles "XA text", "X A text", "wA text", "A   text"
CHOICE_RE = re.compile(r"^[Xw]?\s{0,2}([A-F])\s{1,4}(?=\S)(.+)$")

# Question number line: "1. stem" or "1\t stem"
QSTART_RE = re.compile(r"^(\d{1,2})[.\t]\s*(?=\S)(.+)$")

# Explanation marker
EXPL_RE = re.compile(r"^Explanation\s*$", re.IGNORECASE)

# SET difficulty header
SET_RE = re.compile(r"SET\s+(\d+)[.\s:]+(.+)", re.IGNORECASE)

# Section markers
VERBAL_SECTION_RE = re.compile(r"Verbal Reasoning\s+Practice Questions", re.IGNORECASE)
QUANT_SECTION_RE = re.compile(r"Quantitative Reasoning\s+Practice Questions", re.IGNORECASE)
MATH_REVIEW_RE = re.compile(r"Math Review|8\s+GRE.*Math Review", re.IGNORECASE)
PRACTICE_TEST_RE = re.compile(r"Practice Test\s+\d", re.IGNORECASE)

# Quantitative Comparison detection
QC_RE = re.compile(r"Quantity\s+[AB]", re.IGNORECASE)
QC_ABCD_RE = re.compile(r"\bA\s+B\s+C\s+D\b")

# Blank (i)/(ii)/(iii) for multi-blank TC
BLANK_HDR_RE = re.compile(r"^Blank\s*\(([ivxIVX]+)\)\s*$", re.IGNORECASE)

# Select all / Sentence equivalence
SELECT_ALL_RE = re.compile(r"Indicate all|select all that apply", re.IGNORECASE)
SE_6_CHOICES = 6  # sentence equivalence always has 6 choices

# Junk lines (page headers, watermarks)
JUNK_RE = re.compile(
    r"^(?:GRE\s+(?:Verbal|Quantitative|Analytical)\s+(?:Reasoning|Writing)|"
    r"This ebook was issued|DOHYUN CHOI|SdkBytes|\d{1,3}\s*$)",
    re.IGNORECASE,
)

# Correct answer extraction (order matters — most specific first)
CORRECT_PATTERNS = [
    # "correct answer is Choice A and Choice C"
    re.compile(
        r"correct answers?\s+(?:are|is)[^A-F]*(?:Choice\s+)?([A-F])[^A-F]+(?:Choice\s+)?([A-F])",
        re.IGNORECASE,
    ),
    # "(Choice A) and (Choice F)"
    re.compile(r"\(Choice\s+([A-F])\)[^A-F]+\(Choice\s+([A-F])\)", re.IGNORECASE),
    # "correct answer is Choice A"
    re.compile(r"correct answer is[^A-F]*(?:Choice\s+)?([A-F])\b", re.IGNORECASE),
    # "(Choice A)"
    re.compile(r"\(Choice\s+([A-F])\)", re.IGNORECASE),
    # "The correct answer is D"
    re.compile(r"correct answer is\s+([A-F])\b", re.IGNORECASE),
]

QC_STANDARD_CHOICES = {
    "A": "Quantity A is greater",
    "B": "Quantity B is greater",
    "C": "The two quantities are equal",
    "D": "The relationship cannot be determined from the information given",
}

DIFF_MAP = {"1": "easy", "2": "medium", "3": "hard", "4": "hard", "5": "hard", "6": "hard"}


# ── Helpers ───────────────────────────────────────────────────────────────────

def clean_line(line: str) -> str:
    """Strip non-printable artifacts, normalize."""
    line = line.replace("\r", "").replace("￾", "").replace("�", "")
    line = re.sub(r"[^\x09\x0A\x20-\x7E -￼]", "", line)
    return line.strip()


def extract_correct(text: str) -> list[str]:
    for pat in CORRECT_PATTERNS:
        m = pat.search(text)
        if m:
            result = [m.group(1).upper()]
            if len(m.groups()) >= 2 and m.group(2):
                result.append(m.group(2).upper())
            return sorted(set(result))
    return []


def infer_difficulty(set_header_text: str, set_num: str) -> str:
    h = set_header_text.lower()
    if "easy" in h:
        return "easy"
    if "medium" in h:
        return "medium"
    if "hard" in h:
        return "hard"
    return DIFF_MAP.get(set_num, "medium")


def parse_block(lines: list[str], section: str, difficulty: str, idx: int) -> dict | None:
    """Parse a question block (lines between question number markers)."""
    if not lines:
        return None

    # Split at "Explanation" marker
    expl_idx = next((i for i, l in enumerate(lines) if EXPL_RE.match(l)), None)
    pre = lines[:expl_idx] if expl_idx is not None else lines
    expl_lines = lines[expl_idx + 1 :] if expl_idx is not None else []
    explanation = " ".join(l for l in expl_lines if l).strip()
    explanation = re.sub(r"\s{2,}", " ", explanation)

    # Parse stem + choices from pre
    stem_lines: list[str] = []
    choices: dict[str, str] = {}
    blank_choices: dict[str, dict[str, str]] = {}
    current_blank: str | None = None
    in_choices = False
    is_multiblank = False

    for line in pre:
        if not line:
            continue
        # Blank header?
        bm = BLANK_HDR_RE.match(line)
        if bm:
            is_multiblank = True
            current_blank = bm.group(1).lower()
            blank_choices.setdefault(current_blank, {})
            continue
        # Choice line?
        cm = CHOICE_RE.match(line)
        if cm:
            letter = cm.group(1).upper()
            text = cm.group(2).strip()
            in_choices = True
            if is_multiblank and current_blank:
                blank_choices[current_blank][letter] = text
            else:
                choices[letter] = text
            continue
        # Non-choice line
        if not in_choices:
            stem_lines.append(line)

    stem = " ".join(stem_lines).strip()
    stem = re.sub(r"\s{2,}", " ", stem)

    if not stem:
        return None

    # Determine type
    pre_text = "\n".join(pre)
    is_qc = QC_RE.search(pre_text) and QC_ABCD_RE.search(pre_text)
    is_select_all = SELECT_ALL_RE.search(stem) or SELECT_ALL_RE.search(explanation)
    n_choices = len(choices)

    if is_qc and n_choices < 4:
        choices = dict(QC_STANDARD_CHOICES)
        q_type = "quantitative_comparison"
    elif is_multiblank:
        q_type = "text_completion_multiblank"
    elif n_choices == SE_6_CHOICES:
        q_type = "sentence_equivalence"
    elif is_select_all:
        q_type = "multiple_choice_select_all"
    else:
        q_type = "multiple_choice"

    if not choices:
        return None

    correct = extract_correct(explanation)
    prefix = "V" if section == "verbal" else "Q"
    return {
        "id": f"{prefix}{idx:04d}",
        "section": section,
        "type": q_type,
        "difficulty": difficulty,
        "stem": stem,
        "choices": choices,
        "blank_choices": blank_choices or None,
        "correct": correct,
        "explanation": explanation,
    }


# ── Main parsing loop ─────────────────────────────────────────────────────────

def parse_all():
    verbal_qs: list[dict] = []
    quant_qs: list[dict] = []

    current_section: str | None = None  # "verbal" | "quant" | None
    current_diff = "medium"
    q_lines: list[str] = []
    in_q = False
    v_idx = q_idx = 0

    def flush(sect: str) -> None:
        nonlocal v_idx, q_idx
        if not q_lines or not sect:
            return
        qs_list = verbal_qs if sect == "verbal" else quant_qs
        idx = v_idx if sect == "verbal" else q_idx
        q = parse_block(q_lines, sect, current_diff, idx + 1)
        if q:
            qs_list.append(q)
            if sect == "verbal":
                v_idx += 1
            else:
                q_idx += 1

    for page in PAGES:
        raw = page["text"].replace("\r\n", "\n").replace("\r", "\n")
        for raw_line in raw.splitlines():
            line = clean_line(raw_line)

            # Skip junk
            if not line or JUNK_RE.match(line):
                continue

            # ── Section detection ────────────────────────────────────────────
            if VERBAL_SECTION_RE.search(line):
                if current_section:
                    flush(current_section)
                current_section = "verbal"
                in_q = False
                q_lines = []
                continue

            if QUANT_SECTION_RE.search(line):
                if current_section:
                    flush(current_section)
                current_section = "quant"
                in_q = False
                q_lines = []
                continue

            if (MATH_REVIEW_RE.search(line) or PRACTICE_TEST_RE.search(line)):
                flush(current_section)
                current_section = None
                in_q = False
                q_lines = []
                continue

            if current_section is None:
                continue

            # ── SET header (difficulty) ──────────────────────────────────────
            sm = SET_RE.match(line)
            if sm:
                flush(current_section)
                in_q = False
                q_lines = []
                current_diff = infer_difficulty(sm.group(2), sm.group(1))
                continue

            # ── Question number ──────────────────────────────────────────────
            qm = QSTART_RE.match(line)
            if qm:
                flush(current_section)
                q_lines = [qm.group(2).strip()]
                in_q = True
                continue

            # ── Continuation lines ───────────────────────────────────────────
            if in_q:
                q_lines.append(line)

    # Flush last question
    flush(current_section)

    return verbal_qs, quant_qs


# ── Run ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("GRE 문제 파싱 중...")
    verbal, quant = parse_all()

    # Stats
    print(f"\nVerbal: {len(verbal)}개")
    v_types = {}
    for q in verbal:
        v_types[q["type"]] = v_types.get(q["type"], 0) + 1
    for t, c in sorted(v_types.items(), key=lambda x: -x[1]):
        print(f"  {t}: {c}")

    print(f"\nQuant: {len(quant)}개")
    q_types = {}
    for q in quant:
        q_types[q["type"]] = q_types.get(q["type"], 0) + 1
    for t, c in sorted(q_types.items(), key=lambda x: -x[1]):
        print(f"  {t}: {c}")

    # Save
    vp = CONTENT / "verbal_questions.json"
    qp = CONTENT / "quant_questions.json"
    vp.write_text(json.dumps(verbal, ensure_ascii=False, indent=2), encoding="utf-8")
    qp.write_text(json.dumps(quant, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n저장 완료:\n  {vp}\n  {qp}")

    # Sample output
    if verbal:
        print("\n── Verbal 샘플 ────────────────────────────────────")
        q = verbal[0]
        print(f"ID: {q['id']}  type: {q['type']}  diff: {q['difficulty']}")
        print(f"Stem: {q['stem'][:120]}")
        print(f"Choices: {list(q['choices'].items())[:3]}")
        print(f"Correct: {q['correct']}")
        print(f"Explanation: {q['explanation'][:100]}")

    if quant:
        print("\n── Quant 샘플 ─────────────────────────────────────")
        q = quant[0]
        print(f"ID: {q['id']}  type: {q['type']}  diff: {q['difficulty']}")
        print(f"Stem: {q['stem'][:120]}")
        print(f"Choices: {list(q['choices'].items())[:3]}")
        print(f"Correct: {q['correct']}")
