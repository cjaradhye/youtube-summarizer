from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound, VideoUnavailable

video_id = "MCks7E4Qa6k"

try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    full_text = " ".join(entry['text'] for entry in transcript)
    print(full_text)
except TranscriptsDisabled:
    print("❌ Transcripts are disabled for this video.")
except NoTranscriptFound:
    print("❌ No transcript available (might be auto-captions only or region-restricted).")
except VideoUnavailable:
    print("❌ The video is unavailable or private.")
except Exception as e:
    print(f"❌ Unexpected error: {e}")


