from typing import List, Optional

from pydantic import BaseModel


class Blog(BaseModel):
    title:str 
    body:str
    class Config:
        orm_mode = True

class User(BaseModel):
    name:str
    email:str
    password:str

class UserShow(BaseModel):
    name:str
    email:str
    blogs: List[Blog] = []
    class Config:
        orm_mode = True
class UserBase(BaseModel):
    name:str
    email:str
    class Config:
        orm_mode = True
class ShowBlog(BaseModel):
    title:str 
    body:str
    creator:UserShow

    class Config:
        orm_mode = True

class Login(BaseModel):
    email:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None



        



