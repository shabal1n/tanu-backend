from pydantic import BaseModel, validator
from datetime import datetime
from app.core.database import Base
from sqlalchemy import Column, Integer, String, DateTime

from datetime import datetime
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    surname: str
    email: str
    password_hash: str
    last_login: datetime
    xp_points: int

    class Config:
        orm_mode = True

    @validator('email')
    def email_must_contain_at(cls, v):
        if '@' not in v or '.' not in v:
            raise ValueError('E-mail format is incorrect')
        return v

class UserUpdate(BaseModel):
    name: str
    surname: str
    email: str
    password_hash: str
    last_login: datetime
    xp_points: int

    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    name: str
    surname: str
    email: str
    last_login: datetime
    xp_points: int

    class Config:
        orm_mode = True

class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    last_login = Column(DateTime)
    xp_points = Column(Integer)


