import os

input_dir = "../dataset/transcripts"
output_dir = "../dataset/merged_transcripts"

os.makedirs(output_dir, exist_ok=True)

files = sorted([f for f in os.listdir(input_dir) if f.endswith(".txt")])

window_size = 5
block_num = 1

for i in range(0, len(files), window_size):
    merged_text = ""

    for f in files[i:i+window_size]:
        with open(os.path.join(input_dir, f), "r", encoding="utf-8") as file:
            merged_text += file.read() + "\n"

    output_file = f"block_{block_num:03d}.txt"
    with open(os.path.join(output_dir, output_file), "w", encoding="utf-8") as out:
        out.write(merged_text)

    print(f"Created {output_file}")
    block_num += 1

print("\n✅ Transcript merging completed!")
