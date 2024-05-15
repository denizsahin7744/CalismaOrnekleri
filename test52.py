sayilar = []
kullanici_Girdisi = int(input("Sayı Giriniz.\n>"))
ort=0
sayac=0
while kullanici_Girdisi !=0:
    if kullanici_Girdisi !=0:
        sayilar.append(kullanici_Girdisi)
    kullanici_Girdisi = int(input("Sayı Giriniz.\n>"))
    
print(sayilar)

for sayi in sayilar:
    ort+=sayi
    sayac+=1

print("Ortalama :",ort/sayac)
    


