from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@localhost/"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()
