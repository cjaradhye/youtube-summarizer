import os
import json
from vtt_cleaner import clean_vtt_to_paragraph
from summarizer import summarize_transcript

def summarize_all_vtt_in_dir(directory_path: str) -> str:
    """
    Reads all .vtt files in a given directory, cleans their text,
    summarizes them, and returns a JSON string of summaries.

    Parameters:
        directory_path (str): Path to the folder containing .vtt files.

    Returns:
        str: JSON-formatted string of summaries.
    """
    summaries = []

    for filename in os.listdir(directory_path):
        if filename.endswith(".vtt"):
            filepath = os.path.join(directory_path, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                vtt_text = f.read()
            print(filename)
            cleaned_text = clean_vtt_to_paragraph(vtt_text)
            summary = summarize_transcript(cleaned_text)
            
            summaries.append({
                "file": filename,
                "heading": summary["heading"],
                "content": summary["content"]
            })

    return json.dumps(summaries, indent=4)


# Optional: Run directly if executed as script
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python summarize_all_vtt.py <directory_path>")
    else:
        result_json = summarize_all_vtt_in_dir(sys.argv[1])
        print(result_json)