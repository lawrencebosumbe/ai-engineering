import app.speech
from app.speech.text_to_speech import TextToSpeech


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tts = TextToSpeech()
    tts.speak("Hello, this is a test of text to speech.")
    tts.save_to_file("Hello, this is a test of text to speech.",
                     "data/audio/tts_output.wav")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
