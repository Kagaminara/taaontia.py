from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from taaontia.db.utils import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    statistics = relationship("Statistics", uselist=False, back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name})>"
