from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_qwq import ChatQwen
from langchain_tavily import TavilySearch



llm = ChatQwen(model="qwen3-max")
tools = [TavilySearch()]
agent = create_agent(llm, tools = tools)



def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": HumanMessage(content="search for three job positions for an ai engineer using langchain in linkedin in dublin and list their details")})
    print(result)

if __name__ == "__main__":
    main()
