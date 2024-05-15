import random;
sayac,dogrusayi = 0,random.randint(1,20)
while sayac<3:
    userinput = int(input("Sayı giriniz.\n>"))
    if userinput < 1 or userinput >20:
        continue
    if userinput == dogrusayi:
        print("Tebrikler, Kazandınız!");exit()
    else:
        sayac +=1
        print("Sayıyı bilemediniz. Kalan deneme hakkınız :",3-sayac)