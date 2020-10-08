from Galeri import *

print("""
******************************

Galerideki Araçlar: otomobil, panelvan, kamyon

yapacağınız işlemi seçin:

1) Araçları Göster 

2) Araç Sorgulama

3) Araç Ekle

4) Arac Sil

çıkış: q

******************************
"""
    )
galeri=Galerii()

while True:
    tablo_ismi = input("Hangi araçla işlem yapacağınızı yazın:")
    islem= input("{} araçları için yapmak istediğiniz işlemi yazın:".format(tablo_ismi))
    if(islem == 'q'):
        print("Program kapatılıyor...")
        galeri.baglanti_sonlandir()
    elif(islem=='1'):
        print("Araçlar listeleniyor..")
        time.sleep(2)
        galeri.araclari_göster(tablo_ismi)
    elif(islem=='2'):
        marka=input("Sorgulamak istediğiniz markayı yazın:")
        print("Sorgulanıyor..")
        time.sleep(3)
        galeri.arac_sorgula(tablo_ismi,marka)
    elif(islem=='3'):
        marka=input("Marka: ")
        model=input("Model: ")
        motor=input("Motor: ")
        yıl=input("Yıl: ")
        km=input("KM: ")
        arac=Arac(marka,model,motor,yıl,km)
        galeri.arac_ekle(tablo_ismi,arac)
    elif(islem=='4'):
        marka=input("Hangi marka aracı silmek istiyorsunuz ?")
        galeri.arac_sil(tablo_ismi,marka)
    else:
        print("Geçersiz işlem")


