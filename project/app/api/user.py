from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserIn(BaseModel):
    full_name: Optional[str] = None
    email: EmailStr
    phone: int
    goals: List[str] = []


class UserOut(BaseModel):
	  full_name: Optional[str] = None
    email: EmailStr
    phone: int
    goals: List[str] = []


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user