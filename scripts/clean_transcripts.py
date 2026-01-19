import os
import re

INPUT_DIR = "../dataset/transcripts"
OUTPUT_DIR = "../dataset/transcripts_clean"

os.makedirs(OUTPUT_DIR, exist_ok=True)

filler_words = [
    "um", "uh", "ah", "er", "hmm",
    "you know", "like", "okay", "alright"
]

def clean_line(line):
    # Keep timestamps untouched
    timestamp = re.match(r"\[.*?\]", line)
    text = re.sub(r"\[.*?\]", "", line)

    text = text.lower()

    for filler in filler_words:
        text = re.sub(rf"\b{filler}\b", "", text)

    text = re.sub(r"[^a-z0-9\s\.\,]", "", text)
    text = re.sub(r"\s+", " ", text).strip()

    if timestamp:
        return f"{timestamp.group()} {text}\n"
    else:
        return text + "\n"

for file in sorted(os.listdir(INPUT_DIR)):
    if file.endswith(".txt"):
        with open(os.path.join(INPUT_DIR, file), "r", encoding="utf-8") as f:
            lines = f.readlines()

        cleaned_lines = [clean_line(line) for line in lines]

        with open(os.path.join(OUTPUT_DIR, file), "w", encoding="utf-8") as f:
            f.writelines(cleaned_lines)

print("✅ All transcripts cleaned and normalized.")
