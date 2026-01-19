import whisper

# Load Whisper model (small is fast & accurate)
model = whisper.load_model("small")

# Path to one audio chunk
audio_path = "../dataset/processed_audio/chunks/audio_001.wav"

# Transcribe audio
result = model.transcribe(audio_path, fp16=False)

# Print full text
print("Transcription:")
print(result["text"])

# Print timestamps
print("\nSegments with timestamps:")
for segment in result["segments"]:
    print(f"[{segment['start']:.2f} - {segment['end']:.2f}] {segment['text']}")
