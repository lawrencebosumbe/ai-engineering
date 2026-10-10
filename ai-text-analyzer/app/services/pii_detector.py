from presidio_analyzer import AnalyzerEngine


class PIIDetector:

    def __init__(self):
        self.analyzer = AnalyzerEngine()

    def detect(self, text: str):

        results = self.analyzer.analyze(
            text=text,
            language="en"
        )

        return [
            {
                "entity_type": result.entity_type,
                "start": result.start,
                "end": result.end,
                "score": result.score
            }
            for result in results
        ]