from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W, ttk, LabelFrame
import math 

class AplikasiLuasBangun:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Aplikasi Menghitung Luas dan Keliling Bangun Datar")
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.tabControl = None
        self.aturKomponen()
        self.parent.geometry("800x500")
        self.running_text_label = Label(parent, text='Selamat datang di Aplikasi Menghitung Luas dan Keliling Bangun Datar', font=("Brush Script", 15), bg="lime green")
        self.running_text_label.pack(fill="x", expand=YES, padx=10, pady=10)
       

    def update_running_text(self):
        running_text = "Selamat datang di Aplikasi Menghitung Luas dan Keliling Bangun Datar"
        self.parent.after(3000, self.update_running_text)


    def aturKomponen(self):
        self.tabControl = ttk.Notebook(self.parent)
        background_frame = LabelFrame(self.parent, text="Aplikasi Menghitung Luas dan Keliling Bangun Datar", labelanchor='n', padx=10, pady=10)
        background_frame.pack(fill=BOTH, expand=YES)
        self.update_running_text()
        
        self.tabLingkaran = ttk.Frame(self.tabControl)
        self.tabSegitiga = ttk.Frame(self.tabControl)
        self.tabTrapesium = ttk.Frame(self.tabControl)
        self.tabPersegiPanjang = ttk.Frame(self.tabControl)
        self.tabJajargenjang = ttk.Frame(self.tabControl)
        self.tabLayanglayang = ttk.Frame(self.tabControl)
        self.tabBelahKetupat = ttk.Frame(self.tabControl)
        self.tabPersegi = ttk.Frame(self.tabControl)
        
        
        self.tabControl.add(self.tabLingkaran, text="Lingkaran")
        self.tabControl.add(self.tabSegitiga, text="Segitiga")
        self.tabControl.add(self.tabTrapesium, text="Trapesium")
        self.tabControl.add(self.tabPersegiPanjang, text="PersegiPanjang")
        self.tabControl.add(self.tabJajargenjang, text="Jajargenjang")
        self.tabControl.add(self.tabLayanglayang, text="layanglayang")
        self.tabControl.add(self.tabBelahKetupat, text="Belah Ketupat")
        self.tabControl.add(self.tabPersegi, text="Persegi")
       
    



        self.tabControl.pack(fill="both", expand=True)

        self.aturKomponenLingkaran()
        self.aturKomponenSegitiga()
        self.aturKomponenTrapesium()
        self.aturKomponenPersegiPanjang()
        self.aturKomponenJajargenjang()
        self.aturKomponenLayanglayang()
        self.aturKomponenBelahKetupat()
        self.aturKomponenPersegi()
        
   
    def aturKomponenLingkaran(self):
        mainFrame = Frame(self.tabLingkaran, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        Label(mainFrame, text='Jari-Jari:', anchor='e').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Luas:', anchor='e').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Keliling:', anchor='e').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)

        self.txtJariJariLingkaran = Entry(mainFrame, justify='center')
        self.txtJariJariLingkaran.grid(row=0, column=1, padx=5, pady=5)
        self.txtLuasLingkaran = Entry(mainFrame, justify='center')
        self.txtLuasLingkaran.grid(row=1, column=1, padx=5, pady=5)
        self.txtKelilingLingkaran = Entry(mainFrame, justify='center')
        self.txtKelilingLingkaran.grid(row=2, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitungLingkaran)
        self.btnHitung.grid(row=3, column=1, padx=5, pady=5)

    def aturKomponenSegitiga(self):
        mainFrame = Frame(self.tabSegitiga, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        Label(mainFrame, text='Alas:', anchor='e').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi:", anchor='e').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:", anchor='e').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Sisi A:', anchor='e').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Sisi B:', anchor='e').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Sisi C:', anchor='e').grid(row=6, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Keliling:', anchor='e').grid(row=7, column=0,
            sticky=W, padx=5, pady=5)

        self.txtAlasSegitiga = Entry(mainFrame, justify='center')
        self.txtAlasSegitiga.grid(row=0, column=1, padx=5, pady=5)
        self.txtTinggiSegitiga = Entry(mainFrame, justify='center')
        self.txtTinggiSegitiga.grid(row=1, column=1, padx=5, pady=5)
        self.txtLuasSegitiga = Entry(mainFrame, justify='center')
        self.txtLuasSegitiga.grid(row=3, column=1, padx=5, pady=5)
        self.txtSisiASegitiga = Entry(mainFrame, justify='center')
        self.txtSisiASegitiga.grid(row=4, column=1, padx=5, pady=5)
        self.txtSisiBSegitiga = Entry(mainFrame, justify='center')
        self.txtSisiBSegitiga.grid(row=5, column=1, padx=5, pady=5)
        self.txtSisiCSegitiga = Entry(mainFrame, justify='center')
        self.txtSisiCSegitiga.grid(row=6, column=1, padx=5, pady=5)
        self.txtKelilingSegitiga = Entry(mainFrame, justify='center')
        self.txtKelilingSegitiga.grid(row=7, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitungSegitiga)
        self.btnHitung.grid(row=8, column=1, padx=5, pady=5)



    def aturKomponenTrapesium(self):
        mainFrame = Frame(self.tabTrapesium, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        Label(mainFrame, text='Panjang Sisi Atas:', anchor='e').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Panjang Sisi Bawah:", anchor='e').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi:", anchor='e').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:", anchor='e').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Sisi Kanan Atas:', anchor='e').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Sisi Kanan Bawah:', anchor='e').grid(row=6, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Keliling:', anchor='e').grid(row=7, column=0,
            sticky=W, padx=5, pady=5)

        self.txtSisiAtas = Entry(mainFrame, justify='center')
        self.txtSisiAtas.grid(row=0, column=1, padx=5, pady=5)
        self.txtSisiBawah = Entry(mainFrame, justify='center')
        self.txtSisiBawah.grid(row=1, column=1, padx=5, pady=5)
        self.txtTinggi = Entry(mainFrame, justify='center')
        self.txtTinggi.grid(row=2, column=1, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame, justify='center')
        self.txtLuas.grid(row=4, column=1, padx=5, pady=5)
        self.txtSisiKananAtas = Entry(mainFrame, justify='center')
        self.txtSisiKananAtas.grid(row=5, column=1, padx=5, pady=5)
        self.txtSisiKananBawah = Entry(mainFrame, justify='center')
        self.txtSisiKananBawah.grid(row=6, column=1, padx=5, pady=5)
        self.txtKeliling = Entry(mainFrame, justify='center')
        self.txtKeliling.grid(row=7, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitungTrapesium)
        self.btnHitung.grid(row=8, column=1, padx=5, pady=5)

    def aturKomponenPersegiPanjang(self):
        mainFrame = Frame(self.tabPersegiPanjang, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        Label(mainFrame, text='Panjang:', anchor='e').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Lebar:', anchor='e').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Luas:', anchor='e').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Keliling:', anchor='e').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)

        self.txtPanjang = Entry(mainFrame, justify='center')
        self.txtPanjang.grid(row=0, column=1, padx=5, pady=5)
        self.txtLebar = Entry(mainFrame, justify='center')
        self.txtLebar.grid(row=1, column=1, padx=5, pady=5)
        self.txtLuasPersegiPanjang = Entry(mainFrame, justify='center')
        self.txtLuasPersegiPanjang.grid(row=3, column=1, padx=5, pady=5)
        self.txtKelilingPersegiPanjang = Entry(mainFrame, justify='center')
        self.txtKelilingPersegiPanjang.grid(row=4, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitungPersegiPanjang)
        self.btnHitung.grid(row=5, column=1, padx=5, pady=5)

    def aturKomponenJajargenjang(self):
        mainFrame = Frame(self.tabJajargenjang, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        Label(mainFrame, text='Alas:', anchor='e').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi:", anchor='e').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:", anchor='e').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Sisi A:', anchor='e').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Sisi B:', anchor='e').grid(row=5, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Keliling:', anchor='e').grid(row=6, column=0, sticky=W, padx=5, pady=5)

        self.txtAlasJajargenjang = Entry(mainFrame, justify='center')
        self.txtAlasJajargenjang.grid(row=0, column=1, padx=5, pady=5)
        self.txtTinggiJajargenjang = Entry(mainFrame, justify='center')
        self.txtTinggiJajargenjang.grid(row=1, column=1, padx=5, pady=5)
        self.txtLuasJajargenjang = Entry(mainFrame, justify='center')
        self.txtLuasJajargenjang.grid(row=3, column=1, padx=5, pady=5)
        self.txtSisiAJajargenjang = Entry(mainFrame, justify='center')
        self.txtSisiAJajargenjang.grid(row=4, column=1, padx=5, pady=5)
        self.txtSisiBJajargenjang = Entry(mainFrame, justify='center')
        self.txtSisiBJajargenjang.grid(row=5, column=1, padx=5, pady=5)
        self.txtKelilingJajargenjang = Entry(mainFrame, justify='center')
        self.txtKelilingJajargenjang.grid(row=6, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitungJajargenjang)
        self.btnHitung.grid(row=7, column=1, padx=5, pady=5)

    def aturKomponenLayanglayang(self):
        mainFrame = Frame(self.tabLayanglayang, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        Label(mainFrame, text='Diagonal 1:', anchor='e').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Diagonal 2:', anchor='e').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:", anchor='e').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Keliling:', anchor='e').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)

        self.txtDiagonal1Layanglayang = Entry(mainFrame, justify='center')
        self.txtDiagonal1Layanglayang.grid(row=0, column=1, padx=5, pady=5)
        self.txtDiagonal2Layanglayang = Entry(mainFrame, justify='center')
        self.txtDiagonal2Layanglayang.grid(row=1, column=1, padx=5, pady=5)
        self.txtLuasLayanglayang = Entry(mainFrame, justify='center')
        self.txtLuasLayanglayang.grid(row=3, column=1, padx=5, pady=5)
        self.txtKelilingLayanglayang = Entry(mainFrame, justify='center')
        self.txtKelilingLayanglayang.grid(row=4, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitungLayanglayang)
        self.btnHitung.grid(row=5, column=1, padx=5, pady=5)

    def aturKomponenBelahKetupat(self):
        mainFrame = Frame(self.tabBelahKetupat, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        Label(mainFrame, text='Diagonal 1:', anchor='e').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Diagonal 2:', anchor='e').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:", anchor='e').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Keliling:', anchor='e').grid(row=4, column=0, sticky=W, padx=5, pady=5)

        self.txtDiagonal1BelahKetupat = Entry(mainFrame, justify='center')
        self.txtDiagonal1BelahKetupat.grid(row=0, column=1, padx=5, pady=5)
        self.txtDiagonal2BelahKetupat = Entry(mainFrame, justify='center')
        self.txtDiagonal2BelahKetupat.grid(row=1, column=1, padx=5, pady=5)
        self.txtLuasBelahKetupat = Entry(mainFrame, justify='center')
        self.txtLuasBelahKetupat.grid(row=3, column=1, padx=5, pady=5)
        self.txtKelilingBelahKetupat = Entry(mainFrame, justify='center')
        self.txtKelilingBelahKetupat.grid(row=4, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitungBelahKetupat)
        self.btnHitung.grid(row=5, column=1, padx=5, pady=5)

    def aturKomponenPersegi(self):
        mainFrame = Frame(self.tabPersegi, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        Label(mainFrame, text='Sisi:', anchor='e').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Luas:', anchor='e').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Keliling:', anchor='e').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)

        self.txtSisiPersegi = Entry(mainFrame, justify='center')
        self.txtSisiPersegi.grid(row=0, column=1, padx=5, pady=5)
        self.txtLuasPersegi = Entry(mainFrame, justify='center')
        self.txtLuasPersegi.grid(row=1, column=1, padx=5, pady=5)
        self.txtKelilingPersegi = Entry(mainFrame, justify='center')
        self.txtKelilingPersegi.grid(row=2, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitungPersegi)
        self.btnHitung.grid(row=3, column=1, padx=5, pady=5)




    def onHitungLingkaran(self):
        jari_jari = float(self.txtJariJariLingkaran.get())
        luasLingkaran = math.pi * jari_jari ** 2
        kelilingLingkaran = 2 * math.pi * jari_jari
        self.txtLuasLingkaran.delete(0, END)
        self.txtLuasLingkaran.insert(END, str(luasLingkaran))
        self.txtKelilingLingkaran.delete(0, END)
        self.txtKelilingLingkaran.insert(END, str(kelilingLingkaran))
        
    

    def onHitungSegitiga(self):
        alas = float(self.txtAlasSegitiga.get())
        tinggi = float(self.txtTinggiSegitiga.get())
        sisi_a = float(self.txtSisiASegitiga.get())
        sisi_b = float(self.txtSisiBSegitiga.get())
        sisi_c = float(self.txtSisiCSegitiga.get())
        luasSegitiga = 0.5 * alas * tinggi
        kelilingSegitiga = sisi_a + sisi_b + sisi_c
        self.txtLuasSegitiga.delete(0, END)
        self.txtLuasSegitiga.insert(END, str(luasSegitiga))
        self.txtKelilingSegitiga.delete(0, END)
        self.txtKelilingSegitiga.insert(END, str(kelilingSegitiga))

    def onHitungTrapesium(self):
        sisi_atas = float(self.txtSisiAtas.get())
        sisi_bawah = float(self.txtSisiBawah.get())
        tinggi = float(self.txtTinggi.get())
        sisi_kanan_atas = float(self.txtSisiKananAtas.get())
        sisi_kanan_bawah = float(self.txtSisiKananBawah.get())
        luas = 0.5 * (sisi_atas + sisi_bawah) * tinggi
        keliling = sisi_atas + sisi_bawah + sisi_kanan_atas + sisi_kanan_bawah
        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, str(luas))
        self.txtKeliling.delete(0, END)
        self.txtKeliling.insert(END, str(keliling))

    def onHitungPersegiPanjang(self):
        panjang = float(self.txtPanjang.get())
        lebar = float(self.txtLebar.get())
        luas = panjang * lebar
        keliling = 2 * (panjang + lebar)
        self.txtLuasPersegiPanjang.delete(0, END)
        self.txtLuasPersegiPanjang.insert(END, str(luas))
        self.txtKelilingPersegiPanjang.delete(0, END)
        self.txtKelilingPersegiPanjang.insert(END, str(keliling))

    def onHitungJajargenjang(self):
        alas = float(self.txtAlasJajargenjang.get())
        tinggi = float(self.txtTinggiJajargenjang.get())
        sisi_a = float(self.txtSisiAJajargenjang.get())
        sisi_b = float(self.txtSisiBJajargenjang.get())
        luas = alas * tinggi
        keliling = 2 * (sisi_a + sisi_b)
        self.txtLuasJajargenjang.delete(0, END)
        self.txtLuasJajargenjang.insert(END, str(luas))
        self.txtKelilingJajargenjang.delete(0, END)
        self.txtKelilingJajargenjang.insert(END, str(keliling))

    def onHitungLayanglayang(self):
        diagonal1 = float(self.txtDiagonal1Layanglayang.get())
        diagonal2 = float(self.txtDiagonal2Layanglayang.get())
        luas = 0.5 * diagonal1 * diagonal2
        keliling = 2 * (math.sqrt((0.25 * diagonal1 ** 2) + (0.25 * diagonal2 ** 2)))
        self.txtLuasLayanglayang.delete(0, END)
        self.txtLuasLayanglayang.insert(END, str(luas))
        self.txtKelilingLayanglayang.delete(0, END)
        self.txtKelilingLayanglayang.insert(END, str(keliling))

    def onHitungBelahKetupat(self):
        diagonal1 = float(self.txtDiagonal1BelahKetupat.get())
        diagonal2 = float(self.txtDiagonal2BelahKetupat.get())
        luas = 0.5 * diagonal1 * diagonal2
        keliling = 4 * math.sqrt((0.25 * diagonal1 ** 2) + (0.25 * diagonal2 ** 2))
        self.txtLuasBelahKetupat.delete(0, END)
        self.txtLuasBelahKetupat.insert(END, str(luas))
        self.txtKelilingBelahKetupat.delete(0, END)
        self.txtKelilingBelahKetupat.insert(END, str(keliling))

    def onHitungPersegi(self):
        sisi = float(self.txtSisiPersegi.get())
        luas = sisi ** 2
        keliling = 4 * sisi
        self.txtLuasPersegi.delete(0, END)
        self.txtLuasPersegi.insert(END, str(luas))
        self.txtKelilingPersegi.delete(0, END)
        self.txtKelilingPersegi.insert(END, str(keliling))

 



    def onKeluar(self):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    from tkinter import ttk
    aplikasi = AplikasiLuasBangun(root)




    root.configure(bg="pink")

    root.mainloop()
