from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
base = declarative_base()
class students(base) :
    __tablename__ = "Csea"
    id = column(Integer,primarykey())
    name = column(string)
    rollno = column(string)
    section = column(string)
engine = create_engine("sqlite:///mydb.db")
base.metadata.create_all(engine)
session = sessionmaker(bind = True)
s = session()
s.commit()