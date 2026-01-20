from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import asyncio

from agent.crop_agent import generate_advisory
from agent.schemas import CropAdvisory

app = FastAPI(title="AI Smart Crop Advisory")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for local testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AdvisoryRequest(BaseModel):
    crop: str
    location: str
    soil_type: str
    goal: Optional[str] = "high yield"

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/api/advisory", response_model=CropAdvisory)
async def get_advisory(data: AdvisoryRequest):
    prompt = f"""
You are an expert Indian agricultural advisory AI.

Crop: {data.crop}
Location: {data.location}
Soil Type: {data.soil_type}
Goal: {data.goal}

Give practical, India-specific farming advice.
"""

    try:
        return await generate_advisory(prompt)
    except Exception as e:
        print("ERROR:", repr(e))
        raise HTTPException(status_code=500, detail="Advisory generation failed")
