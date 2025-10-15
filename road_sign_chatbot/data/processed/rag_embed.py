import json
import ollama

# Load chunks
with open("chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

print(f"Loaded {len(chunks)} chunks for embedding...")

# Create embeddings for each chunk
embeddings = []
for i, chunk in enumerate(chunks):
    response = ollama.embeddings(model="llama3", prompt=chunk)
    embeddings.append(response["embedding"])
    if (i + 1) % 10 == 0:
        print(f"Embedded {i + 1}/{len(chunks)} chunks")

# Save embeddings
with open("embeddings.json", "w", encoding="utf-8") as f:
    json.dump(embeddings, f)

print("✅ Embeddings saved as embeddings.json")
