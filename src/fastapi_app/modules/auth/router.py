from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel, EmailStr, Field

class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)

router = APIRouter(prefix="/auth", tags=["Authentication"])

# http://localhost:8000/api/v1/auth/register
@router.post('/register', status_code=status.HTTP_201_CREATED)
def register():
    return {"status": "success"}

# http://localhost:8000/api/v1/auth/login
@router.post("/login")
def login(request: LoginRequest):
    if len(request.password) >= 15:
        raise HTTPException(status_code=400, detail="รหัสผ่านต้องไม่เกิน 15 ตัวอักษร")
    return { "data": request}