import os
from dotenv import load_dotenv, find_dotenv
from langchain.llms import OpenAI
from langchain import PromptTemplate
load_dotenv(find_dotenv(), override=True)

template = '''You are a financial expert.Write an opition about the company {company}.'''

prompt = PromptTemplate(
    input_variables=['company'],
    template=template
)


gpt_client = OpenAI(model='text-davinci-003', temperature=0.7, max_tokens=512,
                    openai_api_key=os.environ.get("OPEN_API_KEY"), max_retries=1)

opinion = gpt_client(prompt.format(company='ITC'))

print(opinion)
