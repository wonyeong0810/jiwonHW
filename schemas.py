# schemas.py
from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: str

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None

class PostCreate(BaseModel):
    title: str
    content: str
    owner_id: int

class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class CommentCreate(BaseModel):
    content: str
    post_id: int
    creator_id: int

class CommentUpdate(BaseModel):
    content: Optional[str] = None
