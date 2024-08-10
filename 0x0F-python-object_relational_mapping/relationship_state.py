#!/usr/bin/python3
"""Articulate definition of class State using
declarative system of SQLAlchemy ORM."""
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class State(Base):
    """
    Class with id and name attribute of each State
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates='state',
                          cascade='all, delete, delete-orphan')
