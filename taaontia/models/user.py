from sqlalchemy import Column, Integer, String
from taaontia.core import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name})>"
