from pathlib import Path

from app.speech.speech_to_text import SpeechToText


def test_speech_to_text():
    audio_file = Path("data/audio/test.wav")

    stt = SpeechToText("base")

    text = stt.transcribe(str(audio_file))

    assert isinstance(text, str)
    assert len(text) > 0