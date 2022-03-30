import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


APP_NAME = ''
Base = declarative_base()


def config_db():
    
    db_path = os.getenv(f'DB_PATH')
    db_user = os.getenv(f'DB_USER')
    db_pass = os.getenv(f'DB_PASS')
    db_name = os.getenv(f'DB_NAME')

    db_uri = f'postgresql://{db_user}:{db_pass}@{db_path}/{db_name}'
    
    return db_uri


def create_db():
    from src.models.database import all
    
    db_uri = config_db()
    
    engine = create_engine(db_uri, echo=True)
    Base.metadata.create_all(bind=engine)


def connect():
    db_uri = config_db()
    
    if APP_NAME:
        db_uri += f'?application_name={APP_NAME}'
    
    engine = create_engine(db_uri, echo=False)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    return SessionLocal()
