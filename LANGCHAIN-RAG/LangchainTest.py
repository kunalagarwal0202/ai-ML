def main():
    print("Hello from langchain-course!")


from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
load_dotenv()


#llm = ChatOpenAI(model="gpt-5", temperature=0)
llm = ChatOllama(model="qwen3:4b", temperature=0)

resp = llm.invoke("Explain LangChain in one sentence.")
print(resp.content)



if __name__ == "__main__":
    main()
