# coding=utf-8
import datetime
import uuid

from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey, BigInteger
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    uuid = Column(String(255), unique=True, index=True, default=uuid.uuid4())
    username = Column(String(255), unique=True, index=True)
    email = Column(String(255), unique=True, index=True)
    email_md5 = Column(String(255), unique=True, index=True)
    email_verified_at = Column(DateTime, nullable=True)
    slogan = Column(String(511), default='')
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, default=datetime.datetime.now())

    encrypted_password = Column(String(511))

    tokens = relationship('UserToken', backref='user')

    def __repr__(self):
        return f'<User {self.id} {self.username}>'


class UserToken(Base):
    __tablename__ = 'user_tokens'
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey('users.id'))
    token = Column(String(512), unique=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.now())
    expired_at = Column(DateTime, default=datetime.datetime.now() + datetime.timedelta(days=1))
    lifetime = Column(BigInteger, default=86400)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f'<UserToken {self.id} -> {self.user_id} {self.expired_at}>'

    @property
    def is_expired(self) -> bool:
        return datetime.datetime.now() > self.expired_at and self.is_active
