from .db_session import SqlAlchemyBase
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean
import datetime
from sqlalchemy.orm import relationship


class Jobs(SqlAlchemyBase):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    team_leader = Column(ForeignKey("users.id"))
    job = Column(String, nullable=True)
    collaborators = Column(String, nullable=True)
    work_size = Column(Integer, nullable=True)
    position = Column(String, nullable=True)
    start_data = Column(DateTime,
                        nullable=True, default=datetime.datetime.now)
    end_date = Column(DateTime,
                        nullable=True)
    is_finished = Column(Boolean, default=True)
    user = relationship("User")