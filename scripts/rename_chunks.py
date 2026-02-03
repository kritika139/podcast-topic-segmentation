import os

chunk_folder = "../dataset/processed_audio/chunks"

files = sorted([f for f in os.listdir(chunk_folder) if f.endswith(".wav")])

for i, filename in enumerate(files, start=1):
    old_path = os.path.join(chunk_folder, filename)
    new_name = f"audio_{i:03d}.wav"
    new_path = os.path.join(chunk_folder, new_name)
    os.rename(old_path, new_path)

print("All chunks renamed successfully")
