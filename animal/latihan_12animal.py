class animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def informasi(self):
        print(f"{'nama hewan':<20}: {self.nama}")
        print(f"{'makanan':<20}: {self.makanan}")
        print(f"{'hidup':<20}: {self.hidup}")
        print(f"{'berkembang biak':<20}: {self.berkembang_biak}")