# Before running this code, ensure you have FFmpeg installed and accessible from the system path.
# Install required dependencies:
# pip install ffmpeg-python pydub

from pydub import AudioSegment

# Load an audio file (MP3 format) into an AudioSegment object
audio = AudioSegment.from_mp3("audio.wav")

# Increase volume by 6dB
audio = audio + 6
# Repeat the clip
audio = audio * 2
# Apply a fade-in effect over the first 2000 milliseconds
audio = audio.fade_in(2000)

audio.export("mashup.mp3", format="mp3")

# Load the newly exported audio file to confirm the process completed successfully
audio2 = AudioSegment.from_mp3("mashup.mp3")

print("Done!")
