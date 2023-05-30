# coding=utf-8
from database import db_session, db_engine
from database.crud.user import create_user
from database.models import *
from utils.config import load_env
from utils.encryption import generate_hash_password, generate_md5

dotenv = f""""""

if __name__ == '__main__':
    load_env()

    engine = db_engine
    db = db_session()
    # drop and create all table
    Base.metadata.drop_all(db_engine)
    Base.metadata.create_all(db_engine)

    # write encrypt key

    # write to user table
    admin = User(username='admin', email='java20131114@gmail.com', email_md5=generate_md5('java20131114@gmail.com'),
                 email_verified_at=datetime.datetime.now(),
                 encrypted_password=generate_hash_password('123456'), is_superuser=True)
    create_user(db, admin)

    # write to user_token table
    # create_user_token(db, admin)
