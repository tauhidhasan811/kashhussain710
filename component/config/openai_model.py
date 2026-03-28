from langchain_openai import ChatOpenAI

def LoadGPT(model_name: str = 'gpt-4.1-2025-04-14'):
    llm = ChatOpenAI(
        model=model_name,
        temperature=0
    )
    return llm