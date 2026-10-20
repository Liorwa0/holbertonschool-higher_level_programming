#!/usr/bin/python3
"""
Contains the City class definition for SQLAlchemy ORM.
"""
from model_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class City(Base):
    """
    City class representing the cities table in MySQL.
    """
    __tablename__ = 'cities'
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        unique=True
    )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
