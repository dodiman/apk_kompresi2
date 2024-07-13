from .extensions import *


class Transformasi:
    def __init__(self, data):
        self.data = data

    # def _validasi_tipe(self):
    #     if self.data.dtype == "uint8":
    #         return
            
    #     raise Exception("tipe data yang dikonversi tidak cocok")

    # def is_int(self):
    #     if self.data.dtype == "uint8":
    #         return True
    #     return False

    # def is_hex(self):
    #     s = self.data[0]
    #     try:
    #         value = int(s, 16)
    #         return True
    #     except:
    #         return False
    #     return False

    # def is_bin(self):
    #     if self.data.dtype != "uint8":
    #         s = self.data[0]
    #         if (len(s) == 8) and all(c in '01' for c in s):
    #             return True
        
    #     return False

    def transformasi(self):
        pass


class IntBiner(Transformasi):
    def __init__(self, data):
        super().__init__(data)

    def transformasi(self):
        hasil = np.vectorize(lambda x: format(x, "08b"))(self.data)
        return hasil


class IntHex(Transformasi):
    def __init__(self, data):
        super().__init__(data)

    def transformasi(self):
        hasil = np.vectorize(lambda x: format(x, "X"))(self.data)
        return hasil 


class HexInt(Transformasi):
    def __init__(self, data):
        super().__init__(data)

    def transformasi(self):
        hasil = np.vectorize(lambda x: int(x, 16))(self.data)
        return hasil.astype(np.uint8)

class BinerHex(Transformasi):
    def __init__(self, data):
        super().__init__(data)

    def transformasi(self):
        hasil = np.vectorize(lambda x: format(int(x, 2), "X"))(self.data)
        return hasil

class BinerInt(Transformasi):
    def __init__(self, data):
        super().__init__(data)

    def transformasi(self):
        hasil = np.vectorize(lambda x: int(x, 2))(self.data)
        return hasil.astype(np.uint8)












class BinerTransformasi(Transformasi):
    def __init__(self, data):
        super().__init__(data)

    def transformasi(self):
        self._validasi_tipe()
        hasil = np.vectorize(lambda x: format(x, "08b"))(self.data) # 8 bit
        return hasil 

class IntegerTransformasi(Transformasi):
    def __init__(self, data):
        super().__init__(data)

    def transformasi(self):
        self._validasi_tipe()
        return self.data

class HexTransformasi(Transformasi):
    def __init__(self, data):
        super().__init__(data)

    def transformasi(self):
        self._validasi_tipe()
        
        hasil = np.vectorize(lambda x: format(x, "X"))(self.data)
        return hasil