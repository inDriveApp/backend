import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


APP_NAME = ''
db_path = os.getenv(f'DB_PATH')
db_user = os.getenv(f'DB_USER')
db_pass = os.getenv(f'DB_PASS')
db_name = os.getenv(f'DB_NAME')

DATABASE_URI = f'postgresql://{db_user}:{db_pass}@{db_path}/{db_name}'
Base = declarative_base()

def create_db():
    engine = create_engine(DATABASE_URI, echo=True)
    Base.metadata.create_all(bind=engine)


def connect():
    if APP_NAME:
        DATABASE_URI += f"?application_name={APP_NAME}"
    
    engine = create_engine(DATABASE_URI, echo=False)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    return SessionLocal()
