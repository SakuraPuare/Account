from database import db_session


def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close()
