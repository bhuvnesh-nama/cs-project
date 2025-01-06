# This file contains all the database related functions
import mysql.connector
from mysql.connector import Error

DATABASE = {
    "host": "localhost",
    "user": "root",
    "password": "0141",
    "database": "port_management"
}

# for database operations
class Database:
    _connection = None
    _cursor = None

    # To connect
    @staticmethod
    def get_connection():
        if Database._connection is None:
            try:
                Database._connection = mysql.connector.connect(
                    host=DATABASE["host"],
                    user=DATABASE["user"],
                    password=DATABASE["password"],
                    database=DATABASE["database"]
                )
                if Database._connection.is_connected():
                    print("Database connected successfully.")
            except Error as e:
                print(f"Error connecting to MySQL: {e}")
                exit()
        return Database._connection

    # To create cursor
    @staticmethod
    def cursor():
        if Database._cursor is None:
            if Database.get_connection():
                Database._cursor = Database._connection.cursor()
        return Database._cursor

    # To close connection
    @staticmethod
    def close_connection():
        if Database._connection and Database._connection.is_connected():
            Database._cursor.close()
            Database._connection.close()
            Database._connection = None
            Database._cursor = None
            print("Database connection closed.")

    # To commit in database
    @staticmethod
    def commit():
        Database._connection.commit()
