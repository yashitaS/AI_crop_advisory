from fastapi import FastAPI, HTTPException
from schemas import AdvisoryRequest, CropAdvisory
from crop_agent import generate_advisory

app = FastAPI()

@app.post("/api/advisory", response_model=CropAdvisory)
async def get_advisory(data: AdvisoryRequest):
    try:
        return await generate_advisory(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def health():
    return {"status": "ok"}