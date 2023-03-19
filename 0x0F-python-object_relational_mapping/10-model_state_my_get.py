#!/usr/bin/python3
"""
This module contains a script that prints the State object
with the name passed as argument from the database hbtn_0e_6_usa

Example usage:
    $ python script.py <mysql username> <mysql password> <mysql database>
    <state_name>

Where:
    <mysql username>: username of mysql user.
    <mysql password>: password of mysql user.
    <mysql database>: database name in question.
    <state_name>: searchable state name.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import urllib.parse


def main(user, password, database, state_name, host='localhost'):
    """
    Prints  the State object with the name
    passed as argument from the database hbtn_0e_6_usa

    Args:
        user: username to connect to the database.
        password: password to connect to the database.
        database: name of the database to connect to.
        state_name: searchable state name.
        host: hostname of the database server (default: 'localhost').

    Returns:
        None.
    """
    engine = create_engine(f'mysql+mysqldb://{user}:'
                           f'{urllib.parse.quote_plus(password)}'
                           f'@{host}/{database}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()
    state = session.query(State).filter_by(name=state_name).first()
    if not state:
        print("Not found")
    else:
        print(state.id)


if __name__ == '__main__':
    user_input = sys.argv[1]
    password_input = sys.argv[2]
    database_input = sys.argv[3]
    state_name_input = sys.argv[4]
    main(user_input, password_input, database_input, state_name_input)
