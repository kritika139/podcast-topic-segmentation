import os
import re

INPUT_DIR = "../dataset/transcripts_clean"
OUTPUT_DIR = "../dataset/transcripts_sentences"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def split_sentences(line):
    timestamp = re.match(r"\[.*?\]", line)
    text = re.sub(r"\[.*?\]", "", line).strip()

    sentences = re.split(r'(?<=[.!?])\s+', text)

    results = []
    for sent in sentences:
        if sent.strip():
            if timestamp:
                results.append(f"{timestamp.group()} {sent.strip()}\n")
            else:
                results.append(sent.strip() + "\n")
    return results

for file in sorted(os.listdir(INPUT_DIR)):
    if file.endswith(".txt"):
        with open(os.path.join(INPUT_DIR, file), "r", encoding="utf-8") as f:
            lines = f.readlines()

        sentence_lines = []
        for line in lines:
            sentence_lines.extend(split_sentences(line))

        with open(os.path.join(OUTPUT_DIR, file), "w", encoding="utf-8") as f:
            f.writelines(sentence_lines)

print("✅ Sentence segmentation completed.")
