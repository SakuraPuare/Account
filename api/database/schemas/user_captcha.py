# coding=utf-8
import datetime

from pydantic import BaseModel

from database import schemas


class EmailCaptchaBase(BaseModel):
    class Config:
        orm_mode = True


class EmailCaptchaUpdate(EmailCaptchaBase):
    captcha: str = ''


class EmailCaptcha(EmailCaptchaBase):
    id: int
    user: schemas.User
    email: str
    captcha: str
    created_at: datetime.datetime
    expired_at: datetime.datetime
