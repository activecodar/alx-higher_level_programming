#!/usr/bin/python3
"""
Create a City model that inherits from
Base and links to the MySQL table states.
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    Represents a city table for a MySQL database.
    __tablename__ (str): The name of table.
    id (sqlalchemy.Integer): The city's id and primary key.
    name (sqlalchemy.String): The city's name and cannot be null.
    state_id (sqlalchemy.String): The city's FK relation with state.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('user.id'), nullable=False)
