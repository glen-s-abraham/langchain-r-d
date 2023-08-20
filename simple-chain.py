import os
from  dotenv import load_dotenv,find_dotenv
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
load_dotenv(find_dotenv(),override=True)

gpt_chat=ChatOpenAI(model='gpt-3.5-turbo',temperature=0.5,max_tokens=1024,openai_api_key=os.environ.get("OPEN_API_KEY"),max_retries=1)

template = '''You are a financial expert.Write an opition about the company {company}.'''

prompt = PromptTemplate(
    input_variables=['company'],
    template=template
)

chain = LLMChain(llm=gpt_chat,prompt=prompt)

opinion = chain.run({'company':'zomato'})

print(opinion)