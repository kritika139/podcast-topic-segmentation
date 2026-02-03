from pydub import AudioSegment
from pydub.effects import normalize

# Load 16kHz WAV audio
audio = AudioSegment.from_wav("../dataset/processed_audio/podcast_16k.wav")

# Normalize audio volume
normalized_audio = normalize(audio)

# Export normalized audio
normalized_audio.export(
    "../dataset/processed_audio/podcast_16k_normalized.wav",
    format="wav"
)

print("Audio normalized successfully")
