import re

def clean_vtt_to_paragraph(vtt_text: str) -> str:
    """
    Takes a WEBVTT-formatted string and returns a cleaned paragraph without timestamps or metadata.
    
    Parameters:
        vtt_text (str): The raw VTT file content as a string.
    
    Returns:
        str: A single paragraph of cleaned transcript text.
    """
    lines = vtt_text.splitlines()

    cleaned_lines = []
    for line in lines:
        if line.strip().lower() == "webvtt":
            continue
        if re.match(r"^\d{2}:\d{2}:\d{2}\.\d{3} -->", line):
            continue
        if re.match(r"^[a-f0-9-]{36}-\d+$", line):
            continue
        if line.strip() == "":
            continue

        cleaned_lines.append(line.strip())

    # Join into one paragraph
    return " ".join(cleaned_lines)
