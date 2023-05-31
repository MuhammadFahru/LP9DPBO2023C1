from mansion import Mansion
from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from PIL import Image, ImageTk

hunians = []
hunians.append(Mansion("Fahru", "Jl. Merdeka No. 1", "mansion.jpg", 3, 3, 1000, 2, 2))
hunians.append(Apartemen("Nelly Joy", "Jl. Merdeka No. 2", "apartement.jpeg", 3, 3, "Apartemen XYZ", 100))
hunians.append(Rumah("Sekar MK", "Jl. Merdeka No. 3", "rumah_1.jpg", 5, 2, 300))
hunians.append(Indekos("Jl. Merdeka No. 4", "indekos.jpg", "Bp. Romi", "Cahya"))
hunians.append(Rumah("Satria", "Jl. Merdeka No. 5", "rumah_2.jpg", 1, 4, 200))

root = Tk()
root.title("Praktikum DPBO Python")
root.geometry("600x600")

photos = []

# Funtion to show resident data
def daftar_residen():
    
    # Menutup screen landing page
    root.withdraw()
    
    daftar_screen = Toplevel(root)
    daftar_screen.title("Residen")
    
    frame = LabelFrame(daftar_screen, text="Data Seluruh Residen", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    opts = LabelFrame(daftar_screen, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    b_add = Button(opts, text="Add Data", state="disabled")
    b_add.grid(row=0, column=0)

    b_exit = Button(opts, text="Exit", command=daftar_screen.quit)
    b_exit.grid(row=0, column=1)

    for index, h in enumerate(hunians):
        idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index, column=1)

        if h.get_jenis() != "Indekos": 
            name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)
        else:
            name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)

        b_detail = Button(frame, text="Details ", command=lambda index=index: detail_residen(index))
        b_detail.grid(row=index, column=3)

# Function to show resident detail
def detail_residen(index):
    detail_screen = Toplevel()
    detail_screen.title("Detail " + hunians[index].get_jenis())

    d_frame = LabelFrame(detail_screen, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    d_summary = Label(d_frame, text="Summary\n" + hunians[index].get_detail() + hunians[index].get_summary() + "\n" + hunians[index].get_dokumen(), anchor="w", justify=LEFT).grid(row=0, column=0, sticky="w")
    
    image = Image.open("assets/" + hunians[index].get_foto_bangunan())
    image = image.resize((250, 250))
    photo = ImageTk.PhotoImage(image)
    photos.append(photo)
    img_label = Label(d_frame, image=photo)
    img_label.grid(row=1, column=0)

    btn = LabelFrame(detail_screen, padx=0, pady=0)
    btn.pack(padx=10, pady=10)
    b_close = Button(btn, text="Close", command=detail_screen.destroy)
    b_close.grid(row=0, column=0)

# Memuat gambar
image = Image.open("assets/bg_landing.jpg")
image = image.resize((400, 400), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
photos.append(photo)

# Membuat label untuk menampilkan gambar
image_label = Label(root, image=photo)
image_label.pack()

# Membuat label untuk judul
title_label = Label(root, text="Landing Page", font=("Helvetica", 20))
title_label.pack(pady=10)

# Membuat tombol
button = Button(root, text="Daftar Residen", command=daftar_residen)
button.pack()

root.mainloop()
