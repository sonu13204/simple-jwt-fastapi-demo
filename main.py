from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from datetime import timedelta

from database import get_user, verify_password
from schemas import LoginRequest, TokenResponse
from auth import create_access_token, create_refresh_token, verify_access_token, verify_refresh_token

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Login endpoint to generate access and refresh tokens
@app.post("/login", response_model=TokenResponse)
async def login(request: LoginRequest):
    user = get_user(request.username)
    if not user or not verify_password(request.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )

    # Create access and refresh tokens
    access_token = create_access_token({"sub": request.username}, timedelta(minutes=15))
    refresh_token = create_refresh_token({"sub": request.username})

    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

# Protected route
@app.get("/protected")
async def protected_route(token: str = Depends(oauth2_scheme)):
    username = verify_access_token(token)
    if not username:
        raise HTTPException(status_code=401, detail="Invalid access token")
    return {"message": f"Welcome, {username}!"}

# Refresh token endpoint
@app.post("/refresh", response_model=TokenResponse)
async def refresh(refresh_token: str):
    username = verify_refresh_token(refresh_token)
    if not username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token"
        )

    # Generate new tokens
    access_token = create_access_token({"sub": username}, timedelta(minutes=15))
    refresh_token = create_refresh_token({"sub": username})

    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}
