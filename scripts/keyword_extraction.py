import os
from sklearn.feature_extraction.text import TfidfVectorizer

input_dir = "../dataset/topic_segments_embeddings"
output_dir = "../dataset/topic_keywords"

os.makedirs(output_dir, exist_ok=True)

files = sorted([f for f in os.listdir(input_dir) if f.endswith(".txt")])

for file in files:
    with open(os.path.join(input_dir, file), "r", encoding="utf-8") as f:
        text = f.read().strip()

    # Skip very small segments
    if len(text.split()) < 20:
        continue

    vectorizer = TfidfVectorizer(
        stop_words="english",
        token_pattern=r'(?u)\b[a-zA-Z][a-zA-Z]+\b',
        max_features=10
    )

    tfidf = vectorizer.fit_transform([text])
    keywords = vectorizer.get_feature_names_out()

    output_path = os.path.join(output_dir, file.replace(".txt", "_keywords.txt"))
    with open(output_path, "w", encoding="utf-8") as out:
        for kw in keywords:
            out.write(kw + "\n")

print("Keyword extraction completed successfully")
