import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    #password="",
    database="perbankan"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM nasabah")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
