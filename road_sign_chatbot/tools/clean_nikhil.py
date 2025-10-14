import json

# Load your structured JSON
with open("data/processed/structured_nikhil.json", "r", encoding="utf-8") as f:
    data = json.load(f)

cleaned = []

for entry in data:
    desc = entry["description"].strip()
    if not desc:  # skip empty paragraphs
        continue

    # Example of fixing sign_name heuristically: take first 5 words in uppercase if the old one is too short
    if len(entry["sign_name"]) < 3:
        entry["sign_name"] = " ".join(desc.split()[:5]).upper()

    # You can fill category / sign_type manually here if obvious
    if "school" in desc.lower():
        entry["category"] = "Warning"
        entry["sign_type"] = "School Zone"
    elif "speed" in desc.lower():
        entry["category"] = "Regulatory"
        entry["sign_type"] = "Speed Limit"

    cleaned.append(entry)

# Save cleaned JSON
with open("data/processed/cleaned_nikhil.json", "w", encoding="utf-8") as f:
    json.dump(cleaned, f, ensure_ascii=False, indent=2)

print(f"✅ Cleaned JSON created with {len(cleaned)} entries")
