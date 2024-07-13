from .extensions import *

# default_directory = "D:\\projects\\jupyter"
# os.chdir(default_directory)
dirs = os.getcwd()

class SumberData:
    def __init__(self, data):
        self.data = data

    def get_data(self):
        pass

class SumberDataDariDiskLokal(SumberData):
    def __init__(self, data):  # data berupa path (str) lokasi file
        super().__init__(data)

    def get_data(self):
        path = os.path.join(dirs, self.data)
        with open(path, "rb") as file:
            hasil = np.frombuffer(file.read(), dtype=np.uint8)
        return hasil
    
class SumberDataDariNumpy(SumberData):
    def __init__(self, data):
        super().__init__(data)

    def get_data(self):
        if self.data.ndim != 1:
            raise Exception("harus numpy 1D")
        return self.data