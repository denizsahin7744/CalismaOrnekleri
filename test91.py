#klavyeden girilen 2 sayı arasındaki farkı pozitif olarak bulan program
def fark(sayi1:int,sayi2:int):
    if sayi1>sayi2:
        print(sayi1-sayi2)
        return sayi1
    elif sayi1<sayi2:
        print(sayi2-sayi1)
        return sayi2
    else:
        print(0)
        return 0

sayi1=int(input("1. Sayıyı Girin. >"))
sayi2=int(input("2. Sayıyı Girin. >"))
fark(sayi1,sayi2)