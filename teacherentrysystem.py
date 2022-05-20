from multiprocessing.sharedctypes import Value
from cv2 import exp

print("""
------------------NOT GİRİŞİ----------------------
------------------FURKAN ÜNAL----------------------
------------------B210109054-----------------------
------------------24.05.2022------------------------
""")


a = 0


print("Ogrendi Not Giris Sistemine Hosgeldiniz...\n")


while a == 0:
    bolumGirisi = input("Lutfen bolum girisi yapiniz.\n")
    if bolumGirisi == "":
        print("Bolum bos birakilamaz.\n")
    else:
        a = 1

print("Girilen bolum : " , bolumGirisi)

b = 0


while b == 0:
    try:
        DersSayisi = int(input("Kaç adet ders girilecek?\n"))
    except ValueError:
        print("Lutfen sayi gir.")
    else:
        b = 1


print("Girilen ders sayisi : " , DersSayisi)

girilenDersler = []


for i in range(1,DersSayisi+1,1):
    DersGiris = input("Ders Giriniz : ")
    girilenDersler.append(DersGiris)



print("Girilen Dersler = ",girilenDersler)

for y in girilenDersler:

    girilenDegerlendirmeler = []
    
    girilenAgirlikYuzdeleri = []

    try:
        degerlendirmeSayisi = int(input("{} dersi icin , kac adet degerlendirme girilecek?\n".format(y)))
    except ValueError:
        print("Lütfen sayi gir.")

    for i in range(1,degerlendirmeSayisi+1,1):
        degerlendirmeGiris = input("Degerlendirme Giriniz : ")
        girilenDegerlendirmeler.append(degerlendirmeGiris)

    print("{} Dersi icin girilen degerlendirmeler {}".format(y,girilenDegerlendirmeler))

    for i in range(1,degerlendirmeSayisi+1,1):
        agirlikYuzdeleri = int(input("{} dersine girdiginiz degerlendirmeler icin, agirlik yuzdeleri ne olacak?\n".format(y)))
        girilenAgirlikYuzdeleri.append(agirlikYuzdeleri)

    print("{} dersinin degerlendirmelerine girdiginiz agirlik yuzdeleri {}".format(y,girilenAgirlikYuzdeleri))




girilenOgrNolar = []
girilenOgrAdlar = []



for z in girilenDersler:



    c = 0

    while c == 0:
        try:
            girilecekOgrenciSayisi = int(input("{} dersi icin, kac adet ogrenci girilecek?\n".format(z)))
        except ValueError:
            print("Sayi gir.")

        if girilecekOgrenciSayisi > 20 or girilecekOgrenciSayisi < 5:
            print("Girilen ogrenci sayisi 20'den fazla, 5 den az olamaz.")
        else:
            c = 1
            
    for x in range(0,girilecekOgrenciSayisi,1):
        x = x + 1
        ogrNo = input("{}. ogrenci icin numara girin.".format(x))
        girilenOgrNolar.append(ogrNo)

    for x in range(0,girilecekOgrenciSayisi,1):
        x = x + 1 
        ogrAd = input("{}. ogrenci icin adi girin.".format(x))
        girilenOgrAdlar.append(ogrAd)


## güncelleme olayı

guncelDers = []
guncelDegerlendirme = []
guncelAgirlik = []
guncelOgrNo = []
guncelOgrAd = []


print("\n")
print("1.Ders Degisikligi\n2.Degerlendirme Degisikligi\n3.Agirlik Yuzdesi Degisikligi\n4.Ogrenci Numara Degisikligi\n5.Ogrenci Ad Degisikligi")



l = 0
while l == 0:   
    try:
        secim = int(input("Degistirmek istediginiz bilginin numarasini girin.\ndegistirmek istemiyorsaniz 6ya basin.\n"))
    except ValueError:
        print("Sayi giriniz.")

    if secim == 1:
        print("Su anda sisteme kayitli olan dersler = " , girilenDersler)

        for p in girilenDersler:
            GuncelDersGiris = input("Yeni Ders adi = ")
            guncelDers.append(GuncelDersGiris)
    
        girilenDersler.clear() 
        girilenDersler.extend(guncelDers)
        print("Guncel dersler = ",girilenDersler)        

    elif secim == 2:
   
        for k in girilenDegerlendirmeler:
            print("Su andaki ait degenlendirmeler {}".format(girilenDegerlendirmeler))
            guncelDegerlendirmeGiris = input("Yeni Degerlendirmeler = ")
            guncelDegerlendirme.append(guncelDegerlendirmeGiris)
        girilenDegerlendirmeler.clear()
        girilenDegerlendirmeler.extend(guncelDegerlendirme)
        print("Guncel degerlendirmeler = ", girilenDegerlendirmeler)
    
    elif secim == 3:
        for t in girilenAgirlikYuzdeleri:
            print("Su andaki degerlendirmeler {}".format(girilenAgirlikYuzdeleri))
            guncelagirlikGiris = input("Yeni agirlik yuzdeleri = ")
            guncelAgirlik.append(guncelagirlikGiris)
            
        girilenAgirlikYuzdeleri.clear()
        girilenAgirlikYuzdeleri.extend(guncelAgirlik)
        print("Guncel agirlik yuzdeleri = ",girilenAgirlikYuzdeleri)

    elif secim == 4:
        for h in girilenOgrNolar:
            print("Su andaki ogrenci numaralari {}".format(girilenOgrNolar))
            guncelOgrNoGiris = input("Yeni ogrenci numaralari = ")
            guncelOgrNo.append(guncelOgrNoGiris)

        girilenOgrNolar.clear()
        girilenOgrNolar.append(guncelOgrNo)
        print("Guncel ogrenci numaralari = ",girilenOgrNolar)

    elif secim == 5:
        for j in girilenOgrAdlar:
            print("Su anki ogrenci adlari {}".format(girilenOgrAdlar))
            guncelOgrAdGiris = input("Yeni ogrenci adlari = ")
            guncelOgrAd.append(guncelOgrAdGiris)

        girilenOgrAdlar.clear()
        girilenOgrAdlar.append(guncelOgrAd)
        print("Guncel ogrenci adlari = ",girilenOgrAdlar)

    elif secim == 6:
        l = 1

    else:
        print("Gecerli secim yapiniiz...")
        
    devamEtmek = input("Tekrar guncelleme yapmak istiyor musunuz? (e/h)\n")

    if devamEtmek == "e":
       l = 0

    elif devamEtmek == "h":
        l = 1
## silme olayı



print("\n")
print("1.Ders Silme\n2.Degerlendirme Silme\n3.Agirlik Yuzdesi Silme\n4.Ogrenci Numara Silme\n5.Ogrenci Ad Silme")
d = 0


