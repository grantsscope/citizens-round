import streamlit as st


import os
os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']

from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader

# load from disk
#index = GPTVectorStoreIndex.load_from_disk('index.json')
index = load_index_from_disk(StorageContext.from_defaults(persist_dir="./storage"))

# while True:
question = st.text_input("Question", placeholder="Enter your question here")

if question != "":
    response = index.query(question)
    display = "\n" + "\n**" + question + "**\n" + str(response)
    st.markdown(display)
