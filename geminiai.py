"""
Script to connect to Google Gemini AI API
"""
# Necessary packages are imported
from dotenv import load_dotenv
from google.generativeai as genai
import os

class GeminiAI:
    """
    Class to work with Google's Gemini AI
    """
    def __init__(self, transcript):
        """
        Constructor to declare class variables and constants
        """
        self.transcript = transcript
        self.prompt = "You are a youtube video summarizer. Understand the transcribed text from the video and \
                       generate detailed noted for study purpose  within 250 words. Below is the trancript text \
                       given in triple quotes"
        self.connect_to_genai()
        self.generate_notes()

    def connect_to_genai(self):
        """
        Method to connect to the Google gemini API with the provided API key
        """
        load_dotenv()
        genai.configure(api_key=os.getenv("GOOGLE_GEMINI_AI_API_KEY"))

    def generate_notes(self):
        """
        To allow the gemini AI to generate notes from the transcript extracted earlier
        """
        model = genai.GenerativeModel("gemini-pro")
        self.response = model.generate_content(self.prompt+self.transcript)
        self.genai_notes = self.response.text


