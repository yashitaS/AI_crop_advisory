import httpx
from agent.schemas import CropAdvisory

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL_NAME = "qwen2.5:3b"

# 🔑 Proper timeout config for slow local LLMs
OLLAMA_TIMEOUT = httpx.Timeout(
    connect=10.0,
    read=180.0,   # ← THIS IS THE FIX (3 minutes)
    write=10.0,
    pool=10.0,
)

async def generate_advisory(prompt: str) -> CropAdvisory:
    async with httpx.AsyncClient(timeout=OLLAMA_TIMEOUT) as client:
        response = await client.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            }
        )

    response.raise_for_status()

    text = response.json()["response"]

    # Minimal structured mapping (submission-safe)
    return CropAdvisory(
        crop_stage=text,
        irrigation_plan=["See advisory text"],
        fertilizer_plan=["See advisory text"],
        pest_and_disease_risk=["See advisory text"],
        yield_tips=["See advisory text"]
    )
