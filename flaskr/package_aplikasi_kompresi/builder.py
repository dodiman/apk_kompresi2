from .extensions import *
from .preprocessing import *
from .dokumen import *

class PenyusunanUlangBuilder:
    def group(self, dok, pointer="0"):
        np_array = dok.data.copy()
        dok_kompresi = Dokumen()
        dok_kompresi.set_data(SumberDataDariNumpy(np_array))
        
        current_datetime=datetime.datetime.now()
        datetime_str = current_datetime.strftime("%Y%m%d%H%M%S")
        # datetime_str = datetime_str.replace(" ", "").replace("-", "").replace(":", "")

        # simpan kunci
        path = datetime_str + ".pkl" + pointer
        # kunci.simpan(path)
        
        # add code
        binary_list = [format(ord(char), '08b') for char in path]
        binary_array = np.array(binary_list) # len = 18
        n = len(dok_kompresi.data)
        temp = np.insert(dok_kompresi.data, n, binary_array)

        dok_kompresi.set_data(SumberDataDariNumpy(temp))
        
        return dok_kompresi, path
        # return dok_kompresi

    def ungroup(self, dok):
        np_array = dok.data.copy()
        dok_kompresi = Dokumen()
        dok_kompresi.set_data(SumberDataDariNumpy(np_array))
        
        path_arr = dok_kompresi.data[-19:]       
        # kondisi = path_arr[-1]
        # path_arr = path_arr[:-1]
        
        chars = [chr(int(binary, 2)) for binary in path_arr] # 1D to str
        path = ''.join(chars)

        kondisi = path[-1]
        path = path[:-1]
        
        dok_kompresi.set_data(SumberDataDariNumpy(dok_kompresi.data[:-19]))

        # print(f"kondisi {kondisi}")
        return dok_kompresi, path, kondisi
    
class Builder:
    def __init__(self):
        # self.dokumen = dokumen
        # self.dokumen_kompresi = Dokumen()
        self.potongan_dokumen = []
        self.hasil_dan_kunci = []
        # self.sizes = []
        # self.kumpulan_kunci = []
        

    def dekompresi_banyak(self, metode, dokumen_kompresi):
        temp = dokumen_kompresi
        
        while True:
            menyusun_ulang = PenyusunanUlangBuilder()
            dokumen_kompresi, kuncipath, kondisi = menyusun_ulang.ungroup(temp)
    
            kunci_builder = KunciBuilder()
            kunci_b = kunci_builder.load(kuncipath)
            
            s_j = SplitJoinNumpy()
    
            split_arr = s_j.split(dokumen_kompresi.data,  kunci_b.sizes)
    
            new_arr = []
            for i in range(len(split_arr)):
                dok = Dokumen()
                dok.set_data(SumberDataDariNumpy(split_arr[i]))
                # kumpulan_dok.append(dok)
                
                metode_dekompresi = metode
                dok_dekompresi = metode_dekompresi.dekompresi(dok, kunci_b.kumpulan_kunci[i])
    
                new_arr.extend(dok_dekompresi.data)
    
            new_arr = np.array(new_arr)
            dok_hasil = Dokumen()
            dok_hasil.set_data(SumberDataDariNumpy(new_arr))

            print(f"kondisi: {kondisi}")
            if kondisi == "0":
                break

            temp = dok_hasil
                    
        return dok_hasil
        

    def kompresi_banyak(self, metode, dokumen, pointer="0"):
        kunci_builder = KunciBuilder()
        
        self._potong(dokumen, 16)
        new_array = []
        sizes=[]
        kumpulan_kunci = []
        for value in self.potongan_dokumen:
            metode_kompresi = metode
            hasil, kunci = metode_kompresi.kompresi(value)
            self.hasil_dan_kunci.append((hasil, kunci))
            new_array.extend(hasil.data)
            sizes.append(len(hasil.data))
            kumpulan_kunci.append(kunci)

        # self.sizs = sizes
        kunci_builder.set_sizes(sizes)
        kunci_builder.set_kumpulan_kunci(kumpulan_kunci)
        
        new_array = np.array(new_array)
        dok = Dokumen()
        dok.set_data(SumberDataDariNumpy(new_array))
        # self.dokumen_kompresi.set_data(SumberDataDariNumpy(new_array))

        # penyusunan ulang
        susun_ulang = PenyusunanUlangBuilder()
        dok, path = susun_ulang.group(dok, pointer) # meng-update dok
        # susun_ulang.group(dok, pointer="0") # menghupdate dok

        kunci_path = path[:-1]
        kondisi = path[-1]
        
        # print(f"kunci_path {path}")
        kunci_builder.simpan(kunci_path)   # simpan kunci
        
        if kondisi != "0":
            nama_file_kompresi = kunci_path[:-4] + ".pdf"
            dok.simpan_file(nama_file_kompresi)
        
        return dok, kunci_builder, kunci_path

    def _potong(self, dokumen, panjang_max=16):
        panjang_max -= 1
        n = dokumen.data.shape[0] // (panjang_max)
        new_arr = np.array_split(dokumen.data, n)

        for value in new_arr:
            dok = Dokumen()
            dok.set_data(SumberDataDariNumpy(value))
            self.potongan_dokumen.append(dok)
        
        return self
    
class KunciBuilder:
    def __init__(self):
        self.sizes = []
        self.kumpulan_kunci = []

    def set_sizes(self, x):
        self.sizes = x

    def set_kumpulan_kunci(self, x):
        self.kumpulan_kunci = x

    def to_dict(self):
        hasil = {
            "sizes": self.sizes,
            "kumpulan_kunci": self.kumpulan_kunci
        }
        return hasil

    def simpan(self, path):

        path_setting = Path()
        path = os.path.join(path_setting.file_uploads, path)
        
        hasil = self.to_dict()
        with open(path, 'wb') as fp:
            pickle.dump(hasil, fp)
            # print("berhasil disimpan kuncinya")

    def load(self, path):

        path_setting = Path()
        path = os.path.join(path_setting.file_uploads, path)
        
        with open(path, 'rb') as fp:
            data_dict = pickle.load(fp)

        kunci_builder = KunciBuilder()
        kunci_builder.set_sizes(data_dict["sizes"])
        kunci_builder.set_kumpulan_kunci(data_dict["kumpulan_kunci"])
            
        return kunci_builder

