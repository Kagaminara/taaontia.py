import sqlalchemy
from .exception import TaaontiaNotInitializedException
from sqlalchemy.orm import sessionmaker
from .db.utils import Base
from .models import User, Statistics


class Taaontia:
    engine = None

    __Session = None

    def is_initialized(self):
        return self.engine is not None

    def get_new_session(self):
        return self.__Session() if self.__Session else None

    def create_user(self, session, username, password, auth_key=None):
        user = User(auth_key=auth_key, username=username, password=password)
        session.add(user)
        session.commit()
        return user

    def connect(self, auth_key=None, username=None, password=None):
        if not self.is_initialized():
            raise TaaontiaNotInitializedException()
        session = self.get_new_session()
        user = None
        if auth_key:
            user = session.query(User).filter(User.auth_key == auth_key).first()
            if not user and username and password:
                user = self.create_user(session, username, password, auth_key)
            if not user:
                return None
        if not user and username and password:
            user = (
                session.query(User)
                .filter(User.username == username, User.password == password)
                .first()
            )
        if not user:
            user = self.create_user(session, username, password, auth_key=auth_key)
        return user.auth_key

    def init(self, db_path="sqlite:///taaontia.db", debug=False):
        self.engine = sqlalchemy.create_engine(db_path or "sqlite://", echo=debug)
        self.__Session = sessionmaker()
        self.__Session.configure(bind=self.engine)
        Base.metadata.create_all(self.engine)
        return True

    def close(self):
        if self.engine:
            self.engine.dispose()
        pass

    def __repr__(self):
        return f"<Taaontia(connected={True if self.engine else False})>"

