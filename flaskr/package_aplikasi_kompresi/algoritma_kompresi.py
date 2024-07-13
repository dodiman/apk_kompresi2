from .extensions import *
from .preprocessing import *
from .dokumen import *
from .kunci import *

class Metode:
    def __init__(self):
        # self.dokumen = dokumen # class Dokumen
        pass

    def dekompresi(self, dokumen, kunci):
        string_to_biner = StringToBiner()
        string_biner = string_to_biner.konversi_balik(dokumen.data)

        padding_flag = PaddingFlag()
        n_awal = sum(kunci.key1) # [2, 3, ...]
        string_biner = padding_flag.decode(string_biner, n_awal)

        gabung_pisah_string = GabungPisahString()
        my_dict = {
            "indeks": kunci.key1,
            "string_biner": string_biner
        }
        pisah_string_biner = gabung_pisah_string.pisah(my_dict)

        # Reverse the dictionary
        decode = {value: key for key, value in kunci.key2.items()}
        decode_dok = np.vectorize(lambda x: decode[x])(pisah_string_biner)

        hasil = Dokumen()
        hasil.set_data(SumberDataDariNumpy(decode_dok))
       
        return hasil

    def kompresi(self, dokumen):
        kunci = Kunci()
        encode = self.get_code_dict(dokumen)
        kunci.set_key2(encode)
        encode_dok = np.vectorize(lambda x: encode[x])(dokumen.data)

        gabung_pisah_string = GabungPisahString()
        gabung_string_biner = gabung_pisah_string.gabung(encode_dok)
        
        kunci.set_key1(gabung_string_biner["indeks"])
        
        padding_flag = PaddingFlag()
        string_biner = padding_flag.encode(gabung_string_biner["string_biner"])
        # string_biner = self.padding_flag(gabung_string_biner["string_biner"])

        string_to_biner = StringToBiner()
        hasil = string_to_biner.konversi(string_biner)
        # hasil = self.menyusun_ulang_8bit(string_biner)

        dok = Dokumen()
        dok.set_data(SumberDataDariNumpy(hasil))
        
        return dok, kunci

    def _urutkan(self, dokumen):
        hasil = pd.Series(dokumen.data).value_counts()
        return hasil

    def get_kode(self, dokumen):
        urutkan_kemunculan = self._urutkan(dokumen).index.to_numpy()
        hasil = np.array([self._pembentukan_kode(x) for x in range(1, len(urutkan_kemunculan)+1)])
        return urutkan_kemunculan, hasil

    def get_code_dict(self, dokumen):
        keys, values = self.get_kode(dokumen)

        if len(keys) != len(values):
            raise ValueError("panjang data key dan value tidak sama")

        # Create the dictionary
        # dict_from_arrays = {key: value for key, value in zip(keys, values)}

        
        hasil = dict(zip(keys, values))
        
        return hasil

    def _pembentukan_kode(self, bilangan):
        pass


class MetodeFibonacci(Metode):
    # def __init__(self, dokumen):
    #     super().__init__(dokumen)

    def _deret_fibonaci(self, limit):
        deret_fibonaci = [1, 2]
        while (deret_fibonaci[-1] + deret_fibonaci[-2]) <= limit:
            temp = deret_fibonaci[-1] + deret_fibonaci[-2] # nilai akhir + nilai ke dua akhir
            deret_fibonaci.append(temp)
    
        return deret_fibonaci

    # pembentukan codeword fibonacci (menggunakan teori zeckendorf)
    def _pembentukan_kode(self, bilangan):
        deret_fibonaci = self._deret_fibonaci(bilangan)
        codeword = []
        string_biner = ""
        
        if bilangan <= 1:
            return "11"
    
        for bilangan_fibonaci in reversed(deret_fibonaci):
            if bilangan_fibonaci <= bilangan:
                codeword.append(bilangan_fibonaci)
                bilangan = bilangan - bilangan_fibonaci
                string_biner += "1"
            else:
                string_biner += "0"
    
        string_biner = string_biner[::-1]  # reversed
        string_biner += "1"   # menambahkan angka 1 diakhir
        
        return string_biner

class MetodeLevenstein(Metode):
    # def __init__(self, data):
    #     super().__init__(data)

    def _pembentukan_kode(self, bilangan):
        if bilangan==0:
            return "0"
        else:
            return bilangan and '1%s'%self._pembentukan_kode(len(bin(bilangan))-3)+bin(bilangan)[3:]

    # def kompresi(self):
    #     pass

    

class MetodeContoh(Metode):
    def __init__(self, data):
        super().__init__(data)

    def kompresi(self):
        return np.where(self.data == 2, 0, self.data)

    def dekompresi(self, key):
        return np.where(self.data == 0, 2, self.data)

    

        

class MetodeContoh(Metode):
    def __init__(self, data):
        super().__init__(data)

    def kompresi(self):
        return np.where(self.data == 2, 0, self.data)

    def dekompresi(self, key):
        return np.where(self.data == 0, 2, self.data)

    