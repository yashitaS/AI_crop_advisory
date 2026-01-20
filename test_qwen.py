from pydantic_ai import Agent
import asyncio

agent = Agent(
    model="ollama:qwen2.5:0.5b",
    system_prompt="Reply ONLY in JSON: {\"test\":\"ok\"}"
)

async def main():
    r = await agent.run("test")
    print("RAW OUTPUT:")
    print(r.output_text)

asyncio.run(main())