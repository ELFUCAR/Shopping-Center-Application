import sqlite3
import random
import time
import datetime

con = sqlite3.connect("proje.db")
cursor = con.cursor()

def tabloolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS menu1 (id INT,urun TEXT,fiyat INT)")

    cursor.execute("CREATE TABLE IF NOT EXISTS Alınanlar(id INT, urun TEXT, fiyat INT)")

    con.commit()


def degerekle():
    cursor.execute("INSERT INTO menu1 VALUES('1','Resim Defteri','7tl')")
    cursor.execute("INSERT INTO menu1 VALUES('2','Cizgili Defter','5tl')")
    cursor.execute("INSERT INTO menu1 VALUES('3','Kareli Defter','5tl')")
    cursor.execute("INSERT INTO menu1 VALUES('4','Tukenmez Kalem','3tl')")
    cursor.execute("INSERT INTO menu1 VALUES('5','Kursun Kalem','1tl')")
    cursor.execute("INSERT INTO menu1 VALUES('6','Kırmızı Kalem','1tl')")
    cursor.execute("INSERT INTO menu1 VALUES('7','Silgi','2tl')")
    cursor.execute("INSERT INTO menu1 VALUES('8','Kuru Boya','9tl')")
    cursor.execute("INSERT INTO menu1 VALUES('9','Keceli Kalem','4tl')")
    cursor.execute("INSERT INTO menu1 VALUES('10','Pastel Boya','6tl')")
    cursor.execute("INSERT INTO menu1 VALUES('11','Sulu Boya','7tl')")
    cursor.execute("INSERT INTO menu1 VALUES('12','Oyun Hamuru','6tl')")
    cursor.execute("INSERT INTO menu1 VALUES('13','Not Defteri','3tl')")
    cursor.execute("INSERT INTO menu1 VALUES('14','Seffaf Dosya','1tl')")
    cursor.execute("INSERT INTO menu1 VALUES('15','Karton','2tl')")

    con.commit()





def degeral(s):
    cursor.execute("SELECT * FROM menu1")
    veri=cursor.fetchall()

    for i in veri:
        print(i)

    i = input("Secim yapmak icin E/H")


def secim(i):

     sum=0


     while i == "E":
        c = int(input("\nSectiginiz urunun id numarası:"))
        if (c == 1):
             cursor.execute("INSERT INTO Alınanlar VALUES ('1','Resim Defteri','7tl')")
             sum = sum+7
             i=("\nBaska Urun İcin: E / H")

        elif (c == 2):
             cursor.execute("INSERT INTO Alınanlar VALUES ('2','Cizgili Defter','5tl')")
             sum = sum + 5
             i = ("\nBaska Urun İcin: E / H")

        elif (c == 3):
             cursor.execute("INSERT INTO Alınanlar VALUES ('3','Kareli Defter','5tl')")
             sum = sum + 5
             i = ("\nBaska Urun İcin: E / H")

        elif (c == 4):
             cursor.execute("INSERT INTO Alınanlar VALUES ('4','Tukenmez Kalem','3tl')")
             sum = sum + 3
             i = ("\nBaska Urun İcin: E / H")


        elif (c == 5):
             cursor.execute("INSERT INTO Alınanlar VALUES ('5','Kursun Kalem','1tl')")
             sum = sum + 1
             i = ("\nBaska Urun İcin: E / H")

        elif (c == 6):
             cursor.execute("INSERT INTO Alınanlar VALUES ('6','Kırmızı Kalem','1tl')")
             sum = sum + 1
             i = ("\nBaska Urun İcin: E / H")


        elif (c == 7):
             cursor.execute("INSERT INTO Alınanlar VALUES ('7','Silgi','2tl')")
             sum = sum + 2
             i = ("\nBaska Urun İcin: E / H")


        elif (c == 8):
             cursor.execute("INSERT INTO Alınanlar VALUES ('8','Kuru Boya','9tl')")
             sum = sum + 9
             i = ("\nBaska Urun İcin: E / H")

        elif (c == 9):
             cursor.execute("INSERT INTO Alınanlar VALUES ('9','Keceli Kalem','4tl')")
             sum = sum + 4
             i = ("\nBaska Urun İcin: E / H")

        elif (c == 10):
             cursor.execute("INSERT INTO Alınanlar VALUES ('10','Pastel Boya','6tl')")
             sum = sum + 6
             i = ("\nBaska Urun İcin: E / H")

        elif (c == 11):
             cursor.execute("INSERT INTO Alınanlar VALUES ('11','Sulu Boya','7tl')")
             sum = sum + 7
             i = ("\nBaska Urun İcin: E / H")

        elif (c == 12):
             cursor.execute("INSERT INTO Alınanlar VALUES ('12','Oyun Hamuru','6tl')")
             sum = sum + 6
             i = ("\nBaska Urun İcin: E / H")

        elif (c == 13):
             cursor.execute("INSERT INTO Alınanlar VALUES ('13','Not Defteri','3tl')")
             sum = sum + 3
             i = ("\nBaska Urun İcin: E / H")

        elif (c == 14):
             cursor.execute("INSERT INTO Alınanlar VALUES ('14','Seffaf Dosya','1tl')")
             sum = sum + 1
             i = ("\nBaska Urun İcin: E / H")

        elif (c == 15):
             cursor.execute("INSERT INTO Alınanlar VALUES ('15','Karton','2tl')")
             sum = sum + 2
             i = ("\nBaska Urun İcin: E / H")

        else:
             print ("\n Yanlıs Secim")
             i = ("\nTekrar Secim Yapmak İcin: E / H")


     print("Odenecek Tutar:",sum,"tl")
     i = ("\nBaska Urun İcin: E / H")


def Alınanlar():
    a = []

    zaman = time.time()
    tarih = time.strftime("%m-%d-%Y %H:%M%p")
    a.append("ALINAN TARIH : ")
    a.append(tarih)

    a.append("ALINANALAR :")

    cursor.execute("SELECT * FROM Alınanlar")
    data = cursor.fetchall()
    for i in data:
        a.append(i)

    f = open("kayit.txt", "w")

    f.write(str(a))




def urunekle(s):
    id = int(input("\nid numarası giriniz:"))
    urun = input("\nurunun adını giriniz:")
    fiyat = int(input("\nurunun fiyatını giriniz:"))

    cursor.execute("INSERT INTO  menu1 VALUES (?,?,?)",(id,urun,fiyat))
    cursor.execute("SELECT * FROM menu1")
    veri = cursor.fetchall()

    for i in veri:
        print(i)





a="d"
while a=="d":
 s = input("\nMenuye gitmek icin: g  veya menu eklemek icin: m  =")

 if(s == "g"):
    degeral(s)
    i="E"
    secim(i)
    Alınanlar()

    name = input("ADINIZ:")
    surname = input("SOYADINIZ:")

    Alınanlar()

    f = open("kayit.txt", "r")
    print (f.read())
    d=input("devam etmek için d")




 elif (s == "m"):
  urunekle(s)
  d = input("devam etmek için d")

 else:
  print ("yanlıs secim")
  d = input("devam etmek için d")

