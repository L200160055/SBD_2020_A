from tkinter import *

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="servismobil"
)

root=Tk()
root.title("Servis Mobil/ Transaksi")
root.geometry("500x500")

def tambah():
    nomor=e1.get()
    tanggal=e2.get()
    idMobil=e3.get()
    idJenisLayanan=e4.get()
    hargaLayanan=e5.get()

    mycursor = mydb.cursor()
    sql = "INSERT INTO transaksi(nomorTransaksi, tanggalTransaksi, idMobilFK, idJenisLayananFK, hargaLayanan) VALUES (%s,%s,%s,%s,%s)"
    val = (nomor, tanggal, idMobil, idJenisLayanan, hargaLayanan)
    mycursor.execute(sql, val)
    mydb.commit()

    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)

def lihat():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM transaksi")
    myresult = mycursor.fetchall()

    result=""
    for myresult in myresult:
        result +=str(myresult[0])+"\t"+str(myresult[1])+"\t"+str(myresult[2])+"\t"+str(myresult[3])+"\t\t"+str(myresult[4])+"\n"

    ll=Label(root, text="Nomor"+"\t"+"Tanggal"+"\t"+"ID Mobil"+"\t"+"ID Layanan"+"\t"+"Harga"+"\n"+result,justify=LEFT)
    ll.grid(row=11, column=0, columnspan=2, padx=10)
    
    mydb.commit()
    
def perbarui():
    pilihID=e6.get()
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM transaksi WHERE nomorTransaksi="+pilihID)
    myresult = mycursor.fetchall()

    for myresult in myresult:
        ep1.insert(0, myresult[0])
        ep2.insert(0, myresult[1])
        ep3.insert(0, myresult[2])
        ep4.insert(0, myresult[3])
        ep5.insert(0, myresult[4])
    mydb.commit()

    e6.delete(0,END)

def simpan():
    nomor=ep1.get()
    tanggal=ep2.get()
    idMobil=ep3.get()
    idJenisLayanan=ep4.get()
    hargaLayanan=ep5.get()

    mycursor = mydb.cursor()
    sql = "UPDATE transaksi SET tanggalTransaksi=%s, idMobilFK=%s, idJenisLayananFK=%s, hargaLayanan=%s WHERE nomorTransaksi= %s"
    val = (tanggal, idMobil, idJenisLayanan, hargaLayanan, nomor)
    mycursor.execute(sql, val)
    mydb.commit()

    ep1.delete(0,END)
    ep2.delete(0,END)
    ep3.delete(0,END)
    ep4.delete(0,END)
    ep5.delete(0,END)

def hapus():
    pilihID=e6.get()

    mycursor = mydb.cursor()
    sql = "DELETE FROM transaksi WHERE nomorTransaksi="+pilihID
    mycursor.execute(sql)
    mydb.commit()

    e6.delete(0,END)

#Tambah
l0=Label(root, text="Tambah", font=(None,12,"bold"))
l0.grid(row=0, column=0, pady=10)

l1=Label(root, text="Nomor")
l1.grid(row=1, column=0, padx=10, pady=5, sticky="w")
e1=Entry(root, width=25)
e1.grid(row=1, column=1)

l2=Label(root, text="Tanggal")
l2.grid(row=2, column=0, padx=10, pady=5, sticky="w")
e2=Entry(root, width=25)
e2.grid(row=2, column=1)

l3=Label(root, text="ID Mobil")
l3.grid(row=3, column=0, padx=10, pady=5, sticky="w")
e3=Entry(root, width=25)
e3.grid(row=3, column=1)

l4=Label(root, text="ID Layanan")
l4.grid(row=4, column=0, padx=10, pady=5, sticky="w")
e4=Entry(root, width=25)
e4.grid(row=4, column=1)

l5=Label(root, text="Harga Layanan")
l5.grid(row=5, column=0, padx=10, pady=5, sticky="w")
e5=Entry(root, width=25)
e5.grid(row=5, column=1)

b1=Button(root, text="Tambah", command=tambah, width=21)
b1.grid(row=6, column=1, columnspan=1, padx=10, pady=5)

b2=Button(root, text="Lihat", command=lihat, width=21)
b2.grid(row=7, column=1, columnspan=1, padx=10, pady=5)

l6=Label(root, text="Pilih ID")
l6.grid(row=8, column=0, padx=10, pady=5, sticky="w")
e6=Entry(root, width=25)
e6.grid(row=8, column=1)

b3=Button(root, text="Perbarui", command=perbarui, width=21)
b3.grid(row=9, column=1, columnspan=1, padx=10, pady=5)

b4=Button(root, text="Hapus", command=hapus, width=21)
b4.grid(row=10, column=1, columnspan=1, padx=10, pady=5)

#Perbarui
lp0=Label(root, text="Perbarui", font=(None,12,"bold"))
lp0.grid(row=0, column=4)

ep1=Entry(root, width=25)
ep1.grid(row=1, column=4, padx=20)

ep2=Entry(root, width=25)
ep2.grid(row=2, column=4)

ep3=Entry(root, width=25)
ep3.grid(row=3, column=4)

ep4=Entry(root, width=25)
ep4.grid(row=4, column=4)

ep5=Entry(root, width=25)
ep5.grid(row=5, column=4)

bp1=Button(root, text="Simpan", command=simpan, width=21)
bp1.grid(row=6, column=4)

root.mainloop()