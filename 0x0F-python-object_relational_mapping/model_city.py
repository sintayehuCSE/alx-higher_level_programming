#!/usr/bin/python3
"""
Declares and mapps the City class to its table in DB
"""
from model_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))