while d == 0:   


    try:
        secim = int(input("silmek istediginiz bilginin numarasini girin.\nDegistirmek istemiyorsanız 6'ya basın.\n"))
    except ValueError:
        print("Sayi giriniz.")


    if secim == 1:
        for p in girilenDersler:
            print("Su anda sisteme kayitli olan dersler = " , girilenDersler)
            hangisiniSilmek = int(input("Silmek istediginiz dersi soldan saga 1den baslayarak secin."))
            girilenDersler.pop(int(hangisiniSilmek)-1)
           
        print("Guncel dersler = ",girilenDersler)        

    elif secim == 2:
        
        for k in girilenDegerlendirmeler:
            print("Su andaki ait degenlendirmeler {}".format(girilenDegerlendirmeler))
            hangisiniSilmek2 = int(input("Silmek istediginiz degerlendirmeyi soldan saga 1den baslayarak secin."))
            girilenDegerlendirmeler.pop(int(hangisiniSilmek2)-1)
                 
        print("Guncel degerlendirmeler = ", girilenDegerlendirmeler)
    
    elif secim == 3:
        for t in girilenAgirlikYuzdeleri:
            print("Su andaki degerlendirmeler {}".format(girilenAgirlikYuzdeleri))
            hangisiniSilmek3 = input("Silmek istediginiz agirlik yuzdesini soldan saga 1den baslayarak secin.")
            girilenAgirlikYuzdeleri.pop(int(hangisiniSilmek3)-1)
           
        print("Guncel agirlik yuzdeleri = ",girilenAgirlikYuzdeleri)

    elif secim == 4:
       
        for h in girilenOgrNolar:
            print("Su andaki ogrenci numaralari {}".format(girilenOgrNolar))
            hangisiniSilmek4 = input("Silmek istediginiz ogrenci numarasini soldan saga 1den baslayarak secin.")
            girilenOgrNolar.pop(int(hangisiniSilmek3)-1)
          
        print("Guncel ogrenci numaralari = ",girilenOgrNolar)

    elif secim == 5:
        for j in girilenOgrAdlar:
            print("Su anki ogrenci adlari {}".format(girilenOgrAdlar))
            hangisiniSilmek5 = input("Silmek istediginiz ogrenci adlarini soldan saga 1den baslayarak secin. ")
            girilenOgrAdlar.pop(int(hangisiniSilmek5)-1)

        print("Guncel ogrenci adlari = ",girilenOgrAdlar)
    
    elif secim == 6:
        d = 1

    else:
        print("Gecerli secim yapiniiz...")
        
    devamEtmek2 = input("Tekrar silme islemi yapmak istiyor musunuz? (e/h)\n")

    if devamEtmek == "e":
        d = 0

    elif devamEtmek == "h":
        d = 1

## sisteme kayıtlı bilgilere not girme olayı




"""6.Öğretmen önce bölüm adını, sonra ders adını,
sonra değerlendirme adını, 
öğrenci adı veya numarasını seçerek ilgili
değerlendirme bölümüne not girebilecektir."""


k = 0
while k == 0:


    print("Once bolum adi, sonra ders adi sonra ogrenci adi girerek ilgili degerlendirme bolumune not giris yapiniz.")

    print("Secilen Bolum = {}".format(bolumGirisi))

    dersSec = input("Not girisi icin ders sec.\nDersler = {}\n".format(girilenDersler))

    for w in girilenDersler:

        if dersSec == w:
            print("Secilen ders = {}".format(dersSec))
        else:
            pass
            
    isimSec = input("Notunu girmek istediginiz ogrenci adini yaziniz.\nisimler = {}\n".format(girilenOgrAdlar))

    for u in girilenOgrAdlar:
        if isimSec == u:
            print("Secilen isim = {}".format(isimSec))
        else:
            pass
            
    puanToplam = []
    degerlendirmeSec = girilenDegerlendirmeler
    print("Su anki degerlendirmeler = {}\n".format(girilenDegerlendirmeler))

    

    for q in girilenAgirlikYuzdeleri:

        notGir = int(input("soldan saga degerlendirmelere not giriniz.\n"))
        puani = ((notGir) * q ) / 100
        puanToplam.append(puani)


    print("Agirlikli toplam puan = ", sum(puanToplam))

    a = sum(puanToplam) 

    ## harf notu hesaplama olayı

    if a >= 90 and a <= 100:
        print("Harf Notu : AA")

    elif a >= 85 and a <= 89:
        print("Harf notu : BA ")

    elif a >= 80 and a <= 84:
        print("Harf Notu : BB")


    elif a >= 75 and a <= 79:
        print("Harf Notu : CB")

    if a >= 70 and a <= 74:
        print("Harf Notu : CC")


    if a >= 65 and a <= 69:
        print("Harf Notu : DC")

    elif a >= 60 and a <= 64:
        print("Harf notu : DD ")


    if a >= 50 and a <= 59:
        print("Harf Notu : FD")
        


    if a < 50:
        print("Harf Notu : FF")
        

    else:
        pass


    devamEtmek3 = input("Not girisine devam etmek istiyor musun? (e/h)\n")

    if devamEtmek3 == "e":
        k = 0

    elif devamEtmek3 == 'h':
        print("Sistemden cikiliyor... hoscakal...")
        k = 1
    
    else:
        pass


