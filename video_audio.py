from moviepy.editor import VideoFileClip

video = VideoFileClip("./material/videos/input_video.mp4")
audio = video.audio

audio.write_audiofile("./material/audios/output_audio.mp3")

audio.close()
video.close()