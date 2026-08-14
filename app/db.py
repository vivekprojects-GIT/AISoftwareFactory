# Database setup

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Answer(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True)
    question = Column(String)
    sql_query = Column(String)
    result_count = Column(Integer)
    conversation_id = Column(Integer, ForeignKey('conversations.id'))

class Conversation(Base):
    __tablename__ = 'conversations'
    id = Column(Integer, primary_key=True)
    answers = relationship('Answer', backref='conversation')

DATABASE_URL = "sqlite:///./test.db"
echo = False
engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False}, echo=echo)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()