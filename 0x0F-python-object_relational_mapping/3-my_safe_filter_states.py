#!/usr/bin/python3
"""
This script sets up a MySQL database connection using the provided
credentials and tests the connection by executing
a query on the 'states' table.

Usage:
    ./script.py <mysql username> <mysql password> <mysql database> \
    <state name searched>

Args:
    mysql username: MySQL username
    mysql password: MySQL password
    mysql database: MySQL database name
    state name searched: MySQL record to be searched
"""
import sys
import importlib
import MySQLdb

states_module = importlib.import_module('0-select_states')


def is_valid_input(input_str):
    """
    Catches attempted  SQL injections
    """
    sql_keywords = ["SELECT", "UPDATE", "DELETE",
                    "DROP", "INSERT", "ALTER", "CREATE"]
    if any(keyword in input_str.upper() for keyword in sql_keywords):
        return False
    if ";" in input_str:
        return False
    return True


def main(user, password, database, state_name, host='localhost'):
    """
        Sets up a MySQL database connection and tests the
        connection by executing a query
        on the 'states' table fetching all states
        and ordering them in ascending order by id and
        fetching state name provided during program call.

        Args:
            user: MySQL username
            password: MySQL password
            database: MySQL database name
            state_name: state name to be queried
            host: MySQL host name (default 'localhost')
        """
    db_instance = states_module.DBConnector(username=user,
                                            password=password,
                                            database=database,
                                            host=host)
    if is_valid_input(state_name):
        results = db_instance.db_query("SELECT * FROM states "
                                       "WHERE BINARY name = '{}';".format(
                                        state_name))
        for row in results:
            print(row)
    else:
        return


if __name__ == '__main__':
    user_input = sys.argv[1]
    password_input = sys.argv[2]
    database_input = sys.argv[3]
    state_name_input = sys.argv[4]
    main(user_input, password_input, database_input, state_name_input)
