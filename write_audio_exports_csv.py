import os
import csv
from deepgram_transcriber import transcribe_audio
from summarizer import summarize_transcript

EXPORTS_FILE = "exports.csv"

def write_audio_summaries_to_csv(directory_path: str):
    """
    Scans for .mp3 files in a directory, transcribes, summarizes, and writes to exports.csv
    """
    summaries = []

    # Get list of .mp3 files
    for filename in os.listdir(directory_path):
        if filename.endswith(".mp3"):
            filepath = os.path.join(directory_path, filename)

            print(f"Processing: {filename}")
            paragraph_text = transcribe_audio(filepath)
            if not paragraph_text.strip():
                print(f"Skipping {filename} due to empty transcript.")
                continue
            print(f"Transcription: {paragraph_text}")
            summary = summarize_transcript(paragraph_text)
            print(summary)

            summaries.append({
                "file": filename,
                "heading": summary.get("heading", "Invalid response"),
                "content": summary.get("content", str(summary)),
            })

    # Write to CSV
    file_exists = os.path.isfile(EXPORTS_FILE)

    with open(EXPORTS_FILE, "a", newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["File Name", "Heading", "Content"])

        if not file_exists:
            writer.writeheader()

        for row in summaries:
            writer.writerow({
                "File Name": row["file"],
                "Heading": row["heading"],
                "Content": row["content"],
            })

    print(f"Summaries written to {EXPORTS_FILE} successfully.")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python write_audio_exports_csv.py <directory_path>")
    else:
        write_audio_summaries_to_csv(sys.argv[1])
