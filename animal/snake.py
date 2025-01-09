from latihan_12animal import *

class Ular(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, bisa):
        super().__init__(nama, makanan, hidup, berkembang_biak) 
        self.warna = warna
        self.bisa = bisa

    def info_ular(self):
        print(f"Nama                 : {self.nama}")
        print(f"Makanan              : {self.makanan}")
        print(f"Hidup                : {self.hidup}")
        print(f"Berkembang biak      : {self.berkembang_biak}")
        print(f"Warna                : {self.warna}")
        print(f"Jenis bisa          : {self.bisa}")
        print() 

ular1 = Ular("Ular Kobra", "Mamalia kecil", "10 tahun", "bertelur", "hitam", "berbisa")
ular1.info_ular()

ular2 = Ular("Ular Sanca", "Burung", "20 tahun", "bertelur", "coklat", "tidak berbisa")
ular2.info_ular()

ular2 = Ular("Ular python", "ular", " 15 ahun", "bertelur", "belang", "tidak berbisa")
ular2.info_ular()