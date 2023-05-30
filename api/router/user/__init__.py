# coding=utf-8
from typing import List

from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session

from database import models, schemas
from database.crud.user import get_user_by_uuid, delete_user_token, get_user_token_by_id, create_user_token, \
    update_user_password, update_user_email, update_user_info
from database.func import get_db
from router.oauth import get_current_user, get_current_token
from utils.encryption import verify_hash_password
from utils.status_code import Unauthorized, NotFound, Forbidden, UnprocessableEntity, NoContent

user_router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={401: {"description": "Unauthorized"}},
)


@user_router.get("/", response_model=schemas.User, tags=["users"])
async def get_root(user: models.User = Depends(get_current_user)) -> models.User:
    if not user:
        raise Unauthorized
    return user


@user_router.get("/me", response_model=schemas.User, tags=["users"])
async def get_self(user: models.User = Depends(get_current_user)) -> models.User:
    if not user:
        raise Unauthorized
    return user


@user_router.get("/{uuid}", response_model=schemas.User, tags=["users"])
async def get_user_info_from_uuid(uuid: str, db: Session = Depends(get_db)) -> models.User:
    user = get_user_by_uuid(db, uuid)
    if not user:
        raise NotFound
    return user


# We don't permit to get user info from id to prevent user enumeration.
#
# @user_router.get("/{ids}", response_model=schemas.User, tags=["users"])
# async def get_user_info_from_id(ids: int, db: Session = Depends(get_db)) -> models.User:
#     user = get_user_by_id(db, ids)
#     if not user:
#         raise NotFound
#     return user

@user_router.patch("/me", response_model=schemas.User, tags=["users"])
async def update_self(user: schemas.UserUpdate, db: Session = Depends(get_db),
                      current_user: models.User = Depends(get_current_user)) -> models.User:
    if not current_user:
        raise Unauthorized

    if not current_user.is_active:
        raise Forbidden

    # catch password change
    if user.password and user.new_password:
        # check password match
        if not verify_hash_password(user.password, current_user.encrypted_password):
            raise Unauthorized
        elif verify_hash_password(user.new_password, current_user.encrypted_password):
            raise UnprocessableEntity
        else:
            update_user_password(db, user, current_user)
    # catch email change
    elif user.email:
        # check password match
        if not verify_hash_password(user.password, current_user.encrypted_password):
            raise Unauthorized
        elif user.email == current_user.email:
            raise UnprocessableEntity
        else:
            update_user_email(db, user, current_user)
    else:
        return update_user_info(db, user, current_user)


@user_router.post("/me/token", response_model=schemas.UserToken, tags=["users"])
async def create_self_token(db: Session = Depends(get_db),
                            user: models.User = Depends(get_current_user)) -> models.User:
    if not user:
        raise Unauthorized

    if not user.is_active:
        raise Forbidden

    token = create_user_token(db, user)
    return token


@user_router.get("/me/token", response_model=List[schemas.UserToken], tags=["users"])
async def get_self_token_all(user: models.User = Depends(get_current_user)) -> List[models.UserToken]:
    if not user:
        raise Unauthorized

    if not user.is_active:
        raise Forbidden

    tokens = user.tokens

    return list(tokens)


@user_router.delete("/me/token", responses={204: {"description": "No Content"}}, tags=["users"])
async def delete_self_token_all(db: Session = Depends(get_db), user: models.User = Depends(get_current_user),
                                current_token: models.UserToken = Depends(get_current_token)) -> None:
    if not user:
        raise Unauthorized('Need login')

    if not user.is_active:
        raise Forbidden('User is not active')

    tokens = user.tokens

    # remove current token from tokens
    # tokens.remove(current_token)

    for token in tokens:
        if token != current_token:
            delete_user_token(db, token)

    raise NoContent


@user_router.delete("/me/token/{token_id}", responses={204: {"description": "No Content"}}, tags=["users"])
async def delete_self_token(db: Session = Depends(get_db), user: models.User = Depends(get_current_user),
                            token_id: int = Path(gt=0)) -> None:
    if not user:
        raise Unauthorized('Need login')

    if not user.is_active:
        raise Forbidden('User is not active')

    token = get_user_token_by_id(db, token_id)

    if not token:
        raise NotFound('Token not found')

    if token.user_id != user.id:
        raise Forbidden('Token not belong to user')

    delete_user_token(db, token)

    raise NoContent
