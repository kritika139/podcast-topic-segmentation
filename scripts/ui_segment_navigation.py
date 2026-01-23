import streamlit as st
import os

# ---------- PATH CONFIG ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(BASE_DIR, "..", "dataset")

SEGMENTS_DIR = os.path.join(DATASET_DIR, "topic_segments_baseline")
SUMMARIES_DIR = os.path.join(DATASET_DIR, "topic_summaries")
KEYWORDS_DIR = os.path.join(DATASET_DIR, "topic_keywords")

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Podcast Segment Navigator",
    layout="wide"
)

st.title("Podcast Segment Navigator")
st.caption("Browse podcast segments by topic, summary, and keywords")


def load_segments():
    segments = []

    for file in sorted(os.listdir(SEGMENTS_DIR)):
        if not file.endswith(".txt"):
            continue

        segment_id = file.replace(".txt", "")

        with open(os.path.join(SEGMENTS_DIR, file), encoding="utf-8") as f:
            text = f.read().strip()

        summary_file = f"{segment_id}_summary.txt"
        summary_path = os.path.join(SUMMARIES_DIR, summary_file)
        summary = ""
        if os.path.exists(summary_path):
            summary = open(summary_path, encoding="utf-8").read().strip()

        keyword_file = f"{segment_id}_keywords.txt"
        keyword_path = os.path.join(KEYWORDS_DIR, keyword_file)
        keywords = ""
        if os.path.exists(keyword_path):
            keywords = open(keyword_path, encoding="utf-8").read().strip()

        title = summary.split(".")[0] if summary else segment_id.replace("_", " ").title()

        segments.append({
            "id": segment_id,
            "title": title,
            "summary": summary,
            "keywords": keywords,
            "text": text
        })

    return segments




segments = load_segments()

# ---------------- SIDEBAR ----------------
st.sidebar.header("Topics")

topic_titles = [seg["title"] for seg in segments]
selected_title = st.sidebar.radio(
    label="Select a segment",
    options=topic_titles
)

selected_segment = next(
    seg for seg in segments if seg["title"] == selected_title
)

# ---------------- MAIN CONTENT ----------------
left, right = st.columns([2, 3])

with left:
    st.subheader("Summary")
    if selected_segment["summary"]:
        st.info(selected_segment["summary"])
    else:
        st.write("No summary available.")

    st.subheader("Keywords")
    if selected_segment["keywords"]:
        st.write(selected_segment["keywords"])
    else:
        st.write("No keywords available.")

with right:
    st.subheader("Transcript")
    st.text_area(
        label="",
        value=selected_segment["text"],
        height=500,
        disabled=True
    )
