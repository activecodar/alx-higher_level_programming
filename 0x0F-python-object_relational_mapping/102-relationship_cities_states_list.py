#!/usr/bin/python3
"""
This module contains a script
that lists all City objects from the database hbtn_0e_101_usa

Example usage:
    $ python script.py <mysql username> <mysql password> <mysql database>

Where:
    <mysql username>: username of mysql user.
    <mysql password>: password of mysql user.
    <mysql database>: database name in question.
"""

import sys
import warnings
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
import urllib.parse


def main(user, password, database, host='localhost'):
    """
    Lists all City objects from the database hbtn_0e_101_usa

    Args:
        user: username to connect to the database.
        password: password to connect to the database.
        database: name of the database to connect to.
        host: hostname of the database server (default: 'localhost').

    Returns:
        None.
    """
    # Ignore SQLAlchemy warnings
    warnings.filterwarnings("ignore", category=exc.SAWarning)
    engine = create_engine(f'mysql+mysqldb://{user}:'
                           f'{urllib.parse.quote_plus(password)}'
                           f'@{host}/{database}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")


if __name__ == '__main__':
    user_input = sys.argv[1]
    password_input = sys.argv[2]
    database_input = sys.argv[3]
    main(user_input, password_input, database_input)
