from langchain.messages import SystemMessage, HumanMessage
from langchain_core.prompts import PromptTemplate

def GenMOTPrompt(mot_info, user_query, previous_chat):
    sys_message = SystemMessage(
        content=("You are a chat assignment"
                "Your task is answer user query based on " 
                "the cars  Ministry of Transport (MOT) report data"
                "Do not hellucinate any data, only answer based on the provided MOT data"
                "If the answer is not found in the MOT data, say 'Sorry, I don't have that information.'")
    )

    human_message = HumanMessage(
        content=f"Current user query: {user_query} \nMOT data: {mot_info}\nUser previous query: {previous_chat}"
    )

    temp = PromptTemplate(
        template="System Message: {sys_message} \n {human_message}",
        input_variables=['sys_message', 'human_message']
    )

    prompt = temp.invoke(
        input={
            'sys_message': sys_message.content,
            'human_message': human_message.content
        }
    )

    return prompt

# def GenMotorPrompt(motor_info, milleage_info, mot_info, 
#                    user_query, previous_chat):
def GenMotorPrompt(motor_info, user_query, previous_chat):
    sys_message = SystemMessage(
        content=("You are a chat assignment"
                "Your task is answer user query based on the Cars/Motor report data"
                "Do not hellucinate any data, only answer based on the provided car/motor data"
                "If the answer is not found in the car/motor data, say 'Sorry, I don't have that information.'")
    )

    human_message = HumanMessage(
        # content=f"Current user query: {user_query} \ncar data: {motor_info}\nMileage data: {milleage_info}\nMOT data: {mot_info}\nUser previous query: {previous_chat}"
        content=f"Current user query: {user_query} \ncar data: {motor_info}\nUser previous query: {previous_chat}"
        
    )

    temp = PromptTemplate(
        template="System Message: {sys_message} \n {human_message}",
        input_variables=['sys_message', 'human_message']
    )

    prompt = temp.invoke(
        input={
            'sys_message': sys_message.content,
            'human_message': human_message.content
        }
    )

    return prompt