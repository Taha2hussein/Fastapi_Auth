import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Falls back to your local Postgres (pgAdmin4) URL when DATABASE_URL isn't set.
# Inside docker-compose, DATABASE_URL is injected and points at the "db" service.
DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://macos@localhost:5433/practice_fastapi"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
