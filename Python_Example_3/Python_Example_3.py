""" < -- Örnek 1 -- >
# Random İsim Üretme Programı
import random

def Name_Generator():
    Names = ["Albert", "Charles", "Nicolas", "Michael", "Anders", "Isaac", "Stephen", "Marie", "Richard"]
    Surnames = ["Einstein", "Darwin", "Copernicus", "Faraday", "Celsius", "Newton", "Hawking", "Curie","Dawkins"]

    return "{0}  {1}".format(random.choice(Names),random.choice(Surnames))


try:
    Count = int(input("Kaç adet İsim Üretmek İStersiniz: "))
except:
    Count = int(input("Lütfen Bir Sayı Gİriniz: "))
    

print("\n")
for i in range(Count):
    print((i+1),". İsim : " + Name_Generator())

print("\n")

"""

""" < -- Örnek 2 -- >
#Celcius - Fahrenheit Dönüştürücü
print("-" * 50)
print("1 -) Celcius to Fahrenheit")
print("2 -) Fahrenheit to Celcius")
print("3 -) Exit")
print("-" * 50)
print("\n")

while True:
    try:
        selection = int(input("Seçiminiz : "))
    except:
        print("Hatalı Giriş \n")
        continue

    while (selection < 1) or (selection > 3):
        selection = int(input("Yanlış Tercih Yaptınız Lütfen Tekrarlayınız : "))
    
    if(selection == 1):
        Celcius = float(input("Celcius : "))
        Fahrenheit = (Celcius * 1.8) + 32
        print("{0} Celcius = {1} Fahrenheit\n".format(Celcius,Fahrenheit))
    elif(selection == 2):
        Fahrenheit = float(input("Fahrenheit : "))
        Celcius = (Fahrenheit - 32)/1.8
        print("{0} Fahrenheit = {1} Celcius \n".format(round(Fahrenheit,2),round(Celcius,2)))
    elif(selection == 3):
        break

print("Programı Kapattınız ...")
"""
""" < -- Örnek 3 -- >

# Şifreleme Ve Şifre Çözme Programı

def Encrypt(text,value):
    
    output = ""
    
    for char in text:
        output += chr(ord(char)+value)
    return output

def Decrypt(text,value):
    
    output = ""
    for char in text:
        output += chr(ord(char) - value)
    return output

print("-" * 50)
print("1 -) Metni Şifrele")
print("2 -) Metni Çöz")
print("3 -) Exit")
print("-" * 50)

while True:
    try:
        selection = int(input("\nSeçiminiz : "))
    except:
        print("Hatalı Giriş \n")
        continue

    while (selection < 1) or (selection > 3):
        selection = int(input("Yanlış Tercih Yaptınız Lütfen Tekrarlayınız : "))
    
    if(selection == 1):
        Text = input("Metni Giriniz : ")
        Value = int(input("Şifrelenme Sayısını Giriniz: "))
        print("Metin = {0}  -- Şifrelenmiş Hali = {1}".format(Text, Encrypt(Text,Value)))
    elif(selection == 2):
        Text = input("Metni Giriniz : ")
        Value = int(input("Şifre Çözülme Sayısını Giriniz: "))
        print("Metin = {0}  -- Çözülmüş Hali = {1}".format(Text, Decrypt(Text,Value)))
    elif(selection == 3):
        break

print("Programı Kapattınız ...")
"""
"""
#  < -- Örnek 4 -- >
# İstenilen Uzunlukta Şifre Oluşturma

import random
import string

def Password_generator(Length,Level,outputs=[]):
    outputs.clear()    
    chars = string.ascii_letters
    if Level <=1:
        chars = "{}{}".format(chars,string.digits)
    elif Level >=2:
        chars = "{}{}".format(chars,string.punctuation)
    
    for i in range(Length):
        outputs.append(random.choice(chars))
    
    return "".join(outputs)

print("-"*50)

while True:
    Length = int(input("Şifrenin Uzunluğunu Giriniz (Çıkış için 0): "))
    if Length == 0:
        break
    Level = int(input("Şifrenin Zorluk Seviyesini Belirleyiniz (1 veya 2) : "))

    print("Şifreniz : {0}".format(Password_generator(Length,Level)))
    print("-"*50)

print("Programdan Çıkış Yaptınız...")
"""