import mysql.connector

def initConnection():
    mydb = mysql.connector(
        host="localhost",
        user="milo",
        password="hello"
    )