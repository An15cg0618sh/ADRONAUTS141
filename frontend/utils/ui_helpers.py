import speech_recognition as sr
import streamlit as st
import time

def voice_input():
    """Capture voice input and convert to text using Google Speech Recognition."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("🎤 Listening... Please speak clearly.")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Could not understand audio."
        except sr.RequestError:
            return "Could not connect to the speech recognition service."

def display_loading(text="Loading...", seconds=2):
    """Simple loading animation placeholder for Streamlit."""
    with st.spinner(text):
        time.sleep(seconds)

def display_metrics(metrics: dict):
    """Display metrics in a neat horizontal row (used for admin dashboard)."""
    cols = st.columns(len(metrics))
    for (key, value), col in zip(metrics.items(), cols):
        col.metric(label=key, value=value)
