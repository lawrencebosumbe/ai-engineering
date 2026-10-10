from mcp.server.mcpserver import MCPServer

from app.services.language_detector import detect_language
from app.services.entity_extractor import EntityExtractor
from app.services.pii_detector import PiiDetector


mcp = MCPServer(
    "Local Language MCP Server",
    instructions=(
        "Provides text analysis tools for language detection, "
        "entity extraction, and PII detection."
    ),
)


entity_extractor = EntityExtractor()
pii_detector = PiiDetector()


@mcp.tool()
def detect_text_language(text: str) -> dict:
    """
    Detect the language of the supplied text.

    Args:
        text: Text to analyze.

    Returns:
        Detected language information.
    """
    return detect_language(text)


@mcp.tool()
def extract_text_entities(text: str) -> list[dict]:
    """
    Extract named entities from text.

    Args:
        text: Text to analyze.

    Returns:
        List of detected entities.
    """
    return entity_extractor.extract(text)


@mcp.tool()
def detect_personal_information(text: str) -> list[dict]:
    """
    Detect personally identifiable information in text.

    Args:
        text: Text to analyze.

    Returns:
        List of detected PII entities.
    """
    return pii_detector.detect(text)


if __name__ == "__main__":
    mcp.run(transport="stdio")