#1-3 ürün bilgisini (id,ad,fiyat) kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız
#2- ürün id bilgisini kullanıcıdan alıp ilgili ürün bilgisini gösterin
"""
urunler={
    '100':{'ad':'Iphone X','fiyat':6000}
}

"""

import os
def clear():os.system("clear")

urunler={}

while True:
    print("0) Çıkış")
    print("1) Veri Gir")
    print("2) Veri Çek")
    komut=input("Komut girin. >")
    clear()

    if komut=="0":
        exit()
    elif komut == "1":
        idn=input("Id girin. >")
        ad=input("Ad girin. >")
        fiyat=input("Fiyat girin. >")
        urunler[idn]={"ad":ad,"fiyat":fiyat}
        clear()
    elif komut=="2":
        idn=input("Id girin. >")
        clear()
        try:
            while urunler[idn][ad]=="":
                idn=input("Id girin. (Geri Dönmek için x yazın) >")
                if idn =="x":break
        except:pass
        print("Ad :",urunler[idn]["ad"],"\nFiyat :",urunler[idn]["fiyat"])
    else:pass