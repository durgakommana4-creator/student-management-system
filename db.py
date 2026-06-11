import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mahadev11",
    database="student_db"
)

cursor = conn.cursor()