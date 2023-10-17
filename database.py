from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///note.db', echo=True)
Base = declarative_base()

metadata = MetaData()

class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True)
    task = Column(String)
    desc = Column(String)



Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)