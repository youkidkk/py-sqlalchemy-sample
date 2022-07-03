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

user: User = session.query(User).first()
# insert
if not user:
    user = User()
    user.name = "hoge"
    user.password = "fuga"
    session.add(user)
    session.commit()

# update
user.password = "piyo"
user.updated_at = datetime.now()
session.commit()

# select
user = session.query(User).filter(User.name == "hoge").first()
if user:
    print(
        f"Name: {user.name}, Password: {user.password}, "
        f"Created at: {user.created_at}, Updated at: {user.updated_at}"
    )

# delete
session.delete(user)
session.commit()
