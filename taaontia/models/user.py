from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy_utils.types.password import PasswordType
from sqlalchemy_utils.types.uuid import UUIDType
from sqlalchemy.orm import relationship
from taaontia.db.utils import Base
from uuid import uuid4


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    auth_key = Column(UUIDType(), nullable=False, default=uuid4, unique=True)
    username = Column(String, nullable=False)
    password = Column(PasswordType(schemes=["pbkdf2_sha512", "md5_crypt"]), nullable=False)

    statistics = relationship("Statistics", uselist=False, back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, name={self.username})>"
