# Two simple agents.
# These are intentionally lightweight and easy to understand.

def risk_agent(vitals, guidelines):
    risk = "LOW"
    confidence = 0.75

    if vitals.temperature > 102 or vitals.spo2 < 92:
        risk = "HIGH"
        confidence = 0.92
    elif vitals.temperature > 99 or vitals.spo2 < 95:
        risk = "MODERATE"
        confidence = 0.82

    return {
        "risk": risk,
        "confidence": confidence
    }

def recommendation_agent(risk_result):
    risk = risk_result["risk"]

    if risk == "HIGH":
        return {
            "priority": "URGENT",
            "action": "Seek medical evaluation within 24 hours"
        }

    if risk == "MODERATE":
        return {
            "priority": "MEDIUM",
            "action": "Monitor symptoms and consult a clinician"
        }

    return {
        "priority": "LOW",
        "action": "Continue routine monitoring"
    }
