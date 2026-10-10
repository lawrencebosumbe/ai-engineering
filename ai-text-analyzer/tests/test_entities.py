import pytest

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.services.entity_extractor import EntityExtractor


@pytest.fixture
def extractor():
    return EntityExtractor()


def test_extract_person(extractor):
    text = "John Smith works at Microsoft."

    entities = extractor.extract(text)

    assert any(
        entity["text"] == "John Smith"
        and entity["type"] == "PERSON"
        for entity in entities
    )


def test_extract_organization(extractor):
    text = "Microsoft is headquartered in Redmond."

    entities = extractor.extract(text)

    assert any(
        entity["text"] == "Microsoft"
        and entity["type"] == "ORG"
        for entity in entities
    )


def test_extract_location(extractor):
    text = "John lives in Pretoria."

    entities = extractor.extract(text)

    assert any(
        entity["text"] == "Pretoria"
        and entity["type"] == "GPE"
        for entity in entities
    )


def test_empty_text(extractor):
    entities = extractor.extract("")

    assert entities == []