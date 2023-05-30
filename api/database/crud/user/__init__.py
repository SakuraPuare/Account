# coding=utf-8
import datetime

from sqlalchemy.orm import Session

from database import models, schemas
from utils.encryption import generate_user_token, generate_hash_password, generate_md5
from utils.status_code import StatusCode


def create_user(db: Session, user: models.User) -> models.User:
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        db.rollback()
        raise e
    return user


def get_user_by_id(db: Session, user_id: int) -> models.User:
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_uuid(db: Session, uuid: str) -> models.User:
    return db.query(models.User).filter(models.User.uuid == uuid).first()


def get_user_by_token(db: Session, token: str) -> models.User:
    return db.query(models.User).join(models.UserToken).filter(models.UserToken.token == token).first()


def get_user_by_email(db: Session, email: str) -> models.User:
    return db.query(models.User).filter(models.User.email == email).first()


def update_user(db: Session, user: models.User) -> models.User:
    try:
        user.updated_at = datetime.datetime.now()
        db.commit()
        db.refresh(user)
    except Exception as e:
        db.rollback()
        raise e
    return user


def update_user_info(db: Session, update: schemas.UserUpdate, current: models.User) -> models.User:
    if update.slogan:
        current.slogan = update.slogan
    if update.username:
        current.username = update.username
    return update_user(db, current)


def update_user_password(db: Session, update: schemas.UserUpdate, current: models.User) -> models.User | StatusCode:
    current.encrypted_password = generate_hash_password(update.new_password)
    return update_user(db, current)


def update_user_email(db: Session, update: schemas.UserUpdate, current: models.User) -> models.User | StatusCode:
    # update email
    current.email = update.email
    current.email_md5 = generate_md5(update.email)
    return update_user(db, current)


def create_user_token(db: Session, user: models.User, lifetime: int = 86400) -> models.UserToken:
    token = generate_user_token(user)

    db_token = models.UserToken(user_id=user.id, token=token, lifetime=lifetime)
    try:
        db.add(db_token)
        db.commit()
        db.refresh(db_token)
    except Exception as e:
        db.rollback()
        raise e
    return db_token


def create_user_token_from_user_id(db: Session, user_id: int, lifetime: int) -> models.UserToken:
    user = get_user_by_id(db, user_id)
    return create_user_token(db, user, lifetime)


def get_user_token_by_id(db: Session, ids: int) -> models.UserToken:
    return db.query(models.UserToken).filter(models.UserToken.id == ids).first()


def get_user_token_by_user_id(db: Session, user_id: int) -> models.UserToken:
    return db.query(models.UserToken).filter(models.UserToken.user_id == user_id).first()


def get_user_token_by_token(db: Session, token: str) -> models.UserToken:
    # Get last token
    return db.query(models.UserToken).filter(models.UserToken.token == token).order_by(
        models.UserToken.id.desc()).first()


def delete_user_token(db: Session, token: models.UserToken) -> None:
    try:
        db.delete(token)
        db.commit()
    except Exception as e:
        db.rollback()
        raise e


def delete_user_token_by_id(db: Session, ids: int) -> None:
    token = get_user_token_by_id(db, ids)
    if token:
        delete_user_token(db, token)


def delete_user_token_by_token(db: Session, token: str) -> None:
    db_token = get_user_token_by_token(db, token)
    if db_token:
        try:
            db.delete(db_token)
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
