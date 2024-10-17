import sys
from api_communication import *

# https://www.assemblyai.com/docs
# Get the file name from the terminal tool.
filename = sys.argv[1]



audio_url = upload(filename)
save_transcript(audio_url, filename)