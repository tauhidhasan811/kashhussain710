from component.asset.prompt_tempt import  GenMotorPrompt, GenMOTPrompt
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from component.config.openai_model import LoadGPT
from dotenv import load_dotenv
from schemas.mot_data import MOTData
from schemas.motor_data import MotorData

load_dotenv()

app = FastAPI()
llm = LoadGPT()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/api/ai/analysis/motor")
async def AnalysisCarData(motorData: MotorData):
    try:
        motor_info=motorData.motor_info,

        user_query = motorData.user_query,
        previous_chat = motorData.previous_chat
        milleage_info = motorData.milleage_info
        mot_info = motorData.mot_info   
        prompt = GenMotorPrompt(motor_info=motor_info,
                            user_query=user_query,
                            milleage_info=milleage_info,
                            mot_info=mot_info,
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
async def AnalysisMOTData(motData: MOTData):
    try:
        mot_info=motData.mot_info
        user_query = motData.user_query,
        previous_chat = motData.previous_chat
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