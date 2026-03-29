from pydantic import BaseModel

class MotorData(BaseModel):
    motor_info: str
    user_query: str
    previous_chat: str