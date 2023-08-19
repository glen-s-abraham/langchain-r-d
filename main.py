import os
from  dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv(),override=True)

print(os.environ.items())