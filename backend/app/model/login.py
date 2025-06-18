from pydantic import BaseModel

class LoginRequest(BaseModel):
    client_id: str
    client_secret: str