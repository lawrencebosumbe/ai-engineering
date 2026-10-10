from json import tool

from spacy.cli import project

[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "ai-text-analyzer"
version = "0.1.0"
description = "Azure + local LLM text analysis lab"
requires-python = ">=3.10"
dependencies = [
    # keep this empty or mirror your requirements.txt — your choice
]

[tool.setuptools.packages.find]
where = ["."]
include = ["app*"]
exclude = ["data*", "source*", "notebooks*", "tests*"]

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["."]