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

    def get_toplam_satis_tutari(self):
        toplam_tutar = 0
        for satis_bilgileri in self.__satislar.values():
            for tutar in satis_bilgileri.values():
                toplam_tutar += tutar
        return toplam_tutar

    def __str__(self):
        sonuc = f"Mağaza adı: {self.__magaza_adi}\n"
        for satici_adi, satis_bilgileri in self.__satislar.items():
            for cins, tutar in satis_bilgileri.items():
                sonuc += f"{cins.title()} satıcısı {satici_adi.title()} için toplam satış tutarı: {tutar} TL'dir.\n"
        sonuc += f"{self.__magaza_adi} mağazasının toplam satış tutarı: {self.get_toplam_satis_tutari()} TL'dir.\n"
        return sonuc

