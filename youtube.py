"""
Script to work with youtube api and to extract the video content transcript
"""
# Necessary packages are imported
from youtube_transcript_api import YouTubeTranscriptApi

class YouTube:
    """
    Class to handle and process youtube content
    """
    def __init__(self, yt_url):
        """
        Constructor to declare variable and run the transcription process
        :param yt_url:
        """
        self.youtube_url = yt_url
        self.get_youtube_video_id(self.youtube_url)
        self.extract_youtube_transcript()

    def get_youtube_video_id(self):
        """
        Method to extract the video id from the user provided youtube url
        """
        self.video_id = self.youtube_url.split("=")[1]

    def extract_youtube_transcript(self):
        """
        Method to extract the transcription from the requested video
        """
        response = YouTubeTranscriptApi.get_transcript(self.video_id)
        self.transcript_text = ""
        for i in response:
            self.transcript_text += " " + i['text']
