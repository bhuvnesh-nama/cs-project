import mysql.connector
from mysql.connector import Error

DATABASE = {
    "host": "localhost",
    "user": "root",
    "password": "0141",
    "database": "port_management"
}

class Database:
    _connection = None
    _cursor = None

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
