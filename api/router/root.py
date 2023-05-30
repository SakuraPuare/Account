# coding=utf-8

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import schemas, models
from database.crud.user import get_user_by_email, create_user_token, create_user
from database.func import get_db
from utils.encryption import verify_hash_password, generate_md5, generate_hash_password
from utils.status_code import Unauthorized, UnprocessableEntity

root_router = APIRouter()


@root_router.post("/login", tags=["root"], response_model=schemas.UserToken)
async def login(user: schemas.UserLogin, db: Session = Depends(get_db)) -> models.UserToken:
    # check post body
    if not user:
        raise Unauthorized('Wrong email or password.')

    email = user.email
    lookup_user = get_user_by_email(db, email)
    if not lookup_user:
        raise Unauthorized('Wrong email or password.')

    password = user.password
    if not verify_hash_password(password, lookup_user.encrypted_password):
        raise Unauthorized('Wrong email or password.')

    return create_user_token(db, lookup_user)


@root_router.post("/register", tags=["root"], response_model=schemas.UserToken)
async def register(user: schemas.UserCreate, db: Session = Depends(get_db)) -> models.UserToken:
    # check post body
    if not user:
        raise UnprocessableEntity('Invalid value.')

    email = user.email
    lookup_user = get_user_by_email(db, email)
    if lookup_user:
        raise UnprocessableEntity('Email already exists.')

    current_user = models.User(username=user.username, email=email, email_md5=generate_md5(email),
                               encrypted_password=generate_hash_password(user.password), slogan=user.slogan)
    create_user(db, current_user)

    return create_user_token(db, current_user)
