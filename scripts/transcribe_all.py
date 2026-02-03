import whisper
import os

# Load model once
model = whisper.load_model("small")

# Paths
audio_dir = "../dataset/processed_audio/chunks"
output_dir = "../dataset/transcripts"

# Create output folder if not exists
os.makedirs(output_dir, exist_ok=True)

# Get all audio files sorted
audio_files = sorted([f for f in os.listdir(audio_dir) if f.endswith(".wav")])

print(f"Found {len(audio_files)} audio files")

# Loop through files
for idx, audio_file in enumerate(audio_files, start=1):
    audio_path = os.path.join(audio_dir, audio_file)
    output_file = os.path.join(output_dir, audio_file.replace(".wav", ".txt"))

    print(f"\n[{idx}/{len(audio_files)}] Transcribing {audio_file}")

    result = model.transcribe(audio_path, fp16=False)

    # Write transcript with timestamps
    with open(output_file, "w", encoding="utf-8") as f:
        for segment in result["segments"]:
            f.write(f"[{segment['start']:.2f} - {segment['end']:.2f}] {segment['text']}\n")

print("\n✅ All files transcribed successfully!")
