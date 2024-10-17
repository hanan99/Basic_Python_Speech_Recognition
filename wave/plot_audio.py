import wave
import matplotlib.pyplot as plt
import numpy as np

# Open the audio file in read-binary mode
obj = wave.open("audio.wav", "rb")

# Extract the sample frequency (frames per second) of the audio
sample_freq = obj.getframerate()
# Get the total number of audio frames (samples)
n_samples = obj.getnframes()
# Read the audio frames (entire signal)
signal_wave = obj.readframes(-1)

# Close the wave file after reading the necessary data
obj.close()

# Calculate the total duration of the audio in seconds
t_audio = n_samples/sample_freq

print("Audio length: ", t_audio, "seconds")

# Convert the raw audio data (byte buffer) into a NumPy array of 16-bit integers
signal_array = np.frombuffer(signal_wave, dtype=np.int16)

# Check if the audio is stereo (2 channels)
if obj.getnchannels() == 2:
    # Reshape to (n_samples, 2) for stereo audio
    signal_array = signal_array.reshape(-1, 2)
    # Extract the first channel (e.g., left channel) for plotting
    signal_array = signal_array[:, 0]

# Generate a time axis (in seconds) for the audio, equally spaced over the number of samples
times = np.linspace(0, t_audio, num=n_samples)

# Create a figure to visualize the audio signal
plt.figure(figsize=(15, 5))
# Plot the audio signal (amplitude vs. time)
plt.plot(times, signal_array)
plt.title("Audio Signal")
plt.ylabel("signal wave")
plt.xlabel("time(s)")
plt.xlim(0, t_audio)

plt.show()




# Instructions for running the code:
# 1. Activate the virtual environment in the terminal:
#    env\Scripts\activate
# 2. Run the Python script:
#    python plot_audio.py

