from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    pass


class UserInDB(UserBase):
    user_id: int

    class Config:
        orm_mode = True
