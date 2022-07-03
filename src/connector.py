import sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker

DATABASE = "postgresql"
USER = "pysqlal"
PASSWORD = "pysqlal"
HOST = "localhost"
PORT = "5432"
DB_NAME = "pysqlal"

CONN_STR = f"{DATABASE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

engine = sqlalchemy.create_engine(CONN_STR)

session = scoped_session(sessionmaker(engine, autocommit=False, autoflush=False))
