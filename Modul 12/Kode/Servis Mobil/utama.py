from tkinter import *

root=Tk()
root.title("Servis Mobil")
root.geometry("500x500")

def mobil():
    import mobil 

def jenisLayanan():
    import jenisLayanan

def transaksi():
    import transaksi

l1=Label(root, text="Servis Mobil", font=(None,24,"bold"))
l1.pack(pady=20)

b1=Button(root, text="Mobil", command=mobil, width=50)
b1.pack(pady=10)

b2=Button(root, text="Jenis Layanan", command=jenisLayanan, width=50)
b2.pack(pady=10)

b3=Button(root, text="Transaksi", command=transaksi, width=50)
b3.pack(pady=10)

l1=Label(root, text="Hadid Aldio Indratama\nL200160055\nA")
l1.pack(pady=40)

root.mainloop()
