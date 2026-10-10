from presidio_analyzer import AnalyzerEngine


class PiiDetector:

    def __init__(self):
        self.analyzer = AnalyzerEngine()

    def detect(self, text: str) -> list[dict]:
        results = self.analyzer.analyze(
            text=text,
            language="en"
        )

        return [
            {
                "entity_type": result.entity_type,
                "start": result.start,
                "end": result.end,
                "score": result.score,
                "text": text[result.start:result.end]
            }
            for result in results
        ]