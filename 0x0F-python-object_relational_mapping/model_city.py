#!/usr/bin/python3
""" class definition of a City."""

from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base


class City(Base):
    """city class"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
