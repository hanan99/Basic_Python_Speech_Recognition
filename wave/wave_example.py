import wave

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