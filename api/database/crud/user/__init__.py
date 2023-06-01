# coding=utf-8
import datetime

from sqlalchemy.orm import Session

from database import models, schemas
from database.crud import create, update, delete
from utils.encryption import generate_user_token, generate_hash_password, generate_md5, generate_captcha_code


def create_user(db: Session, user: models.User) -> models.User:
    return create(db, user)


def get_user_by_id(db: Session, user_id: int) -> models.User:
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_uuid(db: Session, uuid: str) -> models.User:
    return db.query(models.User).filter(models.User.uuid == uuid).first()


def get_user_by_token(db: Session, token: str) -> models.User:
    return db.query(models.User).join(models.UserToken).filter(models.UserToken.token == token).first()


def get_user_by_email(db: Session, email: str) -> models.User:
    return db.query(models.User).filter(models.User.email == email).first()


def update_user(db: Session, user: models.User) -> models.User:
    user.updated_at = datetime.datetime.now()
    return update(db, user)


def update_user_info(db: Session, updated_user: schemas.UserUpdate, current_user: models.User) -> models.User:
    if updated_user.slogan:
        current_user.slogan = updated_user.slogan
    if updated_user.username:
        current_user.username = updated_user.username
    return updated_user(db, current_user)


def update_user_password(db: Session, updated_user: schemas.UserUpdate, current_user: models.User) -> models.User:
    current_user.encrypted_password = generate_hash_password(updated_user.new_password)
    return update_user(db, current_user)


def update_user_email(db: Session, update_user: schemas.UserUpdate, current_user: models.User) -> models.User:
    # update email
    current_user.email = update_user.email
    current_user.email_md5 = generate_md5(update_user.email)
    current_user.email_verified_at = None
    return update_user(db, current_user)


def update_user_email_captcha(db: Session, user: models.User) -> models.User:
    user.email_verified_at = datetime.datetime.now()
    return update_user(db, user)


def create_user_token(db: Session, user: models.User, lifetime: int = 86400) -> models.UserToken:
    token = generate_user_token(user)

    db_token = models.UserToken(user_id=user.id, token=token, lifetime=lifetime)
    return create(db, db_token)


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
    if token:
        return delete(db, token)


def delete_user_token_by_id(db: Session, ids: int) -> None:
    token = get_user_token_by_id(db, ids)
    return delete_user_token(db, token)


def delete_user_token_by_token(db: Session, token: str) -> None:
    db_token = get_user_token_by_token(db, token)
    return delete_user_token(db, db_token)


def create_email_captcha(db: Session, user: models.User) -> None:
    code = generate_captcha_code()

    captcha = models.EmailCaptcha(user_id=user.id, email=user.email, captcha=code)

    return create(db, captcha)


def delete_email_captcha(db: Session, captcha: models.EmailCaptcha) -> None:
    if captcha:
        return delete(db, captcha)


def update_email_captcha(db: Session, user: models.User, captcha: schemas.EmailCaptchaUpdate) -> bool:
    for code in user.captcha:
        code: models.EmailCaptcha
        if datetime.datetime.now() > code.expired_at:
            delete_email_captcha(db, code)
        else:
            if code.captcha == captcha.captcha:
                delete_email_captcha(db, code)
                update_user_email_captcha(db, user)
                return True
    return False
