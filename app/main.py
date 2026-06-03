from fastapi import FastAPI
from pydantic import BaseModel, Field
from app.rag import retrieve_guidelines
from app.agents import risk_agent, recommendation_agent

app = FastAPI(
    title="Healthcare Agent API",
    description="Simple RAG + 2 Agent demo",
    version="1.0"
)

class PatientVitals(BaseModel):
    age: int = Field(..., description="Age in years")
    temperature: float = Field(..., description="Temperature in Fahrenheit")
    spo2: int = Field(..., description="Blood oxygen saturation")

@app.get("/")
def home():
    return {"message": "Healthcare Agent API running"}

@app.post("/assess")
def assess(vitals: PatientVitals):
    # Retrieve relevant guideline text
    guidelines = retrieve_guidelines()

    # Agent 1: Assess risk
    risk = risk_agent(vitals, guidelines)

    # Agent 2: Generate recommendation
    recommendation = recommendation_agent(risk)

    return {
        "patient": vitals.model_dump(),
        "risk_assessment": risk,
        "recommendation": recommendation,
        "guidelines_used": guidelines
    }
