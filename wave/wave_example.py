# Audio file formats:
# .wav : uncompressed, best audio quality and largest file size. standard for CD audio quality.
# .mp3 : most popular, lossy compression format. during the process of compressing data it can lsoe information.
# .flac : lossless compression format. it alow to perfectly reconstruct the original data.

import wave

# Audio signal parameters
# - number of channels: 1 mono, 2 stereo. this is the number of the independent audio channels. ex: stero gives you the impression that the audio is coming from the 2 different directions.
# - sample width: number of bits per sample.
# - framerate/sample_rate: number of samples per second. 44,100 Hz standard sample rate for CD quality. This means we get 44100 sample values in each second.
# - number of frames: total number of frames we get
# - values of a frame: it's in binary format but we can convert it to a integer value.

# load audio file
obj = wave.open("audio.wav", "rb") 

# get number of channels
print("Number of channels", obj.getnchannels())

# get sample width  
print("Sample width", obj.getsampwidth())

# get frame rate
print("Framerate", obj.getframerate())

# get number of frames  
print("Number of frames", obj.getnframes())

# get a all the parameters
print("Parameters", obj.getparams())


# calculate the time of the audio
t_audio = obj.getnframes() / obj.getframerate()
print("Time of audio", t_audio)

# get the actual frames
frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames))

#closing the file
obj.close()


# To save the data
obj_new = wave.open("audio_new.wav", "wb")
obj_new.setnchannels(2)
obj_new.setsampwidth(2)
obj_new.setframerate(44100)

obj_new.writeframes(frames)

obj_new.close()