import mysql.connector
from mysql.connector import Error

class Database:
    _connection = None
    _cursor = None

    @staticmethod
    def get_connection():
        if Database._connection is None:
            try:
                Database._connection = mysql.connector.connect(
                    host="localhost",  # Replace with your host
                    user="root",       # Replace with your username
                    password="0141",       # Replace with your password
                    database="test"  # Replace with your database name
                )
                if Database._connection.is_connected():
                    print("Database connected successfully.")
            except Error as e:
                print(f"Error connecting to MySQL: {e}")
        return Database._connection

    @staticmethod
    def cursor():
        if Database._cursor is None:
            if Database.get_connection():
                Database._cursor = Database._connection.cursor()
        return Database._cursor

    @staticmethod
    def close_connection():
        if Database._connection and Database._connection.is_connected():
            Database._cursor.close()
            Database._connection.close()
            Database._connection = None
            Database._cursor = None
            print("Database connection closed.")

    @staticmethod
    def commit():
        Database._connection.commit()
