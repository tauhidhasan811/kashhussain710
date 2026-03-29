from pydantic import BaseModel

class MOTData(BaseModel):
    mot_info: str
    user_query: str
    previous_chat: str