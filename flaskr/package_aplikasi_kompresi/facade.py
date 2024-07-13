from .algoritma_kompresi import MetodeFibonacci, MetodeLevenstein, Metode
from .builder import Builder

class Facade:
    pass

class FacadeKompresi(Facade):
    def __init__(self):
        pass
        
    def kompresi(self, metodes, dokumen):
    
        dict_metodes = {
            "fib": MetodeFibonacci(),
            "lev": MetodeLevenstein()
        }
    
        
        n = len(metodes)
        
        temp = dokumen
        for i in range(0, n, 1):
            pointer = str(i)
                
            builder1 = Builder()
            dok_kompresi1, _, _ = builder1.kompresi_banyak(dict_metodes[metodes[i]], temp, pointer)
        
            temp = dok_kompresi1
    
        return dok_kompresi1