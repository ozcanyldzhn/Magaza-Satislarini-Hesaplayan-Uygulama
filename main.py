class Magaza:
    def __init__(self, magaza_adi, satici_adi, satici_cinsi):
        self.__magaza_adi = magaza_adi
        self.__satislar = {}
        self.ekle_satis(satici_adi, satici_cinsi, 0)

    def get_magaza_adi(self):
        return self.__magaza_adi

    def set_magaza_adi(self, magaza_adi):
        self.__magaza_adi = magaza_adi
        
    def ekle_satis(self, satici_adi, satici_cinsi, tutar):
        if satici_adi not in self.__satislar:
            self.__satislar[satici_adi] = {satici_cinsi: tutar}
        else:
            if satici_cinsi in self.__satislar[satici_adi]:
                self.__satislar[satici_adi][satici_cinsi] += tutar
            else:
                self.__satislar[satici_adi][satici_cinsi] = tutar