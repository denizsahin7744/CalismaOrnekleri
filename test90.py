'''
- [ ]  Kendisine gönderilen 2 sayıyı toplayan ve ekrana fonksiyonu yazınız.
- [ ] Kendisine gönderilen 2 sayıdan hangisi büyük bulan fonksiyonu yazınız.
- [ ] Kendisine gönderilen sayının faktöriyelini alan ve sonucu ana programa döndüren fonksiyonu yazınız.
- [ ] Klavyeden girilen bir string yazıya ait karakterlerin her birini bir listeye eleman olarak ekleyen programı yazınız 
- [ ] Aynı elemana sahip listedeki elemanları arayan bulduğunda aynı elemanı silen programı yazınız.
'''

def topla(sayi1:int,sayi2:int):
    print(sayi1+sayi2)

def buyukOlan(sayi1:int,sayi2:int):
    if sayi1>sayi2:
        print(sayi1,", ",sayi2,"'den büyüktür.",sep="")
        return sayi1
    elif sayi1<sayi2:
        print(sayi1,", ",sayi2,"'den küçüktür.",sep="")
        return sayi2
    else:
        print(sayi1," ve ",sayi2,"'bir birine eşittir.",sep="")
        return (sayi2+sayi1)/2

def faktoriyel(sayi:int):
    for num in range(1,sayi,1):
        sayi*=num
    print(sayi)
    return sayi

def strToList(text:str):
    '''
    liste=[]
    for ch in text:
        liste.append(ch)
    print(liste)
    return liste
    '''

    print(list(text))
    return list(text)

def removeMultipled(liste:list):
    liste.sort()
    for it in liste:
        if liste[liste.index(it)] ==liste[liste.index(it)+1]:liste.remove(liste[liste.index(it)])
        print(liste)
        return liste