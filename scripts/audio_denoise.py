import librosa
import soundfile as sf
import noisereduce as nr

# Load normalized audio
audio, sr = librosa.load(
    "../dataset/processed_audio/podcast_16k_normalized.wav",
    sr=16000
)

# Apply noise reduction
reduced_noise = nr.reduce_noise(y=audio, sr=sr)

# Save cleaned audio
sf.write(
    "../dataset/processed_audio/podcast_16k_cleaned.wav",
    reduced_noise,
    sr
)

print("Noise reduction applied successfully")
