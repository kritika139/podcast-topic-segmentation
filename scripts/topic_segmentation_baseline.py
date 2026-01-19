import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

input_dir = "../dataset/merged_transcripts"
output_dir = "../dataset/topic_segments_baseline"

os.makedirs(output_dir, exist_ok=True)

files = sorted([f for f in os.listdir(input_dir) if f.endswith(".txt")])

documents = []
for f in files:
    with open(os.path.join(input_dir, f), "r", encoding="utf-8") as file:
        documents.append(file.read())

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(
    stop_words="english",
    min_df=2
)
tfidf = vectorizer.fit_transform(documents)

# Compute similarity
similarities = []
for i in range(len(documents) - 1):
    sim = cosine_similarity(tfidf[i], tfidf[i + 1])[0][0]
    similarities.append(sim)

threshold = sum(similarities) / len(similarities)

segments = []
current_segment = [0]

for i, sim in enumerate(similarities):
    if sim < threshold:
        segments.append(current_segment)
        current_segment = []
    current_segment.append(i + 1)

segments.append(current_segment)

# Write topic files
for idx, segment in enumerate(segments, start=1):
    output_path = os.path.join(output_dir, f"topic_{idx:02d}.txt")
    with open(output_path, "w", encoding="utf-8") as out:
        for block_index in segment:
            out.write(f"===== {files[block_index]} =====\n")
            out.write(documents[block_index] + "\n\n")

print(f"\n✅ Created {len(segments)} topic segment files in '{output_dir}'")
