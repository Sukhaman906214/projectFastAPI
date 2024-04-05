from sqlalchemy import Column, DateTime, Integer, String
from db import Base
from sqlalchemy import func

class enrty(Base):
    __tablename__ = "sinup"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    full_name = Column(String, index=True)
class JobSubmission():
    __tablename = "job_submission"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    job_title = Column(String, index=True)
    description = Column(String)
    deadline = Column(DateTime)
    priority = Column(String)
    submission_time = Column(DateTime, server_default=func.now())
