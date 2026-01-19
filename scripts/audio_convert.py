from pydub import AudioSegment

# Load MP3 audio
audio = AudioSegment.from_mp3("../dataset/raw_audio/podcast.mp3")

# Convert to mono
audio = audio.set_channels(1)

# Resample to 16 kHz
audio = audio.set_frame_rate(16000)

# Export as WAV
audio.export("../dataset/processed_audio/podcast_16k.wav", format="wav")

print("MP3 converted to 16kHz mono WAV successfully")
