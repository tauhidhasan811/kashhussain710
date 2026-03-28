from langchain.messages import SystemMessage, HumanMessage
from langchain_core.prompts import PromptTemplate

def GenPrompt(mot_info, user_query, previous_chat):
    sys_message = SystemMessage(
        content="You are a chat assignment"
                "Your task is answer user query based on " \
                "the cars  Ministry of Transport (MTO) report data"
    )

    human_message = HumanMessage(
        content=f"Current user query: {user_query} \n\MOT data: {mot_info}\nUser previous query: {previous_chat}"
    )

    temp = PromptTemplate(
        "System Message: {sys_message} \n {human_message}",
        input_variables=['sys_message', 'human_message']
    )

    prompt = temp.invoke(
        input={
            'sys_message': sys_message.content,
            'human_message': human_message.content
        }
    )

    return prompt