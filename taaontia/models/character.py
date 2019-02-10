from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from taaontia.core import Base

class Character(Base):
    __tablename__ = "character"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))

    user = relationship("User", back_populates="character")

    def __repr__(self):
        return f"<Character(id={self.id}, name={self.name})>"
