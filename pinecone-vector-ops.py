import pinecone
import os
import random
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)


pinecone.init(api_key=os.environ.get('PINECONE_KEY'),
              environment=os.environ.get('PINECONE_ENV'))

index_name = "langchain-pinecone"
index = pinecone.Index(index_name=index_name)


vectors = [[random.random() for _ in range(1536)]for v in range(5)]
#vectors
ids=list('abcde')

print(index.upsert(vectors=zip(ids,vectors)))

print(index.upsert(vectors=[('c',[0.3]*1536)]))

print(index.fetch(ids=['c','d']))

print(index.delete(ids=['b','c']))

print(index.fetch(ids=['b','d']))

print(index.describe_index_stats())