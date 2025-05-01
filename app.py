import streamlit as st
import speech_recognition as sr
import os
import tempfile
import wave
import audioread

# Title of the Streamlit app
st.title("🎙️ Speech Recognition System")

# File uploader to allow users to upload audio files
uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "flac", "m4a", "mpeg"])

if uploaded_file is not None:
    # Create a temporary file to save the uploaded audio
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as temp_audio:
        temp_audio.write(uploaded_file.read())  # Write the uploaded file's content to the temporary file
        temp_audio_path = temp_audio.name  # Get the path of the temporary file

    try:
        # Determine the file extension of the uploaded file
        file_ext = os.path.splitext(uploaded_file.name)[1].lower()

        if file_ext == ".wav":
            # If the file is already in WAV format, no conversion is needed
            temp_wav_path = temp_audio_path
        elif file_ext in [".mp3", ".flac", ".m4a", ".mpeg"]:
            # Convert MP3, FLAC, M4A, or MPEG files to WAV format using audioread
            temp_wav_path = temp_audio_path + ".wav"
            with audioread.audio_open(temp_audio_path) as audio_file:
                with wave.open(temp_wav_path, "wb") as wav_file:
                    wav_file.setnchannels(audio_file.channels)  # Set the number of audio channels
                    wav_file.setsampwidth(2)  # Set sample width (16-bit audio)
                    wav_file.setframerate(audio_file.samplerate)  # Set the sample rate
                    for buffer in audio_file:
                        wav_file.writeframes(buffer)  # Write audio frames to the WAV file
        else:
            # If the file type is unsupported, display an error message
            st.error("Unsupported file type.")
            st.stop()

        # Initialize the speech recognizer
        recognizer = sr.Recognizer()
        with sr.AudioFile(temp_wav_path) as source:
            st.write("Processing audio...")  # Inform the user that the audio is being processed
            audio_data = recognizer.record(source, duration=20)  # Record the first 20 seconds of the audio

            try:
                # Use Google Speech Recognition to transcribe the audio
                text = recognizer.recognize_google(audio_data)
                st.success("Transcription:")  # Display the transcription result
                st.write(text)
            except sr.UnknownValueError:
                # Handle cases where the audio could not be understood
                st.error("Could not understand the audio.")
            except sr.RequestError as e:
                # Handle errors related to the Google Speech Recognition API
                st.error(f"Google Speech Recognition API error: {e}")

    except Exception as e:
        # Handle any other exceptions that occur during processing
        st.error(f"Processing error: {e}")

    finally:
        # Clean up temporary files to avoid clutter
        for file_path in [temp_audio_path, temp_wav_path]:
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)  # Delete the temporary file
                except Exception as e:
                    st.warning(f"Couldn't delete temp file: {e}")  # Warn the user if a file couldn't be deleted

# Provide usage instructions for the app
st.markdown("### Example Usage:")
st.markdown("1. Upload a short audio clip (WAV, MP3, FLAC, M4A, or MPEG).")
st.markdown("2. The app will transcribe and display the text.")
