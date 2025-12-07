from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql+psycopg2://postgres:nitesh@34.90.21.177:5433/postgres"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

api_record = SessionLocal().query().filter()