import os
from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine, Session
from models.item import Item  # <-- forces Item to register with SQLModel.metadata

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in .env")

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session