"""Render all C.pdf pages as PNG images for OCR via vision."""
import pymupdf
from pathlib import Path

PDF_PATH = Path(__file__).parent / "C.pdf"
OUT_DIR = Path(__file__).parent / "cr_pages"
OUT_DIR.mkdir(exist_ok=True)

doc = pymupdf.open(str(PDF_PATH))
print(f"Total pages: {len(doc)}")
mat = pymupdf.Matrix(2.5, 2.5)  # high-res for readability

for i, page in enumerate(doc):
    pix = page.get_pixmap(matrix=mat)
    out = OUT_DIR / f"page_{i+1:02d}.png"
    pix.save(str(out))
    print(f"  Saved page {i+1}")

doc.close()
print("Done.")
