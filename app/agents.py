"""
agents.py

Two-Agent Workflow

1. Risk Assessment Agent
2. Recommendation Agent
"""

import json

from app.llm import llm


def risk_agent(vitals, guidelines):

    prompt = f"""
You are a healthcare risk assessment agent.

Patient Information:

Age: {vitals.age}
Temperature: {vitals.temperature}
SpO2: {vitals.spo2}

Clinical Guidelines:

{guidelines}

Determine the risk level.

Return ONLY JSON.

Example:

{{
  "risk": "HIGH",
  "confidence": 0.92
}}
"""

    response = llm.invoke(prompt)

    return json.loads(response.content)


def recommendation_agent(risk_result):

    prompt = f"""
You are a healthcare recommendation agent.

Risk Assessment:

{risk_result}

Provide a recommendation.

Return ONLY JSON.

Example:

{{
  "priority":"URGENT",
  "action":"Seek medical evaluation within 24 hours"
}}
"""

    response = llm.invoke(prompt)

    return json.loads(response.content)
