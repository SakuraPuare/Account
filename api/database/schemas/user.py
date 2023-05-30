# coding=utf-8
import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    pass


class UserCreate(UserBase):
    username: str = ''
    password: str = ''
    change_password: str = ''
    email: str = ''
    slogan: str = ''
    email_is_verified: bool = False


class UserUpdate(UserBase):
    username: str = ''
    password: str = ''
    new_password: str = ''
    email: str = ''
    slogan: str = ''
    email_is_verified: bool = False


class UserLogin(BaseModel):
    email: str
    password: str

    def __bool__(self):
        return bool(self.email and self.password)


class User(UserBase):
    id: int
    uuid: str
    username: str
    email: str
    email_md5: str = ''
    email_verified_at: datetime.datetime | None
    slogan: str = ''
    is_active: bool = True
    is_superuser: bool = False
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True
