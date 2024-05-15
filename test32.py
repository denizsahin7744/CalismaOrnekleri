''"""
10 elamanlı dizi içinde sayı bulunan 2 basamaklı sayılardan en küçük olanı bulun
"""
'''
minumum = sayilar[0]
for sayi in sayilar:
    if sayi<minumum:
        minumum = sayi

print(minumum)


'''
'''sayilar = [44,77,99,16,14,63,11,55,18,33]

def min_MyOwn(listc:list):
    minC=listc[0]
    for char in listc:
        if char<minC:
            minC=char
    return minC

print(min_MyOwn(sayilar))

def max_MyOwn(listc:list):
    maxC=listc[0]
    for char in listc:
        if char>maxC:
            maxC=char
    return maxC

print(max_MyOwn(sayilar))


text="test1 test2 test3"
liste = []

print(text.split("1"))


kullanici_Girdisi,sayilar,toplam = int(input("Sayı Giriniz.\n>")),[],0
while kullanici_Girdisi !=0:
    sayilar.append(kullanici_Girdisi)
    kullanici_Girdisi = int(input("Sayı Giriniz.\n>"))
for sayi in sayilar:
    toplam+=sayi
print("Ortalama :",toplam/len(sayilar))

sayilar = [44,77,99,16,14,63,11,55,18,33]
minsayilar =[]
for i in sayilar:
    minumum = sayilar[0]
    for sayi in sayilar:
        if sayi<minumum:
            minumum = sayi
            minsayilar.append(minumum)
            sayilar.remove(minumum)'''

import random
sayilar=[]
tekSayilar=[]
for i in range(10):
    sayilar.append(random.randint(1,100))

for sayi in sayilar:
    if sayi%2!=0:
        tekSayilar.append(sayi)

tekSayilar.sort()
print(tekSayilar)