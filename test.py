import mysql.connector
try:
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="system@123",
        database="aiml1"
    )
    if conn.is_connected():
        print("connected to the database")
    else:
        print("failed to connect the database")
except mysql.connector.Error as err:
        print(err)
finally:
        if conn.is_connected():
            conn.close()
            print("connection closed")