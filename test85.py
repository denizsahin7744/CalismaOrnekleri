list1 = [1,8,15,17,9,44]
sayi= 10

for x in list1:
    for y in list1:
        if x+y == sayi:
            print("Doğru Kombinasyon Bulundu.\n",x,"+",y)
            exit()

print("Kombinasyon Bulunamadı")

