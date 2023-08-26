import os
from  dotenv import load_dotenv,find_dotenv
from langchain.llms import OpenAI
load_dotenv(find_dotenv(),override=True)

gpt_client = OpenAI(model='text-davinci-003',temperature=0.7,max_tokens=512,openai_api_key=os.environ.get("OPEN_API_KEY"),max_retries=1)

questions = [
    "... is the capital of india",
    "Generate an original tagline for a burger restaurent",
    "What is the formula to calculate a line angle"
]

answers = gpt_client.generate(questions);

for answer in answers:
    print(answer)