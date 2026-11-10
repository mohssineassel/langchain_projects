from dotenv import load_dotenv
# from langchain.chat_models import init_chat_model
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain.messages import HumanMessage, AIMessage

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b",
                temperature = 1.0)

agent = create_agent(model=model)

for token, metadata in agent.stream(
    {"messages":[HumanMessage(content = "what is the capital of france"),
                 AIMessage(content="paris"),
                 HumanMessage(content="tell me more about it")]},
    stream_mode="messages"
):
    if token.content :
        print(token.content, end="", flush=True)


# response = agent.invoke(
#     {"messages":[HumanMessage(content = "what is the capital of france"),
#                 AIMessage(content="paris"),
#                 HumanMessage(content="tell me more about it")]}
# )

# print(response["messages"][-1].content)