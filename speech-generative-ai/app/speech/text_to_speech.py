import pyttsx3


class TextToSpeech:
    def __init__(self, rate: int = 175, volume: float = 1.0):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", rate)
        self.engine.setProperty("volume", volume)

    def speak(self, text: str) -> None:
        """Speak the text aloud through the default output device."""
        self.engine.say(text)
        self.engine.runAndWait()

    def save_to_file(self, text: str, output_file: str) -> None:
        """Render the text to a WAV file."""
        self.engine.save_to_file(text, output_file)
        self.engine.runAndWait()