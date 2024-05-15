sayi1 = int(input("1. Sayıyı Girin.\n>"))
sayi2 = int(input("2. Sayıyı Girin.\n>"))
buyuk=0
if sayi1>sayi2:
    buyuk = sayi1
    sayi1=sayi2
elif sayi2>sayi1:
    buyuk = sayi2
    sayi2=sayi1
else:
    print("Sayılar eşit.")
    exit()
    
print("İki sayı arasındaki fark :",buyuk-sayi2)