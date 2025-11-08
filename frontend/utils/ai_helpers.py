import streamlit as st
import speech_recognition as sr

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
            st.error("Sorry, could not understand audio.")
        except sr.RequestError:
            st.error("Could not request results; check your internet connection.")

def display_loading():
    with st.spinner('Loading...'):
        pass

def display_metrics(metrics):
    cols = st.columns(len(metrics))
    for i, (label, value) in enumerate(metrics.items()):
        cols[i].metric(label, value)