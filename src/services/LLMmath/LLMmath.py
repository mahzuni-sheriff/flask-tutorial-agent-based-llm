from langchain.agents import load_tools, initialize_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentType
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", google_api_key=api_key)

llmmathtool = load_tools(["llm-math"], llm=llm)
mathAgent = initialize_agent(
    tools=llmmathtool, 
    llm=llm, 
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
    verbose=True
)
def runQuery(query):
    return mathAgent.run(query)