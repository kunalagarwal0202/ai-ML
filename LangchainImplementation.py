from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch
import ollama
load_dotenv()

def main():
    print('main fun')
    result=agent.invoke({'messages':HumanMessage(content='Please provide me with jobs related to AI product manager'),})
    print(result)


llm=ChatOllama(model="nemotron-3-super:cloud")
tools=[TavilySearch()]
agent=create_agent(model=llm,tools=tools)
if __name__=='__main__':
    main()


