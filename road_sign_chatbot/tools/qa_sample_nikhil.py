import json

# Load cleaned JSON
with open("data/processed/cleaned_nikhil.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Remove duplicates by sign_name
unique = {}
for entry in data:
    name = entry["sign_name"]
    if name not in unique:
        unique[name] = entry

# Save final cleaned JSON
final_cleaned = list(unique.values())
with open("data/processed/final_cleaned_nikhil.json", "w", encoding="utf-8") as f:
    json.dump(final_cleaned, f, ensure_ascii=False, indent=2)

# Save a small sample (first 20 entries) for testing
sample = final_cleaned[:20]
with open("data/processed/sample_nikhil.json", "w", encoding="utf-8") as f:
    json.dump(sample, f, ensure_ascii=False, indent=2)

print(f"✅ QA done. Final cleaned: {len(final_cleaned)} entries, sample: {len(sample)} entries")
