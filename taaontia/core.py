import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
Session = None
userId = None

from .models import user, statistics


def init(db_path="taaontia.db", debug=False):
    engine = sqlalchemy.create_engine(
        f"sqlite:///{db_path}" if db_path else "sqlite://", echo=debug
    )
    Session = sessionmaker()
    Session.configure(bind=engine)
    Base.metadata.create_all(engine)
    return Session
