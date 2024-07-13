from .extensions import time

class Evaluasi:
    def __init__(self):
        self.ukuran_sebelum = None
        self.ukuran_sesudah = None
        self.rc = None
        self.cr = None
        self.ss = None
        self.waktu_eksekusi = None
        self._mulai = 0
        self._selesai = 0

    def to_dict(self):
        context = {
            "rc": self.rc,
            "cr": self.cr,
            "ss": self.ss,
            "waktu_eksekusi": self.waktu_eksekusi,
            "ukuran_sebelum": self.ukuran_sebelum,
            "ukuran_sesudah": self.ukuran_sesudah
        }
        return context

    def _waktu(self):
        hasil = time.time()
        return hasil

    def mulai(self):
        self._mulai = self._waktu()

    def selesai(self):
        self._selesai = self._waktu()
        self.waktu_eksekusi = round(self._selesai - self._mulai, 2)
        

    def set_ukuran_sebelum(self, x):
        self.ukuran_sebelum = x

    def set_ukuran_sesudah(self, x):
        self.ukuran_sesudah = x

    def hitung_rc(self):
        hasil = self.ukuran_sebelum / self.ukuran_sesudah
        # return round(hasil, 2)
        self.rc = round(hasil, 2)

    def hitung_cr(self):
        hasil = self.ukuran_sesudah / self.ukuran_sebelum * 100
        # return round(hasil, 2)
        self.cr = round(hasil, 2)

    def hitung_ss(self):
        hasil = (self.ukuran_sebelum - self.ukuran_sesudah) / self.ukuran_sebelum * 100
        # return round(hasil, 2)
        self.ss = round(hasil, 2)