import os
from  dotenv import load_dotenv,find_dotenv
from langchain.llms import OpenAI
from langchain.schema import(
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.chat_models import ChatOpenAI
load_dotenv(find_dotenv(),override=True)


gpt_chat=ChatOpenAI(model='gpt-3.5-turbo',temperature=0.5,max_tokens=1024,openai_api_key=os.environ.get("OPEN_API_KEY"),max_retries=1)
messages=[
    SystemMessage(content="you are modi and respond to my questions like him"),
    HumanMessage(content="What will be the probable economic developments you see next year?")
]

reply=gpt_chat(messages=messages)

print(reply)