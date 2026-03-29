from component.asset.prompt_tempt import  GenMotorPrompt, GenMOTPrompt
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from component.config.openai_model import LoadGPT
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
llm = LoadGPT()

@app.post("/api/ai/analysis/motor")
async def AnalysisCarData(motor_info: str, user_query: str, previous_chat: str):
    try:
        prompt = GenMotorPrompt(motor_info=motor_info,
                            user_query=user_query,
                            previous_chat=previous_chat)
        
        response = llm.invoke(prompt.text)
        return JSONResponse(
            status_code=200,
            content={
                'status': True,
                'status_code': 200,
                'message': response.content
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                'status': False,
                'status_code': 500,
                'message': str(e)
            }
        )
    
@app.post("/api/ai/analysis/mot")
async def AnalysisMOTData(mot_info: str, user_query: str, previous_chat: str):
    try:
        prompt = GenMOTPrompt(mot_info=mot_info,
                            user_query=user_query,
                            previous_chat=previous_chat)
        
        response = llm.invoke(prompt.text)
        return JSONResponse(
            status_code=200,
            content={
                'status': True,
                'status_code': 200,
                'message': response.content
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                'status': False,
                'status_code': 500,
                'message': str(e)
            }
        )
# prompt = GenMTOPrompt("MOT information", "User Query", "Previous chat")

# print(prompt.text)