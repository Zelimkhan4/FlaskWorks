from .db_session import SqlAlchemyBase
from sqlalchemy import Column, String, Integer, DateTime
from flask_login import UserMixin
import datetime
from sqlalchemy.orm import relationship
from werkzeug.security import check_password_hash, generate_password_hash



class User(SqlAlchemyBase, UserMixin):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    surname = Column(String, nullable=True)
    name = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    position = Column(String, nullable=True)
    speciality = Column(String, nullable=True)
    address = Column(String, nullable=True)
    email = Column(String, nullable=True)
    hashed_password = Column(String, nullable=True)
    modified_date = Column(DateTime,
                           nullable=True, default=datetime.datetime.now)
    jobs = relationship("Jobs", back_populates='user')

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def set_password(self, password):
        print("here")
        self.hashed_password = generate_password_hash(password)