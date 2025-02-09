from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv


# os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
# Langsmith tracking
# os.environ['LANGCHAIN_TRACING_V2']="true"
# print("environ",os.getenv('LANGSMITH_API_KEY'))
# os.environ['LANGSMITH_API_KEY']=os.getenv('LANGSMITH_API_KEY')

# Prompt Template

prompt=ChatPromptTemplate.from_messages([("system","You are a helpful assistant. Respond to user queries: "),("user","Question:{question}")])

# streamlit framework

st.title("Langchain Demo with Ollama")
input_text=st.text_input("Search the topic you want")

# Ollama llm
llm=Ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))