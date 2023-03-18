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
import MySQLdb


class DBConnector:
    """
    A class for creating a MySQL database
    connection and executing queries.
    """

    def __init__(self, username, password, database, host='localhost'):
        """
        Constructs a new DBConnector instance.

        Args:
            username: MySQL username
            password: MySQL password
            database: MySQL database name
            host: MySQL host name (default 'localhost')
        """
        self.username = username
        self.password = password
        self.database = database
        self.host = host

    def db_cursor(self):
        """
        Cursor object to execute
        queries on the MySQL database.

        Returns:
            A MySQLdb cursor object.
        """
        db = MySQLdb.connect(user=self.username,
                             password=self.password,
                             database=self.database,
                             host=self.host)
        return db.cursor()

    def db_query(self, sql_string):
        """
        Executes a raw query on the MySQL database and returns the rows.
        Args:
                sql_string: raw query to execute.
        Returns:
                All rows affected.
        """
        cursor = self.db_cursor()
        cursor.execute(sql_string)
        return cursor.fetchall()


def main(user, password, database, host='localhost'):
    """
        Sets up a MySQL database connection and tests the
        connection by executing a query
        on the 'states' table fetching all states
        and ordering them in ascending order by id.

        Args:
            user: MySQL username
            password: MySQL password
            database: MySQL database name
            host: MySQL host name (default 'localhost')
        """
    db_instance = DBConnector(username=user,
                              password=password,
                              database=database,
                              host=host)
    results = db_instance.db_query('SELECT * FROM states ORDER BY id ASC;')
    for row in results:
        print(row)


if __name__ == '__main__':
    user_input = sys.argv[1]
    password_input = sys.argv[2]
    database_input = sys.argv[3]
    main(user_input, password_input, database_input)
