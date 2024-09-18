from sqlalchemy import Column, Integer, String, Float, DateTime
from database import *
from datetime import datetime



class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), index=True)
    email = Column(String(35), index=True)
    password = Column(String(50), index=True)
    created_at = Column(DateTime, default=datetime.utcnow)



class Book(Base):
    __tablename__ = "Books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    author = Column(String(255), index=True)
    price = Column(Integer)
    quantity = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)


