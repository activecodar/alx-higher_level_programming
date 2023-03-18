#!/usr/bin/python3
"""
This script sets up a MySQL database connection using the provided
credentials and tests the connection by executing
a query on the 'states' table.

Usage:
    ./script.py <mysql username> <mysql password> <mysql database>

Args:
    mysql username: MySQL username
    mysql password: MySQL password
    mysql database: MySQL database name
"""
import sys
import importlib
import MySQLdb
states_module = importlib.import_module('0-select_states')


def main(user, password, database, host='localhost'):
    """
        Sets up a MySQL database connection and tests the
        connection by executing a query
        on the 'states' table fetching all states
        and ordering them in ascending order by id and
        fetching records starting with N.

        Args:
            user: MySQL username
            password: MySQL password
            database: MySQL database name
            host: MySQL host name (default 'localhost')
        """
    db_instance = states_module.DBConnector(username=user,
                                            password=password,
                                            database=database,
                                            host=host)
    results = db_instance.db_query('SELECT * FROM states ORDER BY id ASC;')
    for row in results:
        if row[1][0] == 'N':
            print(row)


if __name__ == '__main__':
    user_input = sys.argv[1]
    password_input = sys.argv[2]
    database_input = sys.argv[3]
    main(user_input, password_input, database_input)
