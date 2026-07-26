from langchain_ollama import ChatOllama
llm = ChatOllama(model="gemma3:270m")
step1 = llm.invoke(""" List the important concepts about diabetes. """)
print(step1)

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import AIMessagePromptTemplate, HumanMessagePromptTemplate
prompt = ChatPromptTemplate.from_messages([
    HumanMessagePromptTemplate.from_template(
        "i Want to understand these topics on diabetes"
    ),
    AIMessagePromptTemplate.from_template(
        "Sure! I'll explain in detail like a 10 year old"
    )
])

chain = prompt | llm 
response = chain.invoke({})
print("-"*89)
print(response.content)