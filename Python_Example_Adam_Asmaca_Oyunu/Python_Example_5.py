# Adam Asmaca Oyunu


import os

def Var_mi(tahmin , soru , Bulunanlar):
    index = 0
    bulunan_say = 0

    for i in soru:
        if(i == tahmin):
            Bulunanlar[index] = tahmin
            bulunan_say +=1
        index +=1

    if(bulunan_say == 0):
        return False
    else:
        return True

  

soru = input("Sormak İstediğiniz Kelime : ")
clear = lambda: os.system('clear')
clear()
Bulunanlar = []

for i in range(0,len(soru)):
    Bulunanlar.insert(i," ")

print("\n")
for i in soru:
    if(i == " "):
        print("    ", end = "")
    else:
        print("[  ]", end = "")
    
print("\n")

Hata_Sayisi = 0
cikis = 1
while Hata_Sayisi < 8:
    tahmin = input("Harf Tahmini Yapınız: (Çıkmak için 0) : ")

    if(tahmin == "0"):
        print("\n Oyundan Çıktınız ...")
        break

    while len(tahmin)>1 or len(tahmin)==0:
        tahmin = input("Tahmininiz Hatalıdır Lütfen Tekrar giriniz: ")
    
    if(Var_mi(tahmin,soru,Bulunanlar)):
        print("\nTahmininiz Doğru Son Durum : " , end = "")
        for i in range(0,len(soru)):
            if(soru[i] == " "):
                print("    ", end = "")
            else:
                print("[ "+Bulunanlar[i]+" ]" , end = "")
                
        print("\n")

    else:
        Hata_Sayisi+=1
        print("Tahmininiz Hatalıdır Kalan Hata Sayınız = {0} ...".format(8-Hata_Sayisi))
    
    kontrol = 0
    for i in range(0,len(soru)):
        if(soru[i] != " "):
            if(Bulunanlar[i] == " "):
                kontrol+=1

    if(kontrol == 0):
        print("Oyunu Tamamladınız Tebrikler...")
        break

if(Hata_Sayisi == 8):
    print("Oyunu Kaybettiniz... ")
