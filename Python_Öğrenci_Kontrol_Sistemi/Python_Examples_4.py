## Veri tabanına Öğrenci kayıt, listeleme, silme, arama programı


import pymysql.cursors

db = pymysql.connect(host = 'localhost',
                     user = 'root',
                     password = '',
                     db = 'python',
                     charset = 'utf8mb4',
                     cursorclass = pymysql.cursors.DictCursor)

baglanti = db.cursor()


def Ogrenci_Listele():
    baglanti.execute("select * from ogrenciler")
    ogrenciler = baglanti.fetchall()

    print("\n -----   ÖĞRENCİLER   -----\n")

    for i in ogrenciler:
        print(i["No"]," <--> ",i["Adi"]," <--> ",i["Soyadi"])
    
    print("\n")

def Ogrenci_Sorgula(No):
    baglanti.execute("SELECT * FROM ogrenciler where No = '{No}' ".format(No = No))
    kontrol = baglanti.fetchall()
    

    if( len(kontrol) == 0):
        print("\n\nÖğrenci Bulunamadı...\n")
        return
    else:
        baglanti.execute("Select * From ogrenciler where No = '{No}' ".format(No = No))
        ogrenci = baglanti.fetchall()
        print("\n\n",ogrenci[0]["No"]," <--> ",ogrenci[0]["Adi"]," <--> ",ogrenci[0]["Soyadi"],"\n")


def Ogrenci_Ekle(No,Adi,Soyadi):
    baglanti.execute("Select count(*) as ticket from ogrenciler where No = '{No}'".format(No = No))
    sonuc = baglanti.fetchone()
    if(sonuc["ticket"] != 0):
        print("\n-- Bu Numaraya Sahip Öğrenci Bulunmaktadır -- \n")
        return
    else:
        baglanti.execute("insert into ogrenciler (No,Adi,Soyadi) values ('{No}','{Adi}','{Soyadi}')".format(No = No, Adi = Adi,Soyadi = Soyadi))
        db.commit()
        print("\n -- Öğrenci Eklendi -- \n")
        return

def Ogrenci_Sil(No):
    baglanti.execute("Select count(*) as ticket from ogrenciler where No = '{No}' ".format(No = No))
    sonuc = baglanti.fetchone()
    if(sonuc["ticket"] == 0):
        print("\n-- Öğrenci Bulunamadı --\n")
        return
    else:
        baglanti.execute("Delete from ogrenciler where No = '{No}'".format(No = No))
        db.commit()
        print("\n -- Öğrenci Silindi --\n")
        return


print("\n\tİşlemler: \n\n"+
"   1-) Öğrencileri Listele: \n"+
"   2-) Öğrenci Sorgula : \n"+
"   3-) Öğrenci Ekle :\n"+
"   4-) Öğrenci Sil : \n"+
"   5-) Çıkış\n\n")

kontol = 0

secim =int(input("Hangi İşlemi Yapmak İstiyorsunuz --> "))
while(secim <1 or secim>5):
    secim = int(input("Yanlış giriş yaptınız Lütfen Tekrar Giriniz : "))

while True:
    
    if(secim == 1):
        Ogrenci_Listele()
    
    elif(secim == 2):
        try:
            if(kontol == 0):
                No = int(input("Öğrencinin Numarasını Giriniz: "))
            else:
                No = int(input("Hatalı Giriş Lütfen Tekrar Giriniz: "))

        except:
            kontol +=1
            continue
        kontol = 0
        Ogrenci_Sorgula(No)
    
    elif(secim == 3):
        
        try:
            if(kontol == 0):
                No = int(input("Öğrencinin Numarasını Giriniz: "))
            else:
                No = int(input("Hatalı Giriş Lütfen Tekrar Giriniz: "))

        except:
            kontol +=1
            continue

        Adi = input("Öğrencinin Adını Giriniz : ")

        Soyadi = input("Öğrencinin Soyadını Giriniz : ")

        if(No == "" or Adi == "" or Soyadi == ""):
            print("\n -- Lütfen Boş Bilgi Bırakmayınız --\n")
            continue
        Ogrenci_Ekle(No,Adi,Soyadi)

    elif(secim == 4):
        try:
            if(kontol == 0):
                No = int(input("Öğrencinin Numarasını Giriniz: "))
            else:
                No = int(input("Hatalı Giriş Lütfen Tekrar Giriniz: "))

        except:
            kontol +=1
            continue
        kontol = 0
        Ogrenci_Sil(No)

    elif(secim == 5):
        break

    secim =int(input("Hangi İşlemi Yapmak İstiyorsunuz --> "))
    while(secim <1 or secim>5):
        secim = int(input("Yanlış giriş yaptınız Lütfen Tekrar Giriniz : "))


print("Programdan Çıktınız Teşekkürler: ")

