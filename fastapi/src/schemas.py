from datetime import datetime, date
from pydantic import BaseModel, EmailStr, Field


class ContactModel(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    date_of_birth: date
    
    
class ContactResponse(ContactModel):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True


class UserModel(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(min_length=6, max_length=14)


class UserDb(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime
    avatar: str
    
    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    user: UserDb
    detail: str = 'User successfully created'


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = 'bearer'


class RequestEmail(BaseModel):
    email: EmailStr