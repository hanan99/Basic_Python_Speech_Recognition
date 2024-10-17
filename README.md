# Needed websites:
https://www.assemblyai.com/ 

https://www.assemblyai.com/docs 

https://people.csail.mit.edu/hubert/pyaudio/ 


# Some information for wave folder projects:
Audio file formats:
- .wav : uncompressed, best audio quality and largest file size. standard for CD audio quality.
- .mp3 : most popular, lossy compression format. during the process of compressing data it can lsoe information.
- .flac : lossless compression format. it alow to perfectly reconstruct the original data.

# Audio signal parameters
- number of channels: 1 mono, 2 stereo. this is the number of the independent audio channels. ex: stero gives you the impression that the audio is coming from the 2 different directions.
- sample width: number of bits per sample.
- framerate/sample_rate: number of samples per second. 44,100 Hz standard sample rate for CD quality. This means we get 44100 sample values in each second.
- number of frames: total number of frames we get
- values of a frame: it's in binary format but we can convert it to a integer value.
