#1 Fonksiyona 2 adet sayı gönderen ve bu sayıların farklarını pozitif olarak ekrana yazdıran program
def pozitifFark(sayi1:int,sayi2:int):
    if sayi1>sayi2:
        return sayi1-sayi2
    elif sayi1<sayi2:
        return sayi2-sayi1
    else:
        return 0
print(pozitifFark(10,7))

#2 Fonksiyona gönderilen sayının faktoriyelini fonksiyonda hesaplayan program
def faktoriyel(sayi:int):
    carpim=1
    for x in range(sayi):
        carpim=sayi*carpim
        sayi-=1
    return carpim
print(faktoriyel(5))

#3 Fonksiyona gönderilen taban üs sayılarına hesaplama yapan program
def carpim(taban,ust):
    retrunValue = 1
    for x in range(ust):
        retrunValue*=taban
    return retrunValue
print(carpim(2,3))

#4 Kullanıcıdan bir üçgene ait 2 adet açı girilecek, açıları fonksiyona gönderip, 3. açıyı ana programda yazdır
def acifarki(aci1,aci2):
    return 180 - aci1 -aci2
print("Kalan Açı :",acifarki(90,40))

#5 bir daireye ait merkez açı bilgisini kullanıcıdan alıp fonksiyona gönderin, bu açıya göre oluşan diliminin daireye göre yüzde biriminden hesaplayan program
def yuzdefarki(girilenYuzde):
    return str((girilenYuzde/360)*100)+" / 100"
print(yuzdefarki(int(input("Açı Girin.\n>"))))

#6 Klavyeden girilen yarıçap bilgisini fonksiyona gönderip, dairenin çevresini ve Çevre = 2*pi*r, Alan = pi*r*r

girilenYaricap=int(input("Yarı Çap Giriniz\n>"))
hesaplancakPi = 3

def cevre(yaricap,pi):
    return 2*pi*yaricap
def alan(yaricap,pi):
    return pi*yaricap*yaricap

print("Çevre :",cevre(girilenYaricap,hesaplancakPi))
print("Alan :", alan(girilenYaricap,hesaplancakPi))

