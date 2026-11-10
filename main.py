from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from tools import web_search
from prompt import SYSTEM_CHEF_PROMPT , CHEF_PROMPT
from decoder_image import choose_image_file, build_image_message




model = ChatGroq(model="qwen/qwen3.8-27b",
                  temperature=1.0)

agent = create_agent(model = model,
                     tools = [web_search],
                     system_prompt=SYSTEM_CHEF_PROMPT)

image_path = choose_image_file()
message = build_image_message(image_path, CHEF_PROMPT)

response = agent.invoke(
    {"messages" : message}
)

print(response["messages"][-1].content)

# if __name__ == "__main__":
#     main()
