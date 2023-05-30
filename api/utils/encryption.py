# coding=utf-8
import datetime
import os
from hashlib import md5

import jwt
from passlib.handlers.pbkdf2 import pbkdf2_sha256

from database import models

ENCRYPT_KEY = os.getenv('ENCRYPT_KEY', '')
ENCRYPT_SALT = os.getenv('ENCRYPT_SALT', '')

if not ENCRYPT_KEY or not ENCRYPT_SALT:
    raise Exception('ENCRYPT_KEY or ENCRYPT_SALT is not set.')


def generate_hash_password(password: str) -> str:
    # sha256 encrypt
    return pbkdf2_sha256.hash(password + ENCRYPT_SALT)


def verify_hash_password(password: str, hash_password: str) -> bool:
    """

    :rtype: object
    """
    # sha256 verify
    try:
        return pbkdf2_sha256.verify(password + ENCRYPT_SALT, hash_password)
    except ValueError:
        return False


def generate_user_token(user: models.User) -> str:
    obj = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'time': datetime.datetime.now().timestamp()
    }
    return jwt.encode(obj, ENCRYPT_KEY + ENCRYPT_SALT, algorithm='HS256')


def generate_md5(message: str) -> str:
    return md5(message.encode('utf-8')).hexdigest()
