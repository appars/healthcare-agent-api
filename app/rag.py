# Extremely simple RAG implementation.
# Reads local guidelines and returns matching rules.

from pathlib import Path

GUIDE_FILE = Path("knowledge/clinical_guidelines.md")

def retrieve_guidelines(vitals):
    text = GUIDE_FILE.read_text()
    matches = []

    if vitals.spo2 < 92:
        matches.append("SpO2 below 92% requires urgent evaluation.")
    if vitals.temperature > 102:
        matches.append("Temperature above 102F requires clinical review.")
    if vitals.age > 55:
        matches.append("Age above 55 increases risk.")

    return matches
