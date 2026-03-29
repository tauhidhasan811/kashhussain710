from pydantic import BaseModel
from typing import List, Dict


class MotorData(BaseModel):
    motor_info: Dict
    user_query: str
    previous_chat: List[Dict]