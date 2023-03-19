#!/usr/bin/python3
"""
Create a State model that inherits from
Base and links to the MySQL table states.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents a state table for a MySQL database.
    __tablename__ (str): The name of table.
    id (sqlalchemy.Integer): The state's id and primary key.
    name (sqlalchemy.String): The state's name and cannot be null.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state', cascade="all, delete")
