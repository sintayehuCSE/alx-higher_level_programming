#!/usr/bin/pyhton3
"""Articulate definition of class State using
declarative system of SQLAlchemy ORM."""
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from sys import argv


engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                       .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)
