import pypyodbc
import platform 
import subprocess  
import os

def TumKullanicilariYazdir():
    conn = pypyodbc.connect('Driver={SQL Server};Server=BATUR\BATUR;Database=PythonDB;Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute("select * from kisiler  WHERE ID BETWEEN 0 AND 20")
    #cursor.execute("")
    records = cursor.fetchall() 
    cursor.execute("select @@rowcount")
    rowcount = cursor.fetchall()[0][0]

    print("Toplam Kişi Sayısı: ", rowcount)
    print("_________\n")
    print("Kişiler\n")
    print("_________\n")
    for row in records:

        print("ID = ", row[0], )
        print("Adı Soyadı: ", row[1])
        print("Yaşı: ", row[2])
        print("Maaşı: ", row[3])
        print("Departmanı: ", row[4], "\n")

def KullaniciEkle():
    print("________________________\n")
    print("Kullanıcı Ekleme İşlemi")
    print("________________________\n")

    KisiAd = input("Adını soyadını giriniz: ")
    KisiYas = int(input("Yaşını giriniz: "))
    KisiMaas = int(input("Maaşını giriniz: "))
    Departman = input("Departmanını giriniz: ")

    conn = pypyodbc.connect('Driver={SQL Server};Server=BATUR\BATUR;Database=PythonDB;Trusted_Connection=yes;')
    cursor = conn.cursor()    
    SQLCommand = ("INSERT INTO kisiler(AdSoyad, Yas, Maas, Departman) VALUES (?,?,?,?)")    
    Values = [KisiAd,KisiYas,KisiMaas,Departman]   
    cursor.execute(SQLCommand,Values)       
    conn.commit()       
    print("Ekleme işlemi yapıldı.")   
    conn.close()  
    TumKullanicilariYazdir()




print("Hangi işlemi yapmak istiyorsunuz?")
print("--------------------------------------")
print("1 - Kullanıcı Ekle")
print("2 - Kullanıcı Sil")
print("3 - Tüm Kullanıcıları Göster")
print("4 - Kullanıcı Güncelle")
print("--------------------------------------")

Secim = int(input("Seçiminiz: "))

if Secim == 1:
    
    KullaniciEkle()

elif Secim == 2:
    print(Secim)

elif Secim == 3:
    
    TumKullanicilariYazdir()

elif Secim == 4:
    print(Secim)

else:
    print("Hatalı seçim yaptınız.")