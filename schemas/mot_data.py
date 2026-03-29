from pydantic import BaseModel
from typing import List, Dict


class MOTData(BaseModel):
    mot_info: Dict
    user_query: str
    previous_chat: List[Dict]