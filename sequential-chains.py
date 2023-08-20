import os
from  dotenv import load_dotenv,find_dotenv
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain,SimpleSequentialChain
load_dotenv(find_dotenv(),override=True)

gpt_client = OpenAI(model='text-davinci-003',temperature=0.7,max_tokens=512,openai_api_key=os.environ.get("OPEN_API_KEY"),max_retries=1)
gpt_chat=ChatOpenAI(model='gpt-3.5-turbo',temperature=0.5,max_tokens=1024,openai_api_key=os.environ.get("OPEN_API_KEY"),max_retries=1)

prompt1 = PromptTemplate(
    input_variables=['concept'],
    template='''You are an experienced scientist and python programmer.write a function that implements the concept of {concept}'''
)
chain1 = LLMChain(llm=gpt_client,prompt=prompt1)


prompt2 = PromptTemplate(
    input_variables=['function'],
    template='''Given the python {function} describe it as detailed as possible'''
)
chain2 = LLMChain(llm=gpt_chat,prompt=prompt2)

sequential_chain = SimpleSequentialChain(chains=[chain1,chain2],verbose=True)

response = sequential_chain.run('linear regression')

print(response)