"""
GOREV 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz.
Virgül ve nokta yerine space koyunuz kelime kelime ayırınız. upper metodunu kullanma
 """


text= ["The goal is to turn data into information, and information into insight."]
buyukler=[kelime.upper() for kelime in text]
print(buyukler)

"""
Görev 3: 
Adım 1: Verilen listenin eleman sayısına bakınız.
Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
Adım 4: Sekizinci indeksteki elemanı siliniz.
Adım 5: Yeni bir eleman ekleyiniz.
Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.
"""
lst= ["D","A","T","A","S","C","İ","E","N","C","E"]
"adım 2"
print("0.indeks:", lst[0])
print("10.indeks:", lst[10])

"adım 3"
sub_list = lst[0:4]
print(sub_list)

"adım 4"
del lst[8]
print(lst)

"adım 5"
lst.append("x")
print(lst)

"adım 6"
lst.insert(8,"N")
print(lst)

""" 
GÖREV 4 :
Adım 1: Key değerlerine erişiniz.
Adım 2: Value'lara erişiniz.
Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
Adım 5: Antonio'yu dictionary'den siliniz.
"""

dict = {'Chris':["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25],
}
"Adım 1"
print(dict.keys())

"Adım 2"
print(dict.values())

"Adım 3"
dict['Daisy'][1] = 13
print(dict['Daisy'])

"Adım 4"
dict['Mehmet'] = ["Turkey",24]
print(dict['Mehmet'])

"Adım 5"
del dict['Mehmet']
print(dict)

"""
GÖREV 5: Bir liste alan , listenin ,içerisindeki tek ve çift sayıları ayrı listelere 
         atayan ve bu listeleri return eden fonksiyon yazınız
"""
lst = [2,13,18,93,22]

def func(liste):
    tek_sayilar = []
    cift_sayilar = []

    for sayi in liste:
        if sayi % 2 == 0:
            cift_sayilar.append(sayi)
        else:
            tek_sayilar.append(sayi)


    return tek_sayilar, cift_sayilar

tekler,ciftler = func(lst)
print(tekler)
print(ciftler)

""" 
GÖREV 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri
bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de
tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız. 
"""

ogrenciler = ["Ali","Veli","Ayse","Talat","Ece","Zeynep"]

print("Mühendislik Fakültesi:")
for i, ogrenci in enumerate(ogrenciler[:3],1):
    print(i, ogrenci)

print("Tıp Fakültesi:")
for i, ogrenci in enumerate(ogrenciler[3:],1):
    print(i,ogrenci)

"""Görev 8: Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını
eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
issuperset() → kapsıyor mu?
intersection() → ortak elemanları bulur
difference() → 2. kümeden 1. kümenin çıkartılması sonucu kalanlar"""

kume1 = set(["data","python"])
kume2 = set(["function","data","qcut","lambda","python","miuul"])

def kume_kontrol(kume1, kume2):
    if kume1.issuperset(kume2):  # kume1, kume2'yi kapsıyor mu?
        ortak = kume1.intersection(kume2)
        print("1. küme 2. kümeyi kapsıyor. Ortak elemanlar:", ortak)
    else:
        fark = kume2.difference(kume1)
        print("1. küme 2. kümeyi kapsamıyor. Farklı elemanlar:", fark)
kume_kontrol(kume1, kume2)

def multiply_add(x,y=2):
    return x*y+y
print(multiply_add(3))