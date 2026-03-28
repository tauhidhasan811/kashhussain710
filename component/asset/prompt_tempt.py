from langchain.messages import SystemMessage, HumanMessage
from langchain_core.prompts import PromptTemplate

def GenPrompt(mot_info, user_query, previous_chat):
    sys_message = SystemMessage(
        content=(
            "You are a chat assistant. "
            "Your task is to answer the user query based on "
            "the car Ministry of Transport (MOT) report data."
        )
    )

    human_message = HumanMessage(
        content=(
            f"Current user query: {user_query}\n"
            f"MOT data: {mot_info}\n"
            f"User previous query: {previous_chat}"
        )
    )

    temp = PromptTemplate(
        template="System Message: {sys_message}\n\nHuman Message: {human_message}",
        input_variables=['sys_message', 'human_message']
    )

    prompt = temp.invoke(
        input={
            'sys_message': sys_message.content,
            'human_message': human_message.content
        }
    )

    return prompt
