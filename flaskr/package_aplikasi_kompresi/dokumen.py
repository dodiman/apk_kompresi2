from .extensions import *
from .sumber_data import *
from .transformasi import *
from .path import Path

class Dokumen:
    def __init__(self):
        self.data = None

    def ukuran_bit(self):
        assert self.data is not None, "data dokumen tidak boleh kosong"

        hasil = round(self.data.shape[0]/1024, 2)
        return hasil

    def get_tipe(self):
        return type(self.data)

    def bentuk(self, transformasi, inplace=False):
        metode_transformasi = transformasi(self.data)
        hasil = metode_transformasi.transformasi()
        
        if inplace:
            self.set_data(SumberDataDariNumpy(hasil))
            
        return hasil

    def set_data(self, sumberdata):
        self.data = sumberdata.get_data()

    def simpan_file(self, path):
        assert self.data is not None, "data dokumen tidak boleh kosong"

        path_setting = Path()
        path = os.path.join(path_setting.file_uploads, path)
        
        binary_file = self.bentuk(BinerInt)
        with open(path, "wb") as file:
            file.write(binary_file)
            