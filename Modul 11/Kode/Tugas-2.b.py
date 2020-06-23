import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    #password="",
    database="perbankan"
)

mycursor = mydb.cursor()

mycursor.execute("""SELECT * FROM nasabah WHERE nasabah.id_nasabah 
                IN (SELECT transaksi.id_nasabahFK FROM transaksi WHERE tanggal BETWEEN '2009-10-1' AND '2009-12-31' )""")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
