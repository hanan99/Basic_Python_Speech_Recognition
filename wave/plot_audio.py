import wave
import matplotlib.pyplot as plt
import numpy as np

obj = wave.open("audio.wav", "rb")

sample_freq = obj.getframerate()
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1)

obj.close()

# calculate the length of the signal per second
t_audio = n_samples/sample_freq

print("Audio length: ", t_audio, "seconds")

signal_array = np.frombuffer(signal_wave, dtype=np.int16)

# If the audio has multiple channels, reshape the array
if obj.getnchannels() == 2:
    # Reshape to (n_samples, 2) for stereo audio
    signal_array = signal_array.reshape(-1, 2)
    # Use only one channel (e.g., left channel) for plotting
    signal_array = signal_array[:, 0]

times = np.linspace(0, t_audio, num=n_samples)

plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title("Audio Signal")
plt.ylabel("signal wave")
plt.xlabel("time(s)")
plt.xlim(0, t_audio)
plt.show()






# To run the code you should run it in the terminal new environment, use these codes in termunal:
# env\Scripts\activate
# then python plot_audio.py

# When you're done, you can deactivate the virtual environment by running:
# deactivate

