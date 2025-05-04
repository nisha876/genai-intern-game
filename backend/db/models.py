from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Guess(Base):
    __tablename__ = 'guesses'

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, index=True)
    guess = Column(String)
    verdict = Column(String)


