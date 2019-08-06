""" << --- Örnek 1 --->> 
# Python ile Sayı Tahmin Oyunu 

from random import randint
sayi = int(input("Bir ile 100 Arasında Bir Sayı giriniz (Çıkış için 0) :  "))
Rand = randint(1,100)
sayac = 0

while sayi !=0:
    sayac +=1
    if(sayi< Rand):
        print("Daha Büyük Bir Sayı Giriniz.")
    elif(sayi > Rand):
        print("Daha Küçük Bir Sayı Giriniz.")
    else:
        print("Sayıyı {0}. Defada Doğru Tahmin Ettiniz...".format(sayac))
        break
    sayi = int(input("Yeni Tahmininiz (Çıkış İçin 0): "))

#Output
Bir ile 100 Arasında Bir Sayı giriniz (Çıkış için 0) :  50
Daha Küçük Bir Sayı Giriniz.
Yeni Tahmininiz (Çıkış İçin 0): 25
Daha Küçük Bir Sayı Giriniz.
Yeni Tahmininiz (Çıkış İçin 0): 12
Daha Küçük Bir Sayı Giriniz.
Yeni Tahmininiz (Çıkış İçin 0): 6
Daha Büyük Bir Sayı Giriniz.
Yeni Tahmininiz (Çıkış İçin 0): 8
Daha Küçük Bir Sayı Giriniz.
Yeni Tahmininiz (Çıkış İçin 0): 7
Sayıyı 6. Defada Doğru Tahmin Ettiniz...
#

"""

""" << --- Örnek 1 --->> 
# Kullanıcıdan Alınan Tarihin Yılın Kaçıncı Günü Olduğunu Bulan Program

def Artik_Yil_mi(Yil):
    Kontrol = False
    if((Yil % 400 == 0) or (Yil % 4 == 0 and Yil % 100 !=0)):
        Kontrol = True
    return Kontrol

def Kacinci_Gün(Gün,Ay,Yil):
    gunler=[31,28,31,30,31,30,31,31,30,31,30,31]
    Toplam_gun = Gün

    if(Artik_Yil_mi(Yil)):
        günler[1] = 29
    
    for i in range(0,Ay-1):
        Toplam_gun += gunler[i]
    
    return Toplam_gun

Gun = int(input("Gün : "))
Ay = int(input("Ay : "))
Yil = int(input("Yıl : "))
print("Girdiğiniz Tarih : {0} / {1} / {2}".format(Gun,Ay,Yil))
Kontrol_int = int(input("Girdiğiniz Tarih Doğru Mu (1 (Evet) /0 (Hayır) )"))
Kontrol = True

while Kontrol_int==0:
    Gun = int(input("Gün : "))
    Ay = int(input("Ay : "))
    Yil = int(input("Yıl : "))
    print("Girdiğiniz Tarih : {0} / {1} / {2}".format(Gun,Ay,Yil))
    Kontrol_int = int(input("Girdiğiniz Tarih Doğru Mu (1 (Evet) /0 (Hayır) )"))

print("Girdiğiniz Tarih Yılın : {0}. Günü ".format(Kacinci_Gün(Gun,Ay,Yil)))

#Output
Gün : 12
Ay : 03
Yıl : 2019
Girdiğiniz Tarih : 12 / 3 / 2019
Girdiğiniz Tarih Doğru Mu (1 (Evet) /0 (Hayır) )1
Girdiğiniz Tarih Yılın : 71. Günü 
#
"""

"""
#  << --- Örnek 3 --->> 
Count = int(input("Kaç Adet Sayı Gireceksiniz : "))
sayilar = []

for i in range(0 , Count):
    print(i+1, end="")
    Eklenecek = int(input(".Değeri Giriniz : "))
    sayilar.insert(i,Eklenecek)
    
print("\nEklediğiniz Değerler => ",sayilar , "\n")
sayac = 0 
for sayi in sayilar:
	if sayi%5 == 0:
		print(sayi , "5'in Katidir")
		sayac = sayac+1
        
print("5'in Katı olan Sayi Adeti : " , sayac)	

# Output
Kaç Adet Sayı Gireceksiniz : 5
1.Değeri Giriniz : 1
2.Değeri Giriniz : 2
3.Değeri Giriniz : 5
4.Değeri Giriniz : 9 
5.Değeri Giriniz : 15

Eklediğiniz Değerler =>  [1, 2, 5, 9, 15] 

5 5'in Katidir
15 5'in Katidir
5'in Katı olan Sayi Adeti :  2
#

"""



""" << --- Örnek 4 --->> 
#Veri tabanından Sorgu Çekilen Verileri Console'a yazdıran Program

import pymysql.cursors 

connection = pymysql.connect(host='localhost', #Host Adı
                             user='root', #Erişim Seviyesi
                             password='', #Hostun Şifresi
                             db='twitter', #Veri Tabanının Adı
                             charset='utf8mb4', #Sonuçların Türkçe Karakter Olması Durumunda
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM uyeler"
        cursor.execute(sql)

        for row in cursor.fetchall():
            Kullanici_Adi = str(row["kadi"])
            Isim = str(row["isim"])
            print("Kullanıcı Adı : " + Kullanici_Adi)
            print("İsim : " + Isim)

finally:
    connection.close()


#Output
Kullanıcı Adı : Mustafaisik
İsim : Mustafa IŞIK
...
#
"""
"""
# Kullanıcıdan String Alıp Ekrana YAzdıran Form Uygulaması...
from tkinter import *
 
from tkinter import messagebox
 
pencere = Tk()
 
pencere.title("https://github.com/mustafaisikk")
pencere.geometry("400x200")

uygulama = Frame(pencere , width = 400 , height = 200)
uygulama.pack(fill=None, expand=False)
uygulama.grid()
 
Label1 = Label(uygulama)
Label1.config(text = "Bir String Giriniz: ")
Label1.place(x=150, y=10)

Entry1 = Entry(uygulama, bd =2)
Entry1.place(x=120, y=40)


def hello():
    messagebox.showinfo("Output",Entry1.get())

button = Button(uygulama, 
                   text="Yazdır", 
                   fg="red",
                   command=hello)
                
button.place(x = 170, y = 70)

pencere.mainloop()
"""