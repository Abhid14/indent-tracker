import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="lab22",
)

print(mydb)
