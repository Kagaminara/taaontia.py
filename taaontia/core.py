import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from models import user


def hello():
    print("Hullo world!")


def init(db_path="taaontia.db", debug=False):
    engine = sqlalchemy.create_engine(
        f"sqlite:///{db_path}" if db_path else "sqlite://", echo=debug
    )
    return engine
