import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  #password="",
  database="perbankan"
)

mycursor = mydb.cursor()

sql = "DELETE FROM nasabah WHERE id_nasabah = '12'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record deleted")