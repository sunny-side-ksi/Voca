"""
GRE Official Guide PDF → Markdown + 섹션별 분리
pypdfium2 직접 사용 (docling ML 모델 불필요)
"""
import json
import re
import sys
import time
from pathlib import Path

import pypdfium2 as pdfium

PDF_PATH = Path(__file__).parent / "GRE - Official Guide to the GRE General Test, Third Edition eBook.pdf"
OUT_DIR = Path(__file__).parent / "gre_content"
OUT_DIR.mkdir(exist_ok=True)


# ── 챕터 감지 패턴 (GRE 공식 가이드 3판 구조 기반) ────────────────────────
CHAPTER_PATTERNS = [
    (r"chapter\s+\d+", "chapter"),
    (r"part\s+[ivxlcdm]+\b", "part"),
    (r"verbal reasoning", "verbal"),
    (r"quantitative reasoning", "quant"),
    (r"analytical writing", "writing"),
    (r"text completion", "text_completion"),
    (r"sentence equivalence", "sentence_equivalence"),
    (r"reading comprehension", "reading_comprehension"),
    (r"arithmetic", "quant_arithmetic"),
    (r"algebra", "quant_algebra"),
    (r"geometry", "quant_geometry"),
    (r"data analysis", "quant_data"),
    (r"practice test", "practice_test"),
]

# 문제 번호 패턴 (예: "1.", "Question 1", "(A)" 등)
QUESTION_RE = re.compile(r"^\s*(?:question\s+)?\d+[\.\)]\s", re.IGNORECASE)
CHOICE_RE = re.compile(r"^\s*[A-Ea-e][\.\)]\s")


def extract_pages(pdf_path: Path) -> list[dict]:
    """각 페이지의 텍스트를 추출하여 반환"""
    print(f"PDF 로딩: {pdf_path.name}")
    doc = pdfium.PdfDocument(str(pdf_path))
    total = len(doc)
    print(f"총 {total}페이지")

    pages = []
    t0 = time.time()
    for i, page in enumerate(doc):
        if i % 50 == 0:
            print(f"  추출 중... {i}/{total} ({time.time()-t0:.1f}s)")
        text_page = page.get_textpage()
        text = text_page.get_text_range()
        pages.append({"page": i + 1, "text": text})
        text_page.close()
        page.close()

    doc.close()
    elapsed = time.time() - t0
    print(f"텍스트 추출 완료 ({elapsed:.1f}초, {total}페이지)")
    return pages


def detect_section(text: str) -> str | None:
    """텍스트에서 섹션 키워드 감지"""
    low = text.lower()
    for pattern, label in CHAPTER_PATTERNS:
        if re.search(pattern, low):
            return label
    return None


def build_markdown(pages: list[dict]) -> str:
    """페이지 목록 → 마크다운 문자열"""
    lines = []
    current_section = None

    for p in pages:
        page_num = p["page"]
        text = p["text"].strip()
        if not text:
            continue

        # 섹션 감지 (첫 100자 기준)
        snippet = text[:100]
        detected = detect_section(snippet)
        if detected and detected != current_section:
            current_section = detected
            lines.append(f"\n\n---\n## [{detected.upper().replace('_', ' ')}] (p.{page_num})\n")

        # 페이지 구분자
        lines.append(f"\n<!-- page {page_num} -->")

        # 문단 분리 (빈 줄 기준)
        for para in re.split(r"\n{2,}", text):
            para = para.strip()
            if not para:
                continue
            lines.append(para + "\n")

    return "\n".join(lines)


def extract_questions(pages: list[dict]) -> list[dict]:
    """
    문제 패턴 감지 → 구조화된 문제 리스트 반환
    (간단한 휴리스틱: 번호 + 선택지 패턴)
    """
    questions = []
    all_text = "\n".join(p["text"] for p in pages)
    current_q = None
    section = "unknown"

    for line in all_text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue

        # 섹션 감지
        detected = detect_section(stripped[:80])
        if detected:
            section = detected

        # 문제 시작 감지
        if QUESTION_RE.match(stripped):
            if current_q:
                questions.append(current_q)
            current_q = {
                "section": section,
                "stem": stripped,
                "choices": [],
            }
        elif current_q and CHOICE_RE.match(stripped):
            current_q["choices"].append(stripped)
        elif current_q and stripped:
            current_q["stem"] += " " + stripped

    if current_q:
        questions.append(current_q)

    return questions


def split_by_section(pages: list[dict]) -> dict[str, list[dict]]:
    """섹션별로 페이지 그룹핑"""
    sections: dict[str, list[dict]] = {}
    current = "intro"

    for p in pages:
        detected = detect_section(p["text"][:150])
        if detected:
            current = detected
        sections.setdefault(current, []).append(p)

    return sections


def main():
    print(f"출력 폴더: {OUT_DIR}\n")

    # 1. 텍스트 추출
    pages = extract_pages(PDF_PATH)

    # 2. 전체 마크다운 저장
    print("\n마크다운 변환 중...")
    md_text = build_markdown(pages)
    md_path = OUT_DIR / "gre_guide_full.md"
    md_path.write_text(md_text, encoding="utf-8")
    print(f"마크다운 저장: {md_path.name}  ({len(md_text):,} 글자)")

    # 3. 전체 페이지 JSON 저장
    json_pages_path = OUT_DIR / "gre_pages.json"
    json_pages_path.write_text(
        json.dumps(pages, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"페이지 JSON: {json_pages_path.name}")

    # 4. 섹션별 분리 저장
    print("\n섹션별 분리 중...")
    sections = split_by_section(pages)
    for sec_name, sec_pages in sections.items():
        sec_path = OUT_DIR / f"section_{sec_name}.md"
        sec_md = build_markdown(sec_pages)
        if sec_md.strip():
            sec_path.write_text(sec_md, encoding="utf-8")
            print(f"  {sec_path.name}  ({len(sec_pages)} 페이지)")

    # 5. 문제 추출 (휴리스틱)
    print("\n문제 패턴 추출 중...")
    questions = extract_questions(pages)
    q_path = OUT_DIR / "gre_questions_raw.json"
    q_path.write_text(
        json.dumps(questions, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"감지된 문제: {len(questions)}개 → {q_path.name}")

    # 6. 요약
    print("\n=== 완료 ===")
    print(f"총 {len(pages)}페이지 추출")
    print(f"섹션: {list(sections.keys())}")
    print(f"감지 문제: {len(questions)}개")
    print(f"\n결과물 위치: {OUT_DIR}")


if __name__ == "__main__":
    main()
