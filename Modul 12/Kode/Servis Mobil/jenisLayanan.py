from tkinter import *

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="servismobil"
)

root=Tk()
root.title("Servis Mobil/ Jenis Layanan")
root.geometry("500x500")

def tambah():
    id=e1.get()
    nama=e2.get()
    informasi=e3.get()
    harga=e4.get()

    mycursor = mydb.cursor()
    sql = "INSERT INTO jenisLayanan (idJenisLayanan, namaLayanan, informasiLayanan, hargaLayanan) VALUES (%s,%s,%s,%s)"
    val = (id, nama, informasi, harga)
    mycursor.execute(sql, val)
    mydb.commit()

    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

def lihat():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM jenisLayanan")
    myresult = mycursor.fetchall()

    result=""
    for myresult in myresult:
        result +=str(myresult[0])+"\t"+str(myresult[1])+"\t"+str(myresult[2])+"\t\t"+str(myresult[3])+"\n"

    ll=Label(root, text="ID"+"\t"+"Nama"+"\t"+"Informasi"+"\t"+"Harga"+"\n"+result,justify=LEFT)
    ll.grid(row=10, column=0, columnspan=2, padx=10)
    
    mydb.commit()
    
def perbarui():
    pilihID=e5.get()
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM jenisLayanan WHERE idJenisLayanan="+pilihID)
    myresult = mycursor.fetchall()

    for myresult in myresult:
        ep1.insert(0, myresult[0])
        ep2.insert(0, myresult[1])
        ep3.insert(0, myresult[2])
        ep4.insert(0, myresult[3])
    mydb.commit()

    e5.delete(0,END)

def simpan():
    id=ep1.get()
    namaBaru=ep2.get()
    informasiBaru=ep3.get()
    hargaBaru=ep4.get()

    mycursor = mydb.cursor()
    sql = "UPDATE jenisLayanan SET namaLayanan=%s, informasiLayanan=%s, hargaLayanan=%s WHERE idJenisLayanan = %s"
    val = (namaBaru, informasiBaru, hargaBaru, id)
    mycursor.execute(sql, val)
    mydb.commit()

    ep1.delete(0,END)
    ep2.delete(0,END)
    ep3.delete(0,END)
    ep4.delete(0,END)

def hapus():
    pilihID=e5.get()

    mycursor = mydb.cursor()
    sql = "DELETE FROM jenisLayanan WHERE idJenisLayanan="+pilihID
    mycursor.execute(sql)
    mydb.commit()

    e5.delete(0,END)

#Tambah
l0=Label(root, text="Tambah", font=(None,12,"bold"))
l0.grid(row=0, column=1, pady=10)

l1=Label(root, text="ID")
l1.grid(row=1, column=0, padx=10, pady=5, sticky="w")
e1=Entry(root, width=25)
e1.grid(row=1, column=1)

l2=Label(root, text="Nama")
l2.grid(row=2, column=0, padx=10, pady=5, sticky="w")
e2=Entry(root, width=25)
e2.grid(row=2, column=1)

l3=Label(root, text="Informasi")
l3.grid(row=3, column=0, padx=10, pady=5, sticky="w")
e3=Entry(root, width=25)
e3.grid(row=3, column=1)

l4=Label(root, text="Harga")
l4.grid(row=4, column=0, padx=10, pady=5, sticky="w")
e4=Entry(root, width=25)
e4.grid(row=4, column=1)

b1=Button(root, text="Tambah", command=tambah, width=21)
b1.grid(row=5, column=1, columnspan=1, padx=10, pady=5)

b2=Button(root, text="Lihat", command=lihat, width=21)
b2.grid(row=6, column=1, columnspan=1, padx=10, pady=5)

l5=Label(root, text="Pilih ID")
l5.grid(row=7, column=0, padx=10, pady=5)
e5=Entry(root, width=25)
e5.grid(row=7, column=1)

b3=Button(root, text="Perbarui", command=perbarui, width=21)
b3.grid(row=8, column=1, columnspan=1, padx=10, pady=5)

b4=Button(root, text="Hapus", command=hapus, width=21)
b4.grid(row=9, column=1, columnspan=1, padx=10, pady=5)

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

bp1=Button(root, text="Simpan", command=simpan, width=21)
bp1.grid(row=5, column=4)

root.mainloop()