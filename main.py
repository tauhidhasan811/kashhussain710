from component.asset.prompt_tempt import  GenMotorPrompt, GenMTOPrompt
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from component.config.openai_model import LoadGPT
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
llm = LoadGPT()

@app.post("/analysis/motor")
async def AnalysisCarData(motor_info: str, user_query: str, previous_chat: str):
    prompt = GenMotorPrompt(motor_info=motor_info,
                          user_query=user_query,
                          previous_chat=previous_chat)
    
    response = llm.invoke(prompt.text)
    return JSONResponse(
        status_code=200,
        content={
            'status': True,
            'message': response.content
        }
    )

# prompt = GenMTOPrompt("MOT information", "User Query", "Previous chat")

# print(prompt.text)