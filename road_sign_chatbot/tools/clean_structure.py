import json

# Load raw extracted text
with open("data/processed/extracted_rahul.json", "r", encoding="utf-8") as f:
    paragraphs = json.load(f)

structured = []
counter = 1

for p in paragraphs:
    # Simple heuristic: first line or uppercase words = sign_name
    sign_name = p.split(".")[0][:30].upper()  # adjust heuristic if needed
    entry = {
        "id": f"N{counter}",
        "sign_name": sign_name,
        "category": "",        # fill manually later
        "sign_type": "",       # fill manually later
        "description": p,
        "placement_rules": "",
        "dimensions_m": {},
        "distance_m": None,
        "height_m": None,
        "examples": [],
        "source_section": "",
        "source_text_snippet": p[:100],
        "notes": "",
        "page_range": ""
    }
    structured.append(entry)
    counter += 1

# Save structured JSON
with open("data/processed/structured_rahul.json", "w", encoding="utf-8") as f:
    json.dump(structured, f, ensure_ascii=False, indent=2)

print(f"✅ Structured JSON created with {len(structured)} entries")
