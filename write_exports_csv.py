import os
import csv
from vtt_cleaner import clean_vtt_to_paragraph
from summarizer import summarize_transcript

EXPORTS_FILE = "exports.csv"

def write_summaries_to_csv(directory_path: str):
    """
    Reads all .vtt files in a directory, summarizes them,
    and writes the results into exports.csv with columns:
    File Name, Heading, Content. Skips files already processed.
    """
    summaries = []

    # Load already processed file names to avoid duplicates
    existing_files = set()
    if os.path.isfile(EXPORTS_FILE):
        with open(EXPORTS_FILE, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                existing_files.add(row["File Name"])

    # Process .vtt files
    for filename in os.listdir(directory_path):
        if filename.endswith(".vtt") and filename not in existing_files:
            filepath = os.path.join(directory_path, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                vtt_text = f.read()

            cleaned_text = clean_vtt_to_paragraph(vtt_text)
            summary = summarize_transcript(cleaned_text)
            print(filename)
            print(summary)
            summaries.append({
                "File Name": filename,
                "Heading": summary.get("heading", "Invalid response"),
                "Content": summary.get("content", str(summary)),
            })

    # Append summaries to CSV
    if summaries:
        file_exists = os.path.isfile(EXPORTS_FILE)
        with open(EXPORTS_FILE, "a", newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["File Name", "Heading", "Content"])
            if not file_exists:
                writer.writeheader()

            for row in summaries:
                writer.writerow(row)

        print(f"✅ {len(summaries)} summaries written to {EXPORTS_FILE} successfully.")
    else:
        print("⚠️ No new .vtt files to process.")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python write_exports_csv.py <directory_path>")
    else:
        write_summaries_to_csv(sys.argv[1])