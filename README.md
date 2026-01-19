Automated Podcast Transcription and Topic Segmentation

Project Overview:
This project focuses on preprocessing podcast audio, generating transcripts, and performing topic segmentation for better navigation and understanding.



Week 1 – Day 1 :

- Installed Python and FFmpeg
- Understood basic audio concepts (sample rate, channels)
- Downloaded a podcast audio file
- Verified audio properties using FFmpeg
- Identified need for resampling to 16 kHz mono for ASR compatibility



Week 1 – Day 2:
- Converted MP3 podcast audio to WAV format
- Resampled audio to 16 kHz
- Converted audio to mono channel
- Verified processed audio using FFmpeg



Week 1 – Day 3:
- Normalized podcast audio for consistent loudness
- Applied noise reduction to remove background noise
- Generated cleaned 16kHz mono WAV audio for ASR



Week 1 – Day 4:
- Trimmed long silences from cleaned audio
- Chunked podcast audio into 25-second segments
- Prepared Whisper-ready audio inputs



Week 1 – Day 5:
- Finalized dataset folder structure
- Assigned unique audio IDs to all chunks
- Created metadata file linking audio files
- Prepared dataset for speech-to-text processing



Week 1 – Day 6:
- Studied OpenAI Whisper ASR model
- Transcribed audio chunks into text
- Generated transcripts with start and end timestamps
- Verified transcription accuracy on sample audio files



Week 1 – Day 7:
- Automated transcription for all audio chunks
- Created transcript files corresponding to each audio ID
- Maintained alignment between audio chunks and transcripts
- Completed speech-to-text preprocessing for the dataset



Week 2 – Day 8:
- Performed text cleaning on Whisper-generated transcripts
- Removed filler words and ASR artifacts
- Normalized transcript text while preserving timestamps
- Prepared clean transcripts for topic segmentation



Week 2 – Day 9:
- Split cleaned transcripts into sentence-level units
- Preserved timestamp alignment during segmentation
- Prepared structured text input for topic segmentation algorithms



Week 3 – Day 10:
- Implemented baseline topic segmentation using sentence similarity
- Applied TF-IDF and cosine similarity to detect topic boundaries
- Generated topic-wise segmented transcripts



Week 3 – Day 11:
- Implemented embedding-based topic segmentation
- Used sentence embeddings to capture semantic similarity
- Detected topic boundaries more accurately than baseline

{“Embedding-based topic segmentation performed better because it captures semantic relationships between sentences rather than relying only on word overlap.}


Week 3 – Day 12:
- Compared baseline and embedding-based topic segmentation outputs
- Evaluated topic coherence and boundary quality
- Selected embedding-based approach for downstream processing



Week 3 – Day 13:
- Extracted keywords for each topic segment using TF-IDF
- Removed stopwords to focus on meaningful terms
- Generated topic-wise keyword representations



Week 3 – Day 14:
- Generated short summaries for each topic segment
- Created concise 1–2 sentence descriptions per topic
- Completed transcript-level topic representation
