from pydantic import BaseModel
from typing import List, Dict


class MotorData(BaseModel):
    motor_info: Dict
    user_query: str
    # milleage_info: Dict
    # mot_info: Dict
    previous_chat: List[Dict]