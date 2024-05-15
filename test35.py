import random
sayi=(random.randrange(1,20))
print(sayi)
for x in range(3):
    tahmini_sayi=int(input("deger girin"))
    if tahmini_sayi < 1 or tahmini_sayi > 20:
       print("sayı 1 ile 20 arasında olmalıdır")
       break
    elif tahmini_sayi==sayi:
      print("dogru")
      break
    else:
       print("yanlis")