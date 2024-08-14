from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from langchain_experimental.agents.agent_toolkits.python.base import create_python_agent
from langchain_experimental.tools.python.tool import PythonREPLTool

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", google_api_key=api_key)


pythonAgent = create_python_agent(
    llm,
    tool=PythonREPLTool(),
    verbose=True
)

def runQuery(query):
    return pythonAgent.run(query)