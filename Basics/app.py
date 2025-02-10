from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
# os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
# Langsmith tracking
os.environ['LANGSMITH_TRACING']='True'
os.environ['LANGSMITH_TRACING_V2']='True'
os.environ['LANGSMITH_ENDPOINT']="https://api.smith.langchain.com"
os.environ['LANGSMITH_API_KEY']="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"
os.environ['LANGSMITH_PROJECT']="pr-linear-inspection-24"
os.environ['LANGCHAIN_API_KEY']="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"
# Prompt Template

prompt=ChatPromptTemplate.from_messages([("system","You are a helpful assistant. Respond to user queries: "),("user","Question:{question}")])

# streamlit framework

st.title("Langchain Demo with Ollama")
input_text=st.text_input("Search the topic you wantT")

# Ollama llm
llm=Ollama(model="mistral")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))