import tkinter as tk

def hitung():
    pilihan = pilihan_var.get()
    angka1 = float(angka1_entry.get())
    angka2 = float(angka2_entry.get())
    
    if pilihan == 'Penjumlahan':
        hasil = angka1 + angka2
    elif pilihan == 'Pengurangan':
        hasil = angka1 - angka2
    elif pilihan == 'Perkalian':
        hasil = angka1 * angka2
    elif pilihan == 'Pembagian':
        if angka2 != 0:
            hasil = angka1 / angka2
        else:
            hasil_label.config(text="Error: Tidak dapat melakukan pembagian oleh nol!")
            return
    else:
        hasil_label.config(text="Pilihan tidak valid")
        return

    hasil_label.config(text=f"Hasil {pilihan}: {hasil}")

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Sederhana")

# Label sambutan
sambutan_label = tk.Label(root, text="Selamat datang di program menghitung sederhana")
sambutan_label.pack()

# Pilihan menu
pilihan_var = tk.StringVar()
pilihan_var.set("Penjumlahan")
pilihan_label = tk.Label(root, text="Pilih operasi:")
pilihan_label.pack()

pilihan_menu = tk.OptionMenu(root, pilihan_var, "Penjumlahan", "Pengurangan", "Perkalian", "Pembagian")
pilihan_menu.pack()

# Input angka
angka1_label = tk.Label(root, text="Masukkan angka pertama:")
angka1_label.pack()

angka1_entry = tk.Entry(root)
angka1_entry.pack()

angka2_label = tk.Label(root, text="Masukkan angka kedua:")
angka2_label.pack()

angka2_entry = tk.Entry(root)
angka2_entry.pack()

# Tombol Hitung
hitung_button = tk.Button(root, text="Hitung", command=hitung)
hitung_button.pack()

# Hasil
hasil_label = tk.Label(root, text="")
hasil_label.pack()

# Menjalankan jendela Tkinter
root.mainloop()
