from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from database import models, schemas
from database.crud.user import get_user_token_by_token
from database.func import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_token(token: str = Depends(oauth2_scheme), db=Depends(get_db)) -> None | models.UserToken:
    token = get_user_token_by_token(db, token)
    return token


async def get_current_user(token: schemas.UserToken = Depends(get_current_token)) -> None | models.User:
    return token.user if token else None
