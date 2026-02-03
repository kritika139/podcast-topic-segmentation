import os
import re

input_dir = "../dataset/topic_segments_embeddings"
output_dir = "../dataset/topic_summaries"

os.makedirs(output_dir, exist_ok=True)

files = sorted([f for f in os.listdir(input_dir) if f.endswith(".txt")])

def split_sentences(text):
    # Simple sentence splitter
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in sentences if len(s.strip()) > 30]

for file in files:
    with open(os.path.join(input_dir, file), "r", encoding="utf-8") as f:
        text = f.read().strip()

    sentences = split_sentences(text)

    if not sentences:
        continue

    summary = " ".join(sentences[:2])

    output_path = os.path.join(output_dir, file.replace(".txt", "_summary.txt"))
    with open(output_path, "w", encoding="utf-8") as out:
        out.write(summary)

print("✅ Summaries generated successfully")
