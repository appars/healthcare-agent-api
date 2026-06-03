"""
rag.py

Simple RAG implementation.

Version 2:
Read guidelines from a knowledge file.

Future:
Replace with FAISS + Embeddings.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

GUIDE_FILE = BASE_DIR / "knowledge" / "clinical_guidelines.md"


def retrieve_guidelines():

    with open(GUIDE_FILE, "r") as file:
        guidelines = file.read()

    return guidelines
