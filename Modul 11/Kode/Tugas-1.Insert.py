import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  #password="",
  database="perbankan"
)

mycursor = mydb.cursor()

sql = "INSERT INTO nasabah (id_nasabah, nama_nasabah, alamat_nasabah) VALUES (%s,%s, %s)"
val = ("12", "L200160055", "Solo")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
