#!/usr/bin/python3
"""
This script sets up a MySQL database connection using the provided
credentials and tests the connection by executing a query on the 'states' table.

Usage:
    ./script.py <mysql username> <mysql password> <mysql database>

Args:
    mysql username: MySQL username
    mysql password: MySQL password
    mysql database: MySQL database name
"""
import sys
import MySQLdb


def setup_db(user, password, database, host='localhost'):
    """
        Sets up a MySQL database connection and tests the connection by executing a query
        on the 'states' table.

        Args:
            user: MySQL username
            password: MySQL password
            database: MySQL database name
            host: MySQL host name (default 'localhost')
        """
    db = MySQLdb.connect(host=host, user=user, password=password, database=database)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER BY id ASC;')
    results = cursor.fetchall()
    for row in results:
        print(row)


if __name__ == '__main__':
    user_input = sys.argv[1]
    password_input = sys.argv[2]
    database_input = sys.argv[3]
    setup_db(user_input, password_input, database_input)
