from latihan_12animal import *
class Ikan(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, habitat):
        super().__init__(nama, makanan, hidup, berkembang_biak) 
        self.warna = warna
        self.habitat = habitat

    def info_fish(self):
        print(f"Nama                 : {self.nama}")
        print(f"Makanan              : {self.makanan}")
        print(f"Hidup                : {self.hidup}")
        print(f"Berkembang biak      : {self.berkembang_biak}")
        print(f"Warna                : {self.warna}")
        print(f"Habitat              : {self.habitat}")
        print() 
ikan1 = Ikan("Ikan Mas", "pelet", "3 tahun", "bertelur", "emas", "air tawar")
ikan2 = Ikan("Ikan Koi", "Pelet", "2 tahun", "bertelur", "merah-putih", "air tawar")
ikan3 = Ikan("Ikan Tuna", "Ikan kecil", "5 tahun", "bertelur", "biru-perak", "air laut")

ikan1.info_fish()
ikan2.info_fish()
ikan3.info_fish()