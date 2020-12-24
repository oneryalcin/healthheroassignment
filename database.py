from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Numeric, String, DateTime

from config import DB_FILE

# Engine to my Sqlite db
engine = create_engine(f'sqlite:///{DB_FILE}')

# Create session object for ORM
Session = sessionmaker(bind=engine)
session = Session()

# Model Base
Base = declarative_base()

class Word(Base):
    """words table
    """
    __tablename__ = 'words'

    word  = Column(String(255), primary_key=True)
    numVowels = Column(Integer())
    numConsonants = Column(Integer())
    createdOn = Column(DateTime)
