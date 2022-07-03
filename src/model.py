from datetime import datetime

from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import DateTime, Integer, String

from connector import engine, session

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    password = Column(String(50))
    created_at = Column(DateTime(timezone=False), default=datetime.now())
    updated_at = Column(DateTime(timezone=False), default=datetime.now())


Base.metadata.create_all(engine)

# insert
user_new = User()
user_new.name = "hoge"
user_new.password = "fuga"
session.add(user_new)
session.commit()
