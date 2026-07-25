from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch
import ollama
load_dotenv()

def main():
    print('main fun')
    result=agent.invoke({'messages':HumanMessage(content='Please provide me with jobs related to AI product manager in Hyderabad for 5 years of experience in software engineering and idea on LLM models, RAG and langchain and machine learning I need 10 jobs with good pay to apply')})
    print(result)


def search(query):
    """Tool that searches over the internet
    Args: 
        query: the query to be searched
    return:
        returns the search result"""

    return ollama.web_search(query=query)

llm=ChatOllama(temperature=1,model="qwen3:4b")
tools=[TavilySearch()]
agent=create_agent(model=llm,tools=tools)
if __name__=='__main__':
    main()


