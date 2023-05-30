# coding=utf-8
import datetime
from typing import Optional

from pydantic import BaseModel

from database import schemas


class UserTokenBase(BaseModel):
    id: int

    class Config:
        orm_mode = True


class UserToken(UserTokenBase):
    id: int
    user: schemas.User
    token: str
    created_at: datetime.datetime
    expired_at: datetime.datetime
    lifetime: int
    is_active: bool

    class Config:
        orm_mode = True
