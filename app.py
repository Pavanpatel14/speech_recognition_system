import streamlit as st
import speech_recognition as sr
import os
import tempfile
import wave
import audioread

st.title("🎙️ Speech Recognition System")

uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "flac", "m4a", "mpeg"])

if uploaded_file is not None:
    # Create a temporary file to save uploaded audio
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as temp_audio:
        temp_audio.write(uploaded_file.read())
        temp_audio_path = temp_audio.name

    try:
        # Check file extension and handle accordingly
        file_ext = os.path.splitext(uploaded_file.name)[1].lower()

        if file_ext == ".wav":
            # Directly process WAV files
            temp_wav_path = temp_audio_path
        elif file_ext in [".mp3", ".flac", ".m4a", ".mpeg"]:
            # Convert MP3, FLAC, M4A, or MPEG to WAV using audioread
            temp_wav_path = temp_audio_path + ".wav"
            with audioread.audio_open(temp_audio_path) as audio_file:
                with wave.open(temp_wav_path, "wb") as wav_file:
                    wav_file.setnchannels(audio_file.channels)
                    wav_file.setsampwidth(2)  # Assuming 16-bit audio
                    wav_file.setframerate(audio_file.samplerate)
                    for buffer in audio_file:
                        wav_file.writeframes(buffer)
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

st.markdown("### Example Usage:")
st.markdown("1. Upload a short audio clip (WAV, MP3, FLAC, M4A, or MPEG).")
st.markdown("2. The app will transcribe and display the text.")