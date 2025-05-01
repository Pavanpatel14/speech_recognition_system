import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment
from pydub.utils import which
import os
import tempfile

# Set FFmpeg path explicitly (optional if FFmpeg is in PATH)
AudioSegment.converter = which("ffmpeg")
AudioSegment.ffprobe = which("ffprobe")

st.title("🎙️ Speech-to-Text System")

uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "flac"])

if uploaded_file is not None:
    # Create a temporary file to save uploaded audio
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as temp_audio:
        temp_audio.write(uploaded_file.read())
        temp_audio_path = temp_audio.name

    # Prepare output WAV path
    temp_wav_path = temp_audio_path + ".wav"

    try:
        # Convert to WAV if necessary
        file_ext = os.path.splitext(uploaded_file.name)[1].lower()

        if file_ext == ".mp3":
            audio = AudioSegment.from_file(temp_audio_path, format="mp3")
            audio.export(temp_wav_path, format="wav")
        elif file_ext == ".flac":
            audio = AudioSegment.from_file(temp_audio_path, format="flac")
            audio.export(temp_wav_path, format="wav")
        elif file_ext == ".wav":
            temp_wav_path = temp_audio_path  # No conversion needed
        else:
            st.error("Unsupported file type.")
            st.stop()

        # Transcribe the WAV audio
        recognizer = sr.Recognizer()
        with sr.AudioFile(temp_wav_path) as source:
            st.write("Processing audio...")
            audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio_data)
                st.success("Transcription:")
                st.write(text)
            except sr.UnknownValueError:
                st.error("Could not understand the audio.")
            except sr.RequestError as e:
                st.error(f"Google Speech Recognition error: {e}")

    except Exception as e:
        st.error(f"Processing error: {e}")

    finally:
        # Clean up temporary files
        for file_path in [temp_audio_path, temp_wav_path]:
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                except Exception as e:
                    st.warning(f"Couldn't delete temp file: {e}")

st.markdown("###  Example Usage:")
st.markdown("1. Upload a short audio clip (WAV, MP3, or FLAC).")
st.markdown("2. The app will transcribe and display the text.")