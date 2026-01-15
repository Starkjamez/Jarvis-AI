import os
import speech_recognition as sr
import pyttsx3
from google import genai

# 1. Setup Gemini Client using your Environment Variable
# This looks for the "GEMINI_API_KEY" you added to your .zshrc
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY not found in environment variables.")
    print("Please run: echo 'export GEMINI_API_KEY=\"your_key\"' >> ~/.zshrc && source ~/.zshrc")
    exit()

client = genai.Client(api_key=api_key)

# 2. Setup Voice Engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# Set to voices[1].id for a female voice if available on your Mac
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)

def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 0.8  # Slight speed up for better response
        r.adjust_for_ambient_noise(source, duration=1)
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

        # Commands to stop the program
        if "stop" in user_input or "exit" in user_input or "goodbye" in user_input:
            speak("Powering down. Goodbye.")
            break

        if user_input != "none":
            try:
                # Send the voice command to Gemini
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=f"You are Jarvis, a helpful AI assistant. Keep responses brief: {user_input}"
                )
                speak(response.text)
            except Exception as e:
                print(f"AI Error: {e}")
                speak("I'm having trouble connecting to my brain right now.")
