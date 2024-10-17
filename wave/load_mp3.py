# Should install ffmpeg first
# pip install ffmpeg-python

from pydub import AudioSegment

audio = AudioSegment.from_mp3("audio.wav")

# increase volume by 6dB
audio = audio + 6
# repeat the clips
audio = audio * 2
# fade in 2000ms
audio = audio.fade_in(2000)

audio.export("mashup.mp3", format="mp3")

audio2 = AudioSegment.from_mp3("mashup.mp3")
print("Done!")
