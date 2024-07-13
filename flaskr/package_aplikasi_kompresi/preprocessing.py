from .extensions import *


class Preprocessing:
    pass

class SplitJoinNumpy(Preprocessing):
    def split(self, arr_1d, sizes=[]):
        # sizes = [2, 3, 1, 3]
        
        # Compute the cumulative sum of sizes to get the split indices
        indices = np.cumsum(sizes)[:-1] # Exclude the last element to use as split points

        new_arr = np.array_split(arr_1d, indices)
        
        return new_arr

    def join(self, potongan):
        new_arr = []
        size = []
        for value in potongan:
            new_arr.extend(value)
            size.append(len(value))

        new_arr = np.array(new_arr)
        
        return new_arr, size


class PaddingFlag(Preprocessing):
    # padding dan flagging
    def encode(self, string_biner, jumlah_bit=8):   # update self._string_biner
        # string_biner = self.kompresi1
        n = len(string_biner)
        sisa_bagi = n % jumlah_bit
        
        # assert n >= 8, "panjang string binernya kurang dari 8"
    
        if sisa_bagi == 0:
            # self._string_biner = string_biner
            hasil = string_biner
        else:
            padding = "0" * (7-sisa_bagi) + "1"   # rumus: 7 - sisa_bagi + "1"
            flag = 9 - sisa_bagi                  # rumus: 9 - sisa_bagi
            flag = format(flag, '08b')
    
            # self._string_biner = string_biner + padding + flag
            
            hasil = string_biner + padding + flag

        return hasil
    
    # padding dan flagging decode
    def decode(self, string_biner, n_awal):
        hasil = string_biner[0:n_awal]
        return hasil

class GabungPisahString(Preprocessing):
    def gabung(self, s) -> dict:
        hasil = {}
        indeks = np.vectorize(lambda x: len(x))(s)
        string_biner = "".join(map(str, s))  # menggabung string biner
        
        hasil["indeks"] = indeks
        hasil["string_biner"] = string_biner
        return hasil

    def pisah(self, dict_kompresi):
        indeks = dict_kompresi["indeks"]
        s = dict_kompresi["string_biner"]
        n = len(indeks)
        s_baru = np.empty(n, dtype=object)
        
        awal = 0
        akhir = 0
        for i in range(0, n):
            if i>0:
                awal = akhir
        
            if i < n-1:
                akhir += indeks[i]
                # print(indeks[i] + indeks[i+1])
            else:
                akhir = sum(indeks)
            
            # print(f"{awal} {akhir}")
            s_baru[i] = s[awal:akhir]
        
        # return pd.Series(s_baru)
        return s_baru

class StringToBiner(Preprocessing):
    def konversi(self, string="", n=8, pemisah="-") -> str:
        # string = self._string_biner
        assert len(string) >= 8, "string terlalu sedikit"
        result = ''
        no = 0
        for i, char in enumerate(string, 1):
            if char=="0" or char=="1":
                no += 1
                
            result += char
            if (no % n == 0) and (result[-2] != pemisah) and (len(string) != i):
                result += pemisah

        # update _strng_biner
        # self._string_biner = result

        def str_list(my_str, pemisah=","):
            my_list = list(my_str.split(pemisah))
            return my_list
            
        result = np.array(str_list(result, pemisah="-"))
        
        return result

    def konversi_balik(self, biner):           
        hasil = biner.tolist()
        hasil = "".join(map(str, hasil))
        
        return hasil

    def set_string_biner(self, list_int):
        
        my_list = list_int.tolist()
        self._string_biner = self.konversi.list_str(my_list, pemisah="")
        return self