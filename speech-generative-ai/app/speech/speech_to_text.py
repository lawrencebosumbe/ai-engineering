import whisper

class SpeechToText:
    def __init__(self, model_name: str = "base"):
        self.model = whisper.load_model(model_name)

    def transcribe(self, audio_file: str) -> str:
        result = self.model.transcribe(audio_file, fp16=False)
        return result["text"].strip()