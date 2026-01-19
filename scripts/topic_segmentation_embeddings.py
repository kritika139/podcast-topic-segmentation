import os
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

input_dir = "../dataset/merged_transcripts"
output_dir = "../dataset/topic_segments_embeddings"

os.makedirs(output_dir, exist_ok=True)

files = sorted([f for f in os.listdir(input_dir) if f.endswith(".txt")])

documents = []
for f in files:
    with open(os.path.join(input_dir, f), "r", encoding="utf-8") as file:
        documents.append(file.read())

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create embeddings
embeddings = model.encode(documents)

# Similarity between consecutive blocks
similarities = []
for i in range(len(embeddings) - 1):
    sim = cosine_similarity(
        embeddings[i].reshape(1, -1),
        embeddings[i + 1].reshape(1, -1)
    )[0][0]
    similarities.append(sim)

threshold = np.mean(similarities)

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

print(f"\n✅ Embedding-based segmentation created {len(segments)} topics")
