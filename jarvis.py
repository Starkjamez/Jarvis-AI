import os
import speech_recognition as sr
import pyttsx3
from google import genai

# 1. Setup Gemini Client
# Replace 'YOUR_API_KEY' with your actual key
client = genai.Client(api_key="YOUR_API_KEY")

# 2. Setup Voice Engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 175)

def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User: {query}")
        return query
    except Exception:
        return "None"

# --- Main Program ---
if __name__ == "__main__":
    speak("Systems online. How can I help you today?")
    
    while True:
        user_input = listen().lower()

        if "stop" in user_input or "exit" in user_input:
            speak("Powering down. Goodbye.")
            break

        if user_input != "none":
            # Send to Gemini
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=f"Keep the response brief and helpful: {user_input}"
            )
            speak(response.text)

