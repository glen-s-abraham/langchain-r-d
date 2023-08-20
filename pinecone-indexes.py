import pinecone
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)


pinecone.init(api_key=os.environ.get('PINECONE_KEY'),
              environment=os.environ.get('PINECONE_ENV'))

index_name = "langchain-pinecone"

#index creation
if index_name not in pinecone.list_indexes():
    print(f'Creating index {index_name}')
    pinecone.create_index(index_name,dimension=1536,metric='cosine',pods=1,pod_type='p1.x2')
    print(f'{pinecone.describe_index(index_name)} created')
else:
    print(f'{pinecone.describe_index(index_name)} already exists')

#index deletion
if index_name in pinecone.list_indexes():
    print(f'Deleting index {index_name}')
    #pinecone.delete_index(index_name)
    print(f'{index_name} deleted')
else:
    print(f'{index_name} does not exists')

#index operations
index = pinecone.Index(index_name=index_name)
print(index.describe_index_stats())