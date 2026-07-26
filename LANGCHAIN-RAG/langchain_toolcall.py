from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain.tools import tool
from langsmith import traceable
load_dotenv()
from langchain.messages import HumanMessage, SystemMessage, ToolMessage
model="qwen3:4b"
Max_Iterations=10

@tool
def product_prices_tool(product):
    """ tool to get the prices of product from the catalogue"""
    print(f"executing tool product prices for {product}")
    product_prices={"laptop":1299,"headphones":599,"keyboard":399}
    return product_prices.get(product,0)

@tool
def discount_tool(price,tier):
    """ tool to apply discount on the product prices based on tier
    available tiers: Gold, Silver, Bronze"""
    print(f"executing tool discount for tier{tier} and price {price}")
    discounts_percentage={"Gold":20,"silver":15,"bronze":10}
    discount=discounts_percentage.get(tier,0)
    final_price=round(price*(1-discount/100),2)
    return final_price

@traceable(name="E-commerce_Agent")
def run_agent(question:str):
    tools=[product_prices_tool, discount_tool]
    tool_dict={t.name:t for t in tools}
    tool_dict={t.name:t for t in tools}
    llm=init_chat_model(f"ollama:{model}")
    llm_tool=llm.bind_tools(tools)
    messages=[
        SystemMessage(
            content=(
                "you are helpful assistant"
                "you have access to product catalouge"
                "and a discount tool. \n\n"
                "STRICT  RULES: FOLLOW AS EXACTLY"
                "Never guess or assume the price of the product"
                "you must call product_prices_tool to get the price "
                 "DO NOT call discount_tool without price"
                "apply discount_tool only after we get the product price"
                "do not pass a made up number"
                "never guess the discounted value use the discount tool"

            )
        ),
        HumanMessage(content=question)
    ]

    for i in range(1,Max_Iterations):
        ai_message=llm_tool.invoke(messages)
        print(ai_message)
        tool_calls=ai_message.tool_calls
        print(tool_calls )
        if not tool_calls:
            return ai_message.content
        
        tool_call=tool_calls[0]
        tool_name=tool_call.get('name')
        tool_call_id=tool_call.get("id")
        too_args=tool_call.get('args')
        tool_to_use=tool_dict.get(tool_name)
        observation=tool_to_use.invoke(too_args)
        messages.append(ai_message)
        messages.append(ToolMessage(content=str(observation),tool_call_id=tool_call_id))

if __name__=="__main__":
    print("Starting the agents")
    test= run_agent("what is the price of laptop with the Gold tier discount")
    print("test",test)
