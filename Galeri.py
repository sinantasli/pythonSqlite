
import sqlite3

import time

class Arac():
    def __init__(self,marka,model,motor,yıl,km):
        self.marka=marka
        self.model= model
        self.motor= motor
        self.yıl=yıl
        self.km=km

    def __str__(self):
        return "Marka: {}\n, Model: {}\n, Motor: {}\n, Yıl: {}\n, KM: {}\n".format(self.marka,self.model,self.motor,self.yıl,self.km)


class Galerii():
    def __init__(self):
        self.baglanti_kur()

    def baglanti_kur(self):
        self.con =sqlite3.connect("Galeri.db")
        self.cursor = self.con.cursor()
        sorgu = "CREATE TABLE IF NOT EXISTS otomobil(Marka TEXT, Model TEXT, Motor INT, Yıl INT, KM INT)"
        sorgu2 = "CREATE TABLE IF NOT EXISTS panelvan(Marka TEXT, Model TEXT, Motor INT, Yıl INT, KM INT)"
        sorgu3 = "CREATE TABLE IF NOT EXISTS kamyon(Marka TEXT, Model TEXT, Motor INT, Yıl INT, KM INT)"

        self.cursor.execute(sorgu)
        self.cursor.execute(sorgu2)
        self.cursor.execute(sorgu3)
        self.con.commit()

    def baglanti_sonlandir(self):
        self.con.close()

    def araclari_göster(self,tablo_ismi):
        say=0
        sorgu="SELECT * FROM {}".format(tablo_ismi)
        self.cursor.execute(sorgu)
        araclar=self.cursor.fetchall()
        if(len(araclar)==0):
            print("Galeride {} bulunmuyor.".format(tablo_ismi))
        else:
            for i in araclar:
                arac = Arac(i[0],i[1],i[2],i[3],i[4])
                print(arac)
                say= say+1
            print("\nGaleride {}  adet {} vardır.".format(say,tablo_ismi))

    def arac_sorgula(self,tablo_ismi,marka):
        sorgu ="SELECT * FROM {} where Marka=?".format(tablo_ismi)
        self.cursor.execute(sorgu,(marka,))
        arac = self.cursor.fetchall()
        if(len(arac)== 0):
            print("Galeride {} marka {} bulunmamaktadır.".format(marka,tablo_ismi))
        else:
            aracc =Arac (arac[0][0],arac [0][1], arac [0][2], arac [0][3],arac [0][4])
            print(aracc)
    def arac_sil(self,tablo_ismi,marka):
        sorgu="SELECT * FROM {} WHERE Marka=?".format(tablo_ismi)
        self.cursor.execute(sorgu,(marka,))
        arac=self.cursor.fetchall()
        if(len(arac)==0):
            print("Böyle bir araç yok.")
        else:
            sorgu="Delete From {} where Marka=?".format(tablo_ismi)
            print("araç siliniyor..")
            self.cursor.execute(sorgu,(marka,))
            time.sleep(2)
            print("araç silindi.")
            self.con.commit()

    def arac_ekle(self,tablo_ismi,arac):
        sorgu = "Insert into {} Values (?,?,?,?,?)".format(tablo_ismi)
        self.cursor.execute(sorgu, (arac.marka, arac.model, arac.motor,arac.yıl, arac.km))
        self.con.commit()




