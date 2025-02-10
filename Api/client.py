import requests
import streamlit as st

base_str="http://localhost:8000"


def get_essay_response(input_text):
    response=requests.post(f"{base_str}/essay/invoke",
    json={'input':{'topic':input_text}})
    return response.json()['output']

def get_poem_response(input_text):
    response=requests.post(f"{base_str}/poem/invoke",json={'input':{'topic':input_text}})
    return response.json()['output']


# streamlit framework

st.title("Langchain Demo with LLAMA2 API")
essay_text=st.text_input("Write an essay on")
poem_text=st.text_input("Write a poem on")

if essay_text:
    st.write(get_essay_response(essay_text))

if poem_text:
    st.write(get_poem_response(poem_text))