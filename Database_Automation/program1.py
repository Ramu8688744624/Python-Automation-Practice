import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="automation_db"
        )
    print("Database connected successfully")
    conn.close()
except Exception as e:
    print("Connection Failed: ", e)