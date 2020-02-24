from datetime import  datetime
from sqlalchemy.orm import mapper
from sqlalchemy import Column, Integer, DateTime, String

from database import Base



class Message(Base):
    __tablename__='messages'

    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(String, nullable=True)
    created = Column(DateTime, default=datetime.now())

