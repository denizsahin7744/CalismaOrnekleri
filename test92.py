def faktoriyel(sayi:int):
    for num in range(1,sayi,1):
        sayi*=num
    print(sayi)
    return sayi

faktoriyel(5)