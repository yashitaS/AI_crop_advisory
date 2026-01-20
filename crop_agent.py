from pydantic_ai import Agent
from schemas import CropAdvisory

crop_agent = Agent(
    model="groq:llama3-8b-8192",
    system_prompt="""
You are an expert Indian agricultural advisory AI.

Give advice under:
- Crop Stage
- Irrigation
- Fertilizer
- Pest & Disease Risk
- Yield Tips
"""
)

async def generate_advisory(data):
    result = await crop_agent.run(
        f"Crop: {data.crop}, Location: {data.location}, Soil: {data.soil_type}, Goal: {data.goal}"
    )
    return CropAdvisory(
        crop_stage=result.output_text,
        irrigation=[],
        fertilizer=[],
        risk=[],
        tips=[]
    )
