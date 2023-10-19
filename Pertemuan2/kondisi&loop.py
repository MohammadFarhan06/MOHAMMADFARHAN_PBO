# Inisialisasi menu makanan
menu_makanan = {
    1: "Nasi Goreng",
    2: "Mie Goreng",
    3: "Ayam Goreng",
    4: "Soto Ayam",
    5: "Nasi Padang",
    6: "Bakso",
    7: "Sate Ayam",
    8: "Pasta",
    9: "Keluar"
}

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("Menu Makanan:")
    for nomor, makanan in menu_makanan.items():
        print(f"{nomor}. {makanan}")

# Looping pemilihan makanan
while True:
    tampilkan_menu()
    
    # Meminta pengguna untuk memilih
    pilihan = input("Masukkan nomor makanan yang Anda inginkan (1-9): ")

    # Periksa apakah pilihan adalah nomor yang valid
    if pilihan.isnumeric():
        pilihan = int(pilihan)
        if 1 <= pilihan <= 9:
            if pilihan == 9:
                print("Terima kasih! Sampai jumpa.")
                break  # Keluar dari loop jika pengguna memilih 'Keluar'
            else:
                makanan_terpilih = menu_makanan[pilihan]
                print(f"Anda telah memilih: {makanan_terpilih}")
        else:
            print("Pilihan tidak valid. Silakan pilih nomor makanan yang benar.")
    else:
        print("Masukkan nomor yang valid (1-9) atau ketik 'Keluar' untuk keluar.")
