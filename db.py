from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
DATABASE_URL = "sqlite:///./lg.db"
# Create the database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
#Sessional class to interact withh the database
SessionalLocal = sessionmaker(autocommit= False ,autoflush=False, bind=engine)
#Declarative Base for ORM 
Base  = declarative_base()
