from docx import Document
import json, sys

def extract_text(doc_path, start_page, end_page):
    doc = Document(doc_path)
    result = []
    page_count = 0
    for p in doc.paragraphs:
        text = p.text.strip()
        if not text:
            continue
        # Rough estimate of pages based on paragraph count
        page_count += len(text) // 800  # approx every 800 chars = 1 page
        if page_count < start_page or page_count > end_page:
            continue
        result.append(text)
    return result

if __name__ == "__main__":
    doc_path = sys.argv[1]
    start_page = int(sys.argv[2])
    end_page = int(sys.argv[3])
    out_path = sys.argv[4]

    text_data = extract_text(doc_path, start_page, end_page)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(text_data, f, ensure_ascii=False, indent=2)

    print(f"✅ Extracted roughly pages {start_page}-{end_page} → {out_path}")
