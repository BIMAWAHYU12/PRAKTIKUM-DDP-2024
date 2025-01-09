from latihan_12animal import *

class burung(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, paruh):
        super().__init__(nama, makanan, hidup, berkembang_biak) 
        self.warna = warna
        self.paruh = paruh

    def info_burung(self):
        print(f"Nama                 : {self.nama}")
        print(f"Makanan              : {self.makanan}")
        print(f"Hidup                : {self.hidup}")
        print(f"Berkembang biak      : {self.berkembang_biak}")
        print(f"Warna                : {self.warna}")
        print(f"Paruh                : {self.paruh}")
        print() 
burung1 = burung("Burung Merpati", "Biji-bijian", "5 tahun", "bertelur", "putih", "berparuh pendek")
burung2 = burung("Burung Kenari", "Buah-buahan", "4 tahun", "bertelur", "kuning", "berparuh sedang")
burung3 = burung("Burung Cendrawasih", "Nektar", "6 tahun", "bertelur", "merah-kuning", "berparuh panjang")

burung1.info_burung()
burung2.info_burung()
burung3.info_burung()