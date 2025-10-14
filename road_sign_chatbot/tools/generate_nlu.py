import json
import yaml

# Load JSON properly
with open("data/processed/final_cleaned_nikhil.json", "r", encoding="utf-8") as f:
    data = json.load(f)

nlu_data = {"version": "3.1", "nlu": []}

for item in data:
    title = item.get("sign_name", "").strip().lower()
    description = item.get("description", "").strip()

    if title and description:
        nlu_data["nlu"].append({
            "intent": title.replace(" ", "_"),
            "examples": f"- {description}"
        })

# Save YAML output
with open("data/processed/nlu.yml", "w", encoding="utf-8") as f:
    yaml.dump(nlu_data, f, allow_unicode=True, sort_keys=False)
