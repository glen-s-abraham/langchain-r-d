import openai
import os
import streamlit as st
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

# Document loader


def load_document(file):
    import os
    # refactor to a factory
    name, extension = os.path.splitext(file)
    print(f'loading {file}')
    if extension == '.pdf':
        from langchain.document_loaders import PyPDFLoader
        loader = PyPDFLoader(file)
    elif extension == '.docx':
        from langchain.document_loaders import Docx2txtLoader
        loader = Docx2txtLoader(file)
    elif extension == '.txt':
        from langchain.document_loaders import TextLoader
        loader = TextLoader(file)
    else:
        print('Document format not supported')
    data = loader.load()
    return data

# Split document into chunks of specified size


def chunk_data(data, chunk_size=256, chunk_overlap=20):
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = text_splitter.split_documents(data)
    return chunks

# Create embeddings


def create_embeddings(chunks):
    embeddings = OpenAIEmbeddings()
    vector_store = Chroma.from_documents(chunks, embedding=embeddings)
    return vector_store


# Calculate embedding cost


def calculate_embedding_cost(texts):
    import tiktoken
    encoding = tiktoken.encoding_for_model('text-embedding-ada-002')
    total_tokens = sum([len(encoding.encode(page.page_content))
                       for page in texts])
    return total_tokens, total_tokens/1000*0.0004


# Vector prompter


def prompt_vector(question, vector_store, k=3):
    from langchain.chains import RetrievalQA
    from langchain.chat_models import ChatOpenAI
    gpt = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    vector_retriever = vector_store.as_retriever(
        search_type='similarity', search_kwargs={'k': k})
    chain = RetrievalQA.from_chain_type(
        llm=gpt, chain_type="stuff", retriever=vector_retriever)
    answer = chain.run(question)
    return answer

def clear_history():
    if 'history' in st.session_state:
        del st.session_state['history']

if __name__ == '__main__':
    openai.key = os.getenv('OPENAI_API_KEY')
    st.subheader('LLM Q&A App')
    with st.sidebar:
        api_key = st.text_input('OpenAI API key:', type='password')
        if api_key:
            os.environ['OPENAI_API_KEY'] = api_key
        uploaded_file = st.file_uploader(
            'Upload file:', type=['pdf', 'docx', 'txt'])
        chunk_size = st.number_input(
            'Chunk_size:', min_value=100, max_value=2048, value=512,on_change=clear_history)
        k = st.number_input('Chunk_size:', min_value=1, max_value=20, value=3,on_change=clear_history)
        add_data = st.button('Add Data',on_click=clear_history)

        if uploaded_file and add_data:
            with st.spinner('Reading, Chunking and Embedding file ...'):
                bytes_data = uploaded_file.read()
                file_name = os.path.join('./uploads', uploaded_file.name)
                with open(file_name, 'wb') as f:
                    f.write(bytes_data)
                data = load_document(file_name)
                chunks = chunk_data(data, chunk_size=chunk_size)
                st.write(f'Chunk size: {chunk_size},Chunks:{len(chunks)}')
                tokens, embeding_cost = calculate_embedding_cost(chunks)
                st.write(f'Embedding cost:${embeding_cost:.4f}')
                vector_store = create_embeddings(chunks=chunks)
                st.session_state.vs = vector_store
                st.success('File uploaded,Chunked and embedded successfully')
    question = st.text_input('Ask a question about the content of the file:')
    if question:
        if 'vs' in st.session_state:
            vector_store = st.session_state.vs
            # st.write(f'k:{k}')
            answer = prompt_vector(question, vector_store, k)
            st.text_area('LLM Response: ', value=answer)
        st.divider()
        if 'history' not in st.session_state:
            st.session_state.history = ''
        value = f'Q: {question}\nA: {answer}'
        st.session_state.history = f'{value}\n{"-"*100}\n{st.session_state.history}'
        h = st.session_state.history
        st.text_area(label='Chat History', value=h,
                    key='history', height=400)
