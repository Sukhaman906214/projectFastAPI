from sqlalchemy import Column, DateTime, Integer, String
from db import Base
class enrty(Base):
    __tablename__ = "sinup"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    full_name = Column(String, index=True)
