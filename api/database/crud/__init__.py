# coding=utf-8
from sqlalchemy.orm import Session

from database import models


def create(db: Session, model: models.Base) -> models.Base:
    try:
        db.add(model)
        db.commit()
        db.refresh(model)
    except Exception as e:
        db.rollback()
        raise e
    return model


def update(db: Session, model: models.Base) -> models.Base:
    try:
        db.commit()
        db.refresh(model)
    except Exception as e:
        db.rollback()
        raise e
    return model


def delete(db: Session, model: models.Base) -> None:
    try:
        db.delete(model)
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    return None
