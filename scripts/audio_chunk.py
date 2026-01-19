from pydub import AudioSegment, silence
import os

# Load cleaned audio
audio = AudioSegment.from_wav(
    "../dataset/processed_audio/podcast_16k_cleaned.wav"
)

# Remove long silences
trimmed_audio = silence.split_on_silence(
    audio,
    min_silence_len=1000,      # 1 second
    silence_thresh=-40,        # silence threshold in dB
    keep_silence=300
)

# Combine non-silent chunks
processed_audio = sum(trimmed_audio)

# Create chunks directory if not exists
chunk_dir = "../dataset/processed_audio/chunks"
os.makedirs(chunk_dir, exist_ok=True)

# Chunk length (25 seconds)
chunk_length_ms = 25 * 1000

# Split into chunks
for i in range(0, len(processed_audio), chunk_length_ms):
    chunk = processed_audio[i:i + chunk_length_ms]
    chunk.export(
        f"{chunk_dir}/chunk_{i//chunk_length_ms:03d}.wav",
        format="wav"
    )

print("Audio trimmed and chunked successfully")
