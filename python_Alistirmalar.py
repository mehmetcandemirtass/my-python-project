ilkSayi = int( input("İlk Sayıyı giriniz: "))
ikinciSayi = int( input("İkinci Sayıyı giriniz: "))
islem = input("""Yapmak istediğiniz İslemi Giriniz:
(Toplama: +, Çıkarma: -, Çarpma: x, Bölme /)
""")

if islem == "+":
    print("Sonuç:  " +str(ilkSayi+ikinciSayi))

elif islem == "-":
    print("Sonuç:  " +str(ilkSayi - ikinciSayi))

elif islem == "x":
    print("Sonuç:  " +str(ilkSayi * ikinciSayi))

elif islem == "/":
    print("Sonuç:  " + str(ilkSayi / ikinciSayi))