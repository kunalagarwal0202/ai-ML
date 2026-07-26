from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain.tools import tool
from langsmith import traceable
from langchain_tavily import TavilySearch
load_dotenv()
from langchain.messages import HumanMessage, SystemMessage, ToolMessage
model="qwen3:4b"
Max_Iterations=5


def main():
    print("creating new agents")

@tool
def webSearch(product):
  "you are websearch assistant whenever you get a product you have to seacrh it on web and return a price"
  "do not assume prices on your own"
  response=TavilySearch(product)
  print(response)
  return response

@tool
def discount_price_tool(product_price):
    """ tool to apply discount on the product prices"""
    print(product_price*0.8)
    return(product_price*0.8)

def execute_agent(query:str):
    search = TavilySearch(max_results=5)
    tools=[discount_price_tool]
    #tool_dict={t.name:t for t in tools}
    tool_dict={'discount_price_tool':discount_price_tool}
    llm=init_chat_model(f"ollama:{model}")
    llm_tool=llm.bind_tools(tools)
    messages=[
            SystemMessage(
                content=(
                    "you are helpful assistant that is needed for a e-commerce application for users to find laptops"
                    "STRICT  RULES: FOLLOW AS EXACTLY"
                    "never assume the price on your own, find it from tavily search tool"
                    "never discount the prices on your own use the discount_price_tool tool"
                    "never discount without knowing the price or never use made up number and never use made up discount number"
                )
            ),
            HumanMessage(content=query)
        ]

    ai_response=llm_tool.invoke(messages)
    tool_call=ai_response.tool_calls
    
    
    if not tool_call:
         print(ai_response)

    tool_call=tool_call[0]
    tool_name=tool_call.get('name')
    tool_call_id=tool_call.get("id")
    too_args=tool_call.get('args')
    
    tool_to_use=tool_dict.get(tool_name)
    response = search.invoke(
    {"query": too_args["product"]})
    print(response)
    print(tool_to_use)
    observation=tool_to_use.invoke(response)
    
    messages.append(ai_response)
    messages.append(ToolMessage(content=str(observation),tool_call_id=tool_call_id))
  

execute_agent("i want to buy hp laptop with 16gb ram and provide me a discount")




