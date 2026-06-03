"""
llm.py

Centralized LLM configuration.
All agents will use this model.
"""

from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)
