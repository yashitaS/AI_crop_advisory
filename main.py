from fastapi import FastAPI, HTTPException
from agent.crop_agent import generate_advisory
from schemas import AdvisoryRequest, CropAdvisory

app = FastAPI()

@app.post("/api/advisory", response_model=CropAdvisory)
async def get_advisory(data: AdvisoryRequest):
    try:
        return await generate_advisory(data)
    except Exception as e:
        print("ERROR:", e)
        raise HTTPException(status_code=500, detail="AI error")

@app.get("/")
def health():
    return {"status": "ok"}
