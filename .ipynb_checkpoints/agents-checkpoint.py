import os
from  dotenv import load_dotenv,find_dotenv
from langchain.llms import OpenAI
from langchain.agents.agent_toolkits import create_python_agent
from langchain.tools.python.tool import PythonREPLTool
from langchain import PromptTemplate
from langchain.chains import LLMChain,SimpleSequentialChain
load_dotenv(find_dotenv(),override=True)

gpt_client = OpenAI(model='text-davinci-003',temperature=0.7,max_tokens=512,openai_api_key=os.environ.get("OPEN_API_KEY"),max_retries=1)

executor = create_python_agent(
    llm=gpt_client,
    tool=PythonREPLTool(),
    verbose=True
)
executor.run('Calculate the square root of factorial of 20 and display ith with 4 decimal points')