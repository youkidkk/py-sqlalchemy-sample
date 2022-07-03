import sqlalchemy

DATABASE = "postgresql"
USER = "pysqlal"
PASSWORD = "pysqlal"
HOST = "localhost"
PORT = "5432"
DB_NAME = "pysqlal"

CONN_STR = f"{DATABASE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

engine = sqlalchemy.create_engine(CONN_STR)

engine.execute("insert into test (text) values ('ttt');")
