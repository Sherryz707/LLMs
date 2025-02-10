from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv(r"E:\llm\LLMs\.env")
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')

app=FastAPI(title="Langchain Server",version="1.0",description="A simple API server")

# adding routes
add_routes(
    app,
    Ollama(model="mistral"),
    path="/ollama"
)

llm=Ollama(model="mistral")

prompt1=ChatPromptTemplate.from_template("Write an essay about {topic} with 100 words")
prompt2=ChatPromptTemplate.from_template("Write me a poem about {topic} with 100 words")

add_routes(
    app,
    prompt1|llm,
    path="/essay"
)
add_routes(
    app,
    prompt2|llm,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)
