import os
from textblob import TextBlob

INPUT_DIR = "../dataset/topic_segments_baseline"
OUTPUT_DIR = "../dataset/topic_sentiments"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for file in os.listdir(INPUT_DIR):
    if not file.endswith(".txt"):
        continue

    text = open(os.path.join(INPUT_DIR, file), encoding="utf-8").read()
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.1:
        label = "Positive"
    elif polarity < -0.1:
        label = "Negative"
    else:
        label = "Neutral"

    with open(
        os.path.join(OUTPUT_DIR, file.replace(".txt", "_sentiment.txt")),
        "w"
    ) as f:
        f.write(f"Sentiment: {label}\nScore: {polarity:.2f}")

print("✅ Sentiment analysis completed")
