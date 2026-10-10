from app.services.pii_detector import PIIDetector

detector = PIIDetector()

text = """
John Smith's email is john.smith@example.com
and his phone number is +27 82 123 4567.
"""

print(detector.detect(text))