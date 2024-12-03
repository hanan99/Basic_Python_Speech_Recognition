# Here we combine the yt_extract infos with assembly AI and extract the transcript of the videos and also the sentiment classification result
# https://www.assemblyai.com/
# https://www.assemblyai.com/docs/audio-intelligence/sentiment-analysis

import json
from yt_extractor import get_video_infos, get_audio_url
from api import save_transcript

def save_video_sentiment(url):
    video_infos = get_video_infos(url)
    audio_url = get_audio_url(video_infos)
    title = video_infos["title"]
    # remove leading and trailing spaces from the title
    title = title.strip().replace(" ", "_")
    # We want to store it in a different folder
    title = "data/" + title 
    save_transcript(audio_url, title, sentiment_analysis=True)