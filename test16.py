# 1 - 11 arasındaki 3 e tam bölünmeyen sayıları alt alta yazdıran programı yaz
sayac = 0
while sayac <=11:
    sayac = sayac +1
    if sayac % 3 == 0:
        continue
    print(sayac)