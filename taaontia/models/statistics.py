from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from taaontia.db.utils import Base
from taaontia.models.user import User


class Statistics(Base):
    __tablename__ = "statistics"

    id = Column(Integer, primary_key=True)
    command_count = Column(Integer, default=0)

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="statistics")

    def __repr__(self):
        return f"<Statistics(id={self.id}, command_count={self.command_count})>"

