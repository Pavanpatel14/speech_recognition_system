
# Speech Recognition system

A simple Streamlit-based web application that allows users to upload an audio file (in WAV, MP3, FLAC, M4A, or MPEG format) and returns a text transcription using Google Speech Recognition.


## Features


- Upload and process multiple audio formats
- Automatic conversion to WAV format (if necessary)
- Speech-to-text transcription using Google Speech      Recognition API
- Clean and interactive Streamlit interface 

## Tech Stack
- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [audioread](https://pypi.org/project/audioread/)
- [wave](https://docs.python.org/3/library/wave.html)
- [tempfile, os](https://docs.python.org/3/library/tempfile.html)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/speech-recognition-app.git
   cd speech-recognition-app 

2. Create a virtual environment and activate it:
   ```bash
    Copy code
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\act

3. Install dependencies:

```bash
              
 copy code
 pip install -r requirements.txt   
  