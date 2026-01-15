# JARVIS AI 🤖

A voice-interactive AI assistant built with **Python** and **Google Gemini**.

## 🛠️ Tech Stack
- **Language:** Python 3.14
- **AI Engine:** Google GenAI (Gemini 1.5/2.0 Flash)
- **Audio:** PyAudio & SpeechRecognition
- **Voice:** Pyttsx3

## 🚀 Key Features
- **Real-time Listening:** Uses Google Speech API to transcribe user commands.
- **Intelligent Responses:** Connects to Gemini for high-level reasoning and helpful answers.
- **Cross-Platform TTS:** Speaks back to the user through the system's native voice engine.
- **Secure Configuration:** Environment variable integration for API security.

## ⚙️ Setup
1. Install dependencies: `pip install google-genai speechrecognition pyttsx3 pyaudio`
2. Set your `GEMINI_API_KEY` in your `.zshrc`.
3. Run `python3 jarvis.py`.
