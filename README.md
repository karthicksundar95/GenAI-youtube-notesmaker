## Gemini YouTube Notes Maker

The idea of this project is to build a notes maker app for the user to 
skip or save time in watching entire YouTube video to understand or take notes for studying
Google's GEMINI ai is used in the application to generate the notes from the YouTube content.
![gemini youtube](https://github.com/user-attachments/assets/6999728a-7ca7-4539-a914-ccebb2be66bf)
### Installation:

> Step 1 : Unzip the entire project 

> Step 2 : create an .env file inside the repo

> Step 3 : Update the file with GOOGLE_GEMINI_AI_API_KEY = '{Enter your Google AI STUDIO api key}'

> Step 4 : Run the main.py file

The above steps will execute the file and generate output on the output display area of the application

### Working

The entire application backend is in python and the front end is developed using
streamlit. 
The control flows from the main.py file. There are separate scripts for YouTube related functions in "YouTube.py"
and the note generation inside "geminiai.py"

The user is prompted with a text box to enter the youtube url they are interested in watching. Then a automatic thumbnail image of the
video is presented on the UI. The url is now taken up by the backend. The youtube.py script has the class methods, that will first analyse the url and extract the video id. 
This video id is then used to display the thumbnail. The url is again now used to connect to YouTube api to extract the content as
text (transcription).

Then the geminiai.py contains the class called GeminiAI, which first set the function of the LLM model to be a note maker
using a prompt message. Then the transcription from the YouTube script is passed on to this and added to the prompt message.
Then we call the summarization functionality of the Gemini AI using api call and the response is displayed for the user.



