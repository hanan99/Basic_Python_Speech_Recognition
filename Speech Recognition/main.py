import requests
from api_secrets import API_KEY_ASSEMBLYAI
import sys


# 1. Upload the file that we have locally to AssemblyAI
# https://www.assemblyai.com/docs
upload_endpoint = "https://api.assemblyai.com/v2/upload"
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"

headers = {"authorization": API_KEY_ASSEMBLYAI}
# Get the file name from the terminal tool.
filename = sys.argv[1]


# Read audio file from our local file
# AssemblyAI needed the uploaded files to be in chunks(5MB per chunk).
def upload(filename):
    def read_file(filename, chunk_size=5242880):
        with open(filename, "rb") as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data
    # Post request to upload file to AssemblyAI
    upload_response = requests.post(
        upload_endpoint,
        headers=headers,
        data=read_file(filename)
    )

    audio_url = upload_response.json()["upload_url"]
    return audio_url

# 2. Transcribe function
def transcribe(audio_url):
    transcript_request = {"audio_url": audio_url}

    transcript_response = requests.post(
        transcript_endpoint,
        json=transcript_request,
        headers=headers
    )
   
    job_id = transcript_response.json()['id']
    return job_id

audio_url = upload(filename)
transcript_id = transcribe(audio_url)
print(transcript_id)


# 3. poll
# Keep polling assemblyAI API to see when the transcription is done. 
polling_endpoint = transcript_endpoint + "/" + transcript_id

# 4. save transcription