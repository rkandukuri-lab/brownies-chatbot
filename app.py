from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
import streamlit as st



client = ChatOpenAI(api_key=OPENAI_API_KEY_FREE, model="gpt-4.1-nano")

my_file = "The-Book-of-Brownies.pdf"

loader = PyPDFLoader(my_file)
docs = loader.load()

st.subheader("Chat Application")

qq = st.chat_input("Enter your prompt: ")

if qq:
    my_prompt = f'''
        You are a helpful assistant. Answer the questions based only on the provided data, dont use
        your existing knowledge.

        Question: {qq}
        Document: {docs}
        '''

    response = client.invoke(my_prompt)
    st.write(response.content)


