#100 sayaçlı bir döngüde 10 a kadar olan sayılatı yazdıran ve döngüden çıkan programı yazın
sayac = 0
while sayac <= 100:
    sayac = sayac + 1
    print(sayac)
    if sayac == 10:
        break
print("Döngü bitti")