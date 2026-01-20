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
    result = await crop_agent.run(data.prompt)
    return CropAdvisory(advisory=result.output_text)