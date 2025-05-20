import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import requests
import re
import dotenv
import os
dotenv.load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

st.set_page_config(page_title="YouTube Summarizer", layout="centered")
st.title("YouTube Video Summarizer")
st.write("Paste a YouTube link below to get an AI-generated summary.")

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer " + HF_TOKEN}

def summarize_text(text, max_chunk_length=900):
    chunks = [text[i:i+max_chunk_length] for i in range(0, len(text), max_chunk_length)]
    summaries = []

    for chunk in chunks:
        chunk = "Summarize this youtube video transcript in less than 20 words in a professional way: " + chunk
        response = requests.post(API_URL, headers=headers, json={"inputs": chunk})
        if response.status_code == 200:
            summaries.append(response.json()[0]['summary_text'])
        else:
            summaries.append("[Error summarizing chunk]")
    return " ".join(summaries)

def extract_video_id(url):
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url)
    return match.group(1) if match else None

def fetch_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return " ".join([entry['text'] for entry in transcript])

video_url = st.text_input("🔗 Enter YouTube video URL")

if video_url:
    with st.spinner("Fetching transcript..."):
        try:
            video_id = extract_video_id(video_url)
            transcript = fetch_transcript(video_id)
            st.success("Transcript fetched!")
            st.write("📝 **Transcript (first 1000 characters):**")
            st.write(transcript[:1000] + "..." if len(transcript) > 1000 else transcript)

            # if st.button("⚡ Generate Summary"):
            with st.spinner("Summarizing..."):
                summary = summarize_text(transcript)
                st.success("Summary ready!")
                st.subheader("🧠 AI Summary:")
                st.write(summary)
        except Exception as e:
            st.error(f"Could not fetch transcript: {e}")
