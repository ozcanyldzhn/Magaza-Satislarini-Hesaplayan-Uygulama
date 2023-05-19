class Magaza:
    def __init__(self, magaza_adi, satici_adi, satici_cinsi):
        self.__magaza_adi = magaza_adi
        self.__satislar = {}
        self.ekle_satis(satici_adi, satici_cinsi, 0)