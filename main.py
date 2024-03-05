"""
Main script that controls the flow from youtube API call, extracting the transcript and getting output from
Gemini AI API
"""
# Necessary packages are imported
import streamlit as st
from youtube import *
from geminiai import *

# Streamlit title for the Html page is added
st.title("Gen AI study notes creator for youtube videos")

# Requesting user to input youtube url
youtube_url = st.text_input("Enter the YouTube link:")

# To extract the video id and display the thumbnail
if youtube_url:
    yt = YouTube(youtube_url)
    video_id = yt.video_id
    st.image(f'http://img.youtube.com/vi/{video_id}/0.jog', use_column_width=True)

# To extract the transcript and then generate notes using Google Gemini AI
if st.button("Get Study Notes"):
    try:
        transcript_text = yt.transcript_text
    except Exception as e:
        raise e
    if transcript_text:
        genai = GeminiAI(transcript_text)
        st.markdown(" Study notes is as follows:")
        st.write(genai.genai_notes)