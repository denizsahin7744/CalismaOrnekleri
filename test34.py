sayilar = []
negatif = []
pozitif = []
sayac = 10
while sayac != 0:
    sayac -= 1
    sayilar.append(int(input("Sayı Girin. \n>")))
for sayi in sayilar:
    if sayi <0:
        negatif.append(sayi)
    else:
        pozitif.append(sayi)

print("Tüm sayılar :",sayilar,"\n Pozitif Sayılar :",pozitif, "\n Negatif sayılar :",negatif)