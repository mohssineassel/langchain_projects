from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b",
                 temperature=1.0)

agent = create_agent(model=model,
                     checkpointer=InMemorySaver())

config = {"configurable" : {"thread_id":"1"}}

response = agent.invoke(
    {"messages" : [HumanMessage(content="My favorite color is blue")]},
    config   
)

print(response["messages"][-1].content)

response = agent.invoke(
    {"messages" : [HumanMessage(content="what is my favorite color")]},
    config
)

print(response["messages"][-1].content)