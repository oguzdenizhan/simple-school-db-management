import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password= "YourPassword",
    database = "schooldb"
)