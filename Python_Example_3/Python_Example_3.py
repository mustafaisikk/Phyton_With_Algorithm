# X-O-X Oyunu

Oyuncu_1 = input("X -- Oyuncusunun Adi : ")
Oyuncu_2 = input("O -- Oyuncusunun Adi : ")

Tahta = [[["    "],["    "],["    "]],[["    "],["    "],["    "]],[["    "],["    "],["    "]]]

sonuc = 0
sira = 0
Siradaki_kisi = Oyuncu_1
cikis = 0

for i in Tahta:
    print(i)     

while sonuc == 0:
    secim = input("Seciminiz :"+ Siradaki_kisi+" ([Satir] - [Sutun]) (Cikmak icin 0) -- >")
    if(secim == "0"):
        cikis = 1
        break
    secim = secim.split(" - ")
    while (len(secim) != 2) or (int(secim[0])>3) or (int(secim[0])<1)  or (int(secim[1])>3) or (int(secim[1])<1) :
        secim = input("Yanlis Giris Yaptiniz Lutfen Tekrar Giris Yapiniz : ")
        secim = secim.split(" - ")

    if(Tahta[int(secim[0])-1][int(secim[1])-1][0] == "    "):
        if(sira %2 == 0):
            Tahta[int(secim[0])-1][int(secim[1])-1] = "   X  "            
        else:
            Tahta[int(secim[0])-1][int(secim[1])-1] = "   O  "
    else:
        while(Tahta[int(secim[0])-1][int(secim[1])-1][0] != "    "):
            secim = input("Buraya Hamle Zaten Yapıldı Lütfen Tekrar Hamle Yapınız : ")
            secim = secim.split(" - ")

        if (sira % 2 == 0):
            Tahta[int(secim[0]) - 1][int(secim[1]) - 1] = "   X  "
        else:
            Tahta[int(secim[0]) - 1][int(secim[1]) - 1] = "   O  "
    for i in Tahta:
        print(i)        

    for i in Tahta:
        satir = ""
        bitis = 1
        for j in i:
            if(j[0] != "    "):
                if(satir == ""):
                    satir = j
                else:
                    if(satir == j):
                        bitis +=1
        
        if(bitis == 3):
            if (sira % 2 == 0):
                print("Oyunu "+Oyuncu_1+" Kazandı...")
                break
            else:
                print("Oyunu "+Oyuncu_2+" Kazandı...")
                break

        sutun = ["","",""]
        bitis = [1,1,1]
        kazanan = 0

        for i in Tahta:
            if(sutun[0] == ""):
                sutun[0] = i[0]
                sutun[1] = i[1]
                sutun[2] = i[2]
            else:
                if(sutun[0] == i[0] and sutun[0][0] != "    "):
                    bitis[0] +=1
                if(sutun[1] == i[1] and sutun[1][0] != "    "):
                    bitis[1] +=1
                if (sutun[2] == i[2] and sutun[2][0] != "    "):
                    bitis[2] += 1
        if((bitis[0] == 3) or (bitis[1] == 3) or (bitis[2] == 3) ):
            if(sira %2 == 0):
                print("Oyunu " + Oyuncu_1 + " Kazandı...")
                break
            else:
                print("Oyunu " + Oyuncu_2 + " Kazandı...")
                break

    if ((Tahta[0][0] == Tahta[1][1]) and (Tahta[1][1] == Tahta[2][2]) and (Tahta[1][1][0] != "    ")):
        print("Oyunu " + Oyuncu_1 + " Kazandı...")
        break
    elif (Tahta[0][2] == Tahta[1][1] and Tahta[1][1] == Tahta[2][0] and Tahta[1][1][0] != "    "):
        print("Oyunu " + Oyuncu_1 + " Kazandı...")
        break

    if((bitis == 3 ) or (bitis[0] == 3) or (bitis[1] == 3) or (bitis[2] == 3)):
        break



    sira +=1
    if(sira %2 == 0):
        Siradaki_kisi = Oyuncu_1
    else:
        Siradaki_kisi = Oyuncu_2

if(cikis == 1):
    print("Oyundan ciktiniz...")


    