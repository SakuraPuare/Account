# coding=utf-8
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# from database.models import *


database_url = os.getenv('DATABASE_URL')
if not database_url:
    raise Exception('DATABASE_URL not found in .env')

db_engine = create_engine(database_url, echo=True)
db_session = sessionmaker(bind=db_engine)

Base = declarative_base()

# class DataBase:
#     database_url: str = ''
#
#     def __init__(self):
#         super().__init__()
#         self.__load_env()
#
#     @classmethod
#     def init(cls, echo: bool = True, is_dispose=False):
#         self = cls()
#
#         self.engine = create_engine(self.database_url, echo=echo)
#         self.session = create_session(bind=self.engine)
#
#         if is_dispose:
#             Base.metadata.drop_all(self.engine)
#         Base.metadata.create_all(self.engine)
#
#         return self
#
#     def __load_env(self):
#         if not self.database_url:
#             database_url = os.getenv('DATABASE_URL')
#             if database_url:
#                 self.database_url = database_url
#             else:
#                 self.database_url = 'mysql://root:20131114@localhost:3306/account?charset=utf8mb4'
#                 # raise Exception('DATABASE_URL not found in .env')
#
#     def close(self) -> None:
#         self.session.close()
#
#
# class DataBaseAsync(DataBase):
#     database_url = 'mysql+aiomysql://root:20131114@localhost:3306/account?charset=utf8mb4'
#     def __init__(self):
#         super().__init__()
#
#     @classmethod
#     def init(cls, echo: bool = True, is_dispose=False):
#         self = cls()
#         self.engine = create_async_engine(self.database_url, echo=echo)
#
#         asyncio.run(self.__create_all(is_dispose=is_dispose))
#         return self
#
#     async def __create_all(self, is_dispose=False):
#         async with self.engine.begin() as conn:
#             if is_dispose:
#                 await conn.run_sync(Base.metadata.drop_all)
#             await conn.run_sync(Base.metadata.create_all)
#
# class DataBase:
#     database_url: str = ''
#
#     def __init__(self, echo: bool = True, is_dispose=False):
#         super().__init__()
#         self.__load_env()
#
#         self.init(echo=echo, is_dispose=is_dispose)
#
#     def init(self, echo: bool = True, is_dispose=False):
#         self.engine = create_engine(self.database_url, echo=echo)
#         self.session = create_session(bind=self.engine)
#
#         if is_dispose:
#             Base.metadata.drop_all(self.engine)
#         Base.metadata.create_all(self.engine)
#
#         return self
#
#     def close(self) -> None:
#         self.session.close()
#         self.engine.dispose()
#
#     def query(self, obj: Base):
#         try:
#             return self.session.query(obj)
#         except Exception as e:
#             self.session.rollback()
#             raise e
#
#     def insert(self, data: Iterable | Base):
#         if not isinstance(data, Iterable):
#             data = [data]
#         try:
#             self.session.add_all(data)
#             self.session.commit()
#         except Exception as e:
#             self.session.rollback()
#             raise e
#
#     def __load_env(self):
#         if not self.database_url:
#             database_url = os.getenv('DATABASE_URL')
#             if database_url:
#                 self.database_url = database_url
#             else:
#                 raise Exception('DATABASE_URL not found in .env')
#
#
# if __name__ == '__main__':
#     # db_async = DataBaseAsync.init()
#     # db = DataBase.init()
#     db = DataBase()
#     print(db.database_url)
#
# db = DataBase(echo=False)
