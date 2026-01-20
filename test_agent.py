import asyncio
from potpie.backend.crop_agent import crop_agent

async def main():
    result = await crop_agent.run(
        user_prompt={
            "crop": "rice",
            "location": "Chennai",
            "soil_type": "clayey",
            "goal": "high yield"
        }
    )
    print(result.output)

if __name__ == "__main__":
    asyncio.run(main())