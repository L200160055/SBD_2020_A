from tkinter import *

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="servismobil"
)

root=Tk()
root.title("Servis Mobil/ Mobil")
root.geometry("500x500")

def tambah():
    id=e1.get()
    merk=e2.get()
    model=e3.get()
    tahun=e4.get()
    varian=e5.get()

    mycursor = mydb.cursor()

    sql = "INSERT INTO mobil (idMobil, merkMobil, modelMobil, tahunMobil, varianMobil) VALUES (%s,%s,%s,%s,%s)"
    val = (id, merk, model, tahun, varian)
    
    mycursor.execute(sql, val)

    mydb.commit()

    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)

def lihat():
    mycursor = mydb.cursor()
    
    mycursor.execute("SELECT * FROM mobil")

    myresult = mycursor.fetchall()

    result=""
    for myresult in myresult:
        result +=str(myresult[0])+"\t"+str(myresult[1])+"\t"+str(myresult[2])+"\t"+str(myresult[3])+"\t"+str(myresult[4])+"\n"

    ll=Label(root, text="ID"+"\t"+"Merk"+"\t"+"Tahun"+"\t"+"Model"+"\t"+"Versi"+"\n"+result,justify=LEFT)
    ll.grid(row=11, column=0, columnspan=4, padx=10)
    
    mydb.commit()
    
def perbarui():
    pilihID=e6.get()
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM mobil WHERE idMobil="+pilihID)
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
    id=ep1.get()
    merkBaru=ep2.get()
    modelBaru=ep3.get()
    tahunBaru=ep4.get()
    varianBaru=ep5.get()

    mycursor = mydb.cursor()
    sql = "UPDATE mobil SET merkMobil=%s, modelMobil=%s, tahunMobil=%s, varianMobil=%s WHERE idMobil = %s"
    val = (merkBaru, modelBaru, tahunBaru, varianBaru, id)
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
    sql = "DELETE FROM mobil WHERE idMobil="+pilihID
    mycursor.execute(sql)
    mydb.commit()

    e6.delete(0,END)

#Tambah
l0=Label(root, text="Tambah", font=(None,12,"bold"))
l0.grid(row=0, column=1, pady=10)

l1=Label(root, text="ID")
l1.grid(row=1, column=0, padx=10, pady=5, sticky="w")
e1=Entry(root, width=25)
e1.grid(row=1, column=1)

l2=Label(root, text="Merk")
l2.grid(row=2, column=0, padx=10, pady=5, sticky="w")
e2=Entry(root, width=25)
e2.grid(row=2, column=1)

l3=Label(root, text="Model")
l3.grid(row=3, column=0, padx=10, pady=5, sticky="w")
e3=Entry(root, width=25)
e3.grid(row=3, column=1)

l4=Label(root, text="Tahun")
l4.grid(row=4, column=0, padx=10, pady=5, sticky="w")
e4=Entry(root, width=25)
e4.grid(row=4, column=1)

l5=Label(root, text="Versi")
l5.grid(row=5, column=0, padx=10, pady=5, sticky="w")
e5=Entry(root, width=25)
e5.grid(row=5, column=1)

b1=Button(root, text="Tambah", command=tambah, width=21)
b1.grid(row=6, column=1, columnspan=1, padx=10, pady=5)

b2=Button(root, text="Lihat", command=lihat, width=21)
b2.grid(row=7, column=1, columnspan=1, padx=10, pady=5)

l6=Label(root, text="Pilih ID")
l6.grid(row=8, column=0, padx=10, pady=5)
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
