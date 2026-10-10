from app.speech.speech_to_text import SpeechToText


stt = SpeechToText("base")

text = stt.transcribe(
    "data/audio/test.wav"
)

print("Recognized text:")
print(text)