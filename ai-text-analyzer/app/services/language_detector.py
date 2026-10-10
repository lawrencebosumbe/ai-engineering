from langdetect import detect
import spacy


def detect_language(text2: str) -> str:
    return detect(text2)

text = "Hello, how are you today?"
text2 = "Bonjour, comment allez-vous aujourd'hui ?"

language = detect_language(text2)

print(language)