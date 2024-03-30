from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///./lg.db"
# Create the database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
