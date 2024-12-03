import yt_dlp as youtube_dl

# We set up an instance of the YoutubeDL class
ydl = youtube_dl.YoutubeDL()

# Now we want to download a video and extract its information
def get_video_infos(url):
    with ydl:
        result = ydl.extract_info(url, download=False)
        # download=False means that we don't want to download the video
    
    if "entries" in result:
        # A playlist was provided
        return result["entries"][0]
    
    return result

# Gets the video infos
def get_audio_url(video_info):
    for f in video_info["formats"]:
        if f["ext"] == "m4a":
            return f["url"]


if __name__ == "__main__":

    video_info = get_video_infos("https://www.youtube.com/watch?v=e-kSGNzu0hM")
    audio_url = get_audio_url(video_info)
    print(audio_url)
