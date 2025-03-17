import os
import azure.cognitiveservices.speech as speechsdk
from fastapi import FastAPI, File, UploadFile
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# ✅ Add this root route here
@app.get("/")
def home():
    return {"message": "Welcome to the Speech-to-Text API!"}

SPEECH_KEY = os.getenv("SPEECH_KEY")
SPEECH_REGION = os.getenv("SPEECH_REGION")

def recognize_speech_from_audio(audio_path):
    speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
    audio_config = speechsdk.AudioConfig(filename=audio_path)

    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    result = speech_recognizer.recognize_once()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return result.text
    else:
        return "Speech not recognized"

@app.post("/speech-to-text/")
async def speech_to_text(audio: UploadFile = File(...)):
    file_path = f"temp_{audio.filename}"
    with open(file_path, "wb") as buffer:
        buffer.write(audio.file.read())

    text = recognize_speech_from_audio(file_path)
    os.remove(file_path)  # Clean up the temp file

    return {"transcription": text}

