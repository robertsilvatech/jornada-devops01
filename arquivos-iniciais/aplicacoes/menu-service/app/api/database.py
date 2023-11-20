from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config

POSTGRES_USER=config('POSTGRES_USER')
POSTGRES_PASSWORD=config('POSTGRES_PASSWORD')
POSTGRES_SERVER=config('POSTGRES_SERVER')
POSTGRES_PORT=config('POSTGRES_PORT')
POSTGRES_DB=config('POSTGRES_DB')

DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()