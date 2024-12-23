import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", passwd="0141",database="test")
if conn.is_connected():
    print("conntected to db")
