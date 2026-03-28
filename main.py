from component.asset.prompt_tempt import GenMTOPrompt, GenMotorPrompt
from fastapi import FastAPI

app = FastAPI()

@app.post
async def Analysis

prompt = GenMTOPrompt("MOT information", "User Query", "Previous chat")

print(prompt)