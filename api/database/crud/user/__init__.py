# coding=utf-8
import datetime

from sqlalchemy.orm import Session

from database import models, schemas
from utils.encryption import generate_user_token, generate_hash_password, generate_md5, generate_captcha_code


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


def update_user_password(db: Session, update: schemas.UserUpdate, current: models.User) -> models.User:
    current.encrypted_password = generate_hash_password(update.new_password)
    return update_user(db, current)


def update_user_email(db: Session, update: schemas.UserUpdate, current: models.User) -> models.User:
    # update email
    current.email = update.email
    current.email_md5 = generate_md5(update.email)
    current.email_verified_at = None
    return update_user(db, current)


def update_user_email_captcha(db: Session, user: models.User) -> models.User:
    user.email_verified_at = datetime.datetime.now()
    return update_user(db, user)


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


def create_email_captcha(db: Session, user: models.User) -> None:
    code = generate_captcha_code()

    captcha = models.EmailCaptcha(user_id=user.id, email=user.email, captcha=code)

    try:
        db.add(captcha)
        db.commit()
        db.refresh(captcha)
    except Exception as e:
        db.rollback()
        raise e


def delete_email_captcha(db: Session, captcha: models.EmailCaptcha) -> None:
    try:
        db.delete(captcha)
        db.commit()
    except Exception as e:
        db.rollback()
        raise e


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
