import os
from deepgram import DeepgramClient, PrerecordedOptions, FileSource

def transcribe_audio(file_path: str) -> str:
    """
    Transcribes an audio file using Deepgram and returns the transcript text.
    
    Args:
        file_path (str): Path to the audio file (e.g., MP3 or WAV).
    
    Returns:
        str: Transcript text of the audio.
    """
    try:
        deepgram = DeepgramClient()

        with open(file_path, "rb") as file:
            buffer_data = file.read()

        payload: FileSource = {
            "buffer": buffer_data,
        }

        options = PrerecordedOptions(
            model="nova-3",
            smart_format=True,
        )

        response = deepgram.listen.rest.v("1").transcribe_file(payload, options)

        transcript = response.results.channels[0].alternatives[0].transcript
        return transcript

    except Exception as e:
        print(f"Transcription error: {e}")
        return ""

