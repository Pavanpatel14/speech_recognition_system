#  Speech Recognition System

A simple **Streamlit-based web application** that allows users to upload an audio file (in `.wav`, `.mp3`, `.flac`, `.m4a`, or `.mpeg` format) and returns a **text transcription** using **Google Speech Recognition**.

---

## Features

- Upload and process multiple audio formats
- Automatic conversion to WAV format (if necessary)
- Speech-to-text transcription using Google Speech Recognition API
- Clean and interactive Streamlit interface

---

##  Tech Stack

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [audioread](https://pypi.org/project/audioread/)
- [wave](https://docs.python.org/3/library/wave.html)
- [tempfile](https://docs.python.org/3/library/tempfile.html), [os](https://docs.python.org/3/library/os.html)

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/speech-recognition-app.git
   cd speech-recognition-app
2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt


## Usage

1. Run the Streamlit app:

  ```bash
     streamlit run app.py
  ```

2. Open your browser and go to the local URL (usually http://localhost:8501)

3. Upload an audio file in one of the supported formats.

4. The app process the first 20 secondsof the audio and returns the transcribed text.



## Supported File Types
.wav

.mp3

.flac

.m4a

.mpeg




  
