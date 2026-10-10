import spacy


def test_spacy_model_loads():
    nlp = spacy.load("en_core_web_sm")

    assert nlp is not None


def test_spacy_can_extract_entities():
    nlp = spacy.load("en_core_web_sm")

    doc = nlp("Microsoft is located in Redmond.")

    entities = [(entity.text, entity.label_) for entity in doc.ents]

    assert ("Microsoft", "ORG") in entities
    assert ("Redmond", "GPE") in entities