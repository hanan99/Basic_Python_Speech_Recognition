# How we can record with our mic and capture with our mic input in python
# For this we use PyAudio

import pyaudio
import wave

FRAMES_PER_BUFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=FRAMES_PER_BUFER
                )

print("recording")
seconds = 5
frames = []
for i in range (0, int(RATE/FRAMES_PER_BUFER*seconds)):
    data = stream.read(FRAMES_PER_BUFER)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

obj = wave.open("output.wav", 'wb')
obj.setnchannels(CHANNELS)
obj.setsampwidth(p.get_sample_size(FORMAT))
obj.setframerate(RATE)
# This would combine all the elements in our frames list into a binary string
obj.writeframes(b''.join(frames))

obj.close()