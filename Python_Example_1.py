""" << --- Örnek 1 --->>  
# Kullanıcıdan Adını String Alıp Ekrana Yazdıran Program

isim = input("Adınız: ")
print("Merhabalar" , isim)

# Output
Adınız: Mustafa
Merhabalar Mustafa
#
"""


""" << --- Örnek 2 --->> 
# Kullanıcıdan Alınan iki sayının Toplamını Bulan Program
sayi_1 = input("Birinci Sayiyi Giriniz: ") 
sayi_2 = input("İkinci Sayiyi Giriniz: ") 
toplam = int(sayi_1)+int(sayi_2)

print("Sonuç : ", sayi_1 , "+ " , sayi_2 , " = ", toplam )

#Output
Birinci Sayiyi Giriniz: 10
İkinci Sayiyi Giriniz: 12
Sayi 1 :  10 +  12  =  22
#
"""


""" << --- Örnek 3 --->> 
# Girilen Vize ve Final Notlarının Çan değerini bulan program (vize(%30) , final(%70))

sayi_1 = input("Vize Sınav Sonucunu Giriniz: ")
sayi_2 = input("Final Sınav Sonucunu Giriniz: ")

Ortalama = (int(sayi_1)*(0.3))+(int(sayi_2)*(0.7))

print("Öğrencinin Notu : " , Ortalama)

#Output
Vize Sınav Sonucunu Giriniz: 50
Final Sınav Sonucunu Giriniz: 60
Öğrencinin Notu :  57.0
#
"""


""" << --- Örnek 4 --->> 
# Sınav Notları Girilen Öğrencinin Sınıfı Geçip Geçmediğini Söyleyen Program

Sınav_1 = input("İlk Sınav Notu :  ")
Sınav_2 = input("İkinci Sınav Notu :  ")
Sınav_3 = input("Üçüncü Sınav Notu :  ")

Ortalama = (int(Sınav_1) + int(Sınav_2) + int(Sınav_3))/3

if(Ortalama < 50):
	print("Öğrencinin Notu : ",Ortalama," --> Öğrenci Başarısızdır.")
else:
	print("Öğrencinin Notu : ",Ortalama," --> Öğrenci Başarılıdır.")

#Output
İlk Sınav Notu :  45
İkinci Sınav Notu :  55
Üçüncü Sınav Notu :  80
Öğrencinin Notu :  60.0  --> Öğrenci Başarılıdır.
"""


""" << --- Örnek 5 --->> 
# 1-100 Arası 3′ e ve 5′ e tam bölünen sayıları bulan Program

for i in range(1,101):
	if(i % 3 == 0 and i % 5 ==0 ):
		print("<-",i,"->", end ="") 

		#Print fonksiyonunun bir end parametresi vardır ve bu parametre
		#default olarak "\n" değerini alır buda her print fonksiyonu kullanıldığında çıktıların alt 
		#satıra geçmesine sebep olur çıktıların yan yana yazmasını istiyorsanız end parametresine boş 
		#değer ataması yapabilirsiniz :) 
#Output
 <- 15 -><- 30 -><- 45 -><- 60 -><- 75 -><- 90 ->
"""

""" << --- Örnek 6 --->> 
#Girilen String'i Karakterlerine Ayırma
isim = input("Bir String Giriniz : ")
sayac = 0
while sayac < len(isim):
	print(isim[sayac], end="-")
	sayac += 1
	pass
print("\nString Karakter Biçiminde Listelendi...")

#Output
Bir String Giriniz : Mustafa IŞIK
M-u-s-t-a-f-a- -I-Ş-I-K-
String Karakter Biçiminde Listelendi...
"""


""" << --- Örnek 7 --->> 
#Kullanıcın girdiği iki sayı arasındaki sayıların toplamını gösteren program

toplam = 0
sayi_1 = input("Birinci Sayiyi Giriniz : ")
sayi_2 = input("İkinci Sayiyi Giriniz : ")

for i in range(int(sayi_1)+1 , int(sayi_2)):
	toplam += i

print(sayi_1 , " ile " , sayi_2 , " Arasındaki sayıların Toplamı = " , toplam)
#Biçiminde Yazılabildiği Gibi
#print("{0} ile {1} Arasındaki sayıların Toplamı = {2}" . format(sayi_1,sayi_2,toplam))	
#Biçiminde de yazılabilir.


#Output
Birinci Sayiyi Giriniz : 10
İkinci Sayiyi Giriniz : 15
10 ile 15 Arasındaki sayıların Toplamı = 50
"""

""" << --- Örnek 8 --->> 
#Girilen Sayının Asal Sayı mı Değil mi olduğunu bulan program

Sayi=input("Bir Sayı Giriniz : ")
sayac = 0
for i in range(2 , int(Sayi)):
	if(int(Sayi) % i == 0):
		sayac +=1
		break
if(sayac == 0):
	print("{0} Sayısı Asaldır. ".format(Sayi))
else:
	print("{0} Sayısı Asal Değildir. " . format(Sayi))
#Output
Bir Sayı Giriniz : 13
13 Sayısı Asaldır. 
"""

"""
# << --- Örnek 9 --->> 
#1 den kullanıcının girmiş olduğu sayıya kadar olan tek ve çift sayıların toplamını ayrı ayrı bulan program

sayi = input("Bir Sayi Giriniz : ")
Çift_Sayilar_toplamı = 0
Tek_Sayilar_toplamı = 0

for i in range(1 , int(sayi)):
	if(i%2 == 0):
		Çift_Sayilar_toplamı += i
	else:
		Tek_Sayilar_toplamı += i
print("Çift Sayıların Toplamı = {0} <--> Tek Sayıların Toplamı = {1}" . format(Çift_Sayilar_toplamı,Tek_Sayilar_toplamı))

#Output
Bir Sayi Giriniz : 7
Çift Sayıların Toplamı = 12 <--> Tek Sayıların Toplamı = 9
"""

"""
# << --- Örnek 10 --->> 
# Fonksiyon kullanarak yarıçapı girilen dairenin alanını hesaplayan program

def Alan_Hesapla(Yari_Cap):
	return int(Yari_Cap)*int(Yari_Cap)*3.14

Yari_Cap = input("Dairenin Yarıçapını Giriniz : ")

print("Dairenin Alanı : {0}".format(Alan_Hesapla(Yari_Cap)))

# Output

Dairenin Yarıçapını Giriniz : 3
Dairenin Alanı : 28.26
"""
