from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_groq import ChatGroq
from langchain.messages import HumanMessage
from tavily import TavilyClient
from typing import Dict, Any
import logging

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s | %(levelname)s | %(message)s"
)

load_dotenv()

tavily = TavilyClient()


@tool
def web_search(query : str) -> Dict[str, Any]:
    """ tool for searching on the web"""
    logging.info(f"searching for {query}")
    return tavily.search(query)

# model = ChatGroq(model="openai/gpt-oss-120b",
#                 temperature = 1.0)

# agent = create_agent(model=model,
#                      tools = [web_search])

# response = agent.invoke(
#     {"messages": [HumanMessage(content="give me the latest news of the day")]}
# )

# print(response["messages"])

# print(response["messages"][-1].content)