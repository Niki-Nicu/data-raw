import json
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load JSON file
with open("extracted_nikhil.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Convert to plain text
if isinstance(data, list):
    text = " ".join(str(item) for item in data)
elif isinstance(data, dict):
    text = " ".join(str(value) for value in data.values())
else:
    text = str(data)

print(f"Loaded {len(text)} characters from the document.")

# Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len
)

chunks = splitter.split_text(text)
print(f"✅ Split into {len(chunks)} chunks")

# Optional: Save chunks for later use
with open("chunks.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f, ensure_ascii=False, indent=2)
print("💾 Chunks saved as chunks.json")
