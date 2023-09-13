import os
from dotenv import load_dotenv, find_dotenv
import pinecone

import tiktoken


from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
load_dotenv(find_dotenv(), override=True)


pinecone.init(api_key=os.environ.get('PINECONE_KEY'),
              environment=os.environ.get('PINECONE_ENV'))


index_name = "churchill-speech"

if index_name not in pinecone.list_indexes():
    print(f'Creating index {index_name}')
    pinecone.create_index(index_name, dimension=1536,
                          metric='cosine', pods=1, pod_type='p1.x2')
    print(f'{pinecone.describe_index(index_name)} created')
else:
    print(f'{pinecone.describe_index(index_name)} already exists')

index = pinecone.Index(index_name=index_name)
print(index.describe_index_stats())


def print_embedding_cost(texts):
    encoding = tiktoken.encoding_for_model('text-embedding-ada-002')
    total_tokens = sum([len(encoding.encode(page.page_content))
                       for page in texts])
    print(f'Total tokens: {total_tokens}')
    print(f'Embedding Cost in USD: {total_tokens/1000*0.0004:.6f}')


with open('files/churchill_speech.txt') as f:
    churchill_speech = f.read()
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    length_function=len
)

chunks = text_splitter.create_documents([churchill_speech])

print_embedding_cost(chunks)

embedding = OpenAIEmbeddings(openai_api_key=os.environ.get("OPEN_API_KEY"))

vector_store=Pinecone.from_documents(chunks,embedding=embedding,index_name=index_name)


print(vector_store.similarity_search("where shall we fight"))

