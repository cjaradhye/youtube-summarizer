import os
import subprocess

def convert_videos_to_audio(directory_path):
    """
    Converts all .mp4 files in a directory to .mp3 using ffmpeg.
    Output files are saved in the same directory with the same base name.
    """
    if not os.path.isdir(directory_path):
        raise NotADirectoryError(f"{directory_path} is not a valid directory.")

    for filename in os.listdir(directory_path):
        if filename.lower().endswith(".mp4"):
            input_path = os.path.join(directory_path, filename)
            output_filename = os.path.splitext(filename)[0] + ".mp3"
            output_path = os.path.join(directory_path, output_filename)

            print(f"Converting: {input_path} -> {output_path}")
            try:
                subprocess.run(
                    ["ffmpeg", "-i", input_path, output_path],
                    check=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
            except subprocess.CalledProcessError as e:
                print(f"❌ Failed to convert {filename}: {e.stderr.decode()}")

    print("✅ Conversion complete.")

convert_videos_to_audio("./material/audios")
