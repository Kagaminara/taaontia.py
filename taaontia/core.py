import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

from .models import user, statistics


class Taaontia:
    engine = None

    __Session = None

    def is_initialized(self):
        return self.engine is not None

    def get_new_session(self):
        return self.__Session() if self.__Session else None

    def init(self, db_path="sqlite:///taaontia.db", debug=False):
        self.engine = sqlalchemy.create_engine(
            f"{db_path}" if db_path else "sqlite://", echo=debug
        )
        self.__Session = sessionmaker()
        self.__Session.configure(bind=self.engine)
        Base.metadata.create_all(self.engine)
        return self.__Session

    def close(self, parameter_list):
        if self.engine:
            self.engine.dispose()
        pass

    def __repr__(self):
        return f"<Taaontia(connected={True if self.engine else False})>"

