import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="lab22",
)
mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES;")
print(mycursor.fetchall())