from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import asyncio

load_dotenv()

# os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["math_server.py"],
                "transport": "stdio"
            },
            "weather": {
                # "command": "python",
                # "args": ["weather_server.py"],
                "url": "http://localhost:8000/mcp/",
                "transport": "streamable_http"
            }
        }
    )
    # await client.connect()
    tools = await client.get_tools()
    model = ChatOpenAI(model="gpt-4.1")
    agent = create_react_agent(model,tools)

    # query = await agent.ainvoke({
    #     "messages": [{"role": "user", "content": "what is sum of 1 and 333"}]
    # })
    # print(query['messages'][-1].content)


    queryy = await agent.ainvoke({
        "messages": [{"role":"user", "content":"What is the weather in Bangalore"}]
    })
    print(queryy['messages'][-1].content)

if __name__ == "__main__":
    asyncio.run(main())