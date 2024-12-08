from pydantic import BaseModel

# User login model
class LoginRequest(BaseModel):
    username: str
    password: str

# Token response model
class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
