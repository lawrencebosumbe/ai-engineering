from langdetect import detect


def detect_language(text: str) -> dict:
    if not text.strip():
        return {
            "language": None,
            "confidence": 0.0
        }

    language = detect(text)

    return {
        "language": language
    }