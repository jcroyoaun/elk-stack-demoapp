from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

db_service_name = os.getenv("DB_SERVICE_NAME", "default_db_service")
database_name = os.getenv("DATABASE_NAME", "elk_demo_metrics")

SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:root@{db_service_name}:5432/{database_name}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

