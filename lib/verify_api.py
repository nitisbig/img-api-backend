import os
from fastapi import HTTPException, Security, Depends
from fastapi.security import APIKeyHeader

from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
load_dotenv()


DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class APIKey(Base):
    __tablename__ = 'api_key'
    id = Column(Integer, primary_key=True, index=True)
    token = Column(String, unique=True, index=True) 
    is_active = Column(Boolean, default=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify(key: str = Security(APIKeyHeader(name='x-key', auto_error=False)), db: Session = Depends(get_db)):
    if not key:
        raise HTTPException(
            status_code=401,
            detail='Missing api key header'
        )
    
    db_key = db.query(APIKey).filter(
        APIKey.token == key,
        APIKey.is_active == True
    ).first()
    
    db.commit()

    if not db_key:
        raise HTTPException(
            status_code=401,
            detail='invalid or inactive key'
        )
    return db_key