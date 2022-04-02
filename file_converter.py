from moviepy.editor import VideoFileClip

location = "D:/Audiost/"

def convert_to_mp3(filename):
    clip = VideoFileClip(location + filename)
    clip.audio.write_audiofile(location + filename[:-4] + ".mp3")
    clip.close()
