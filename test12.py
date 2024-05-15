sayi1 = int(input("1. sayıyı girin. >"))
sayi2 = int(input("2. sayıyı girin.>"))
sayi3 = int(input("3. sayıyı girin.>"))
ort = (sayi1 + sayi2 + sayi3)/3
if ort >= 80:print("Pek İyi")
elif ort> 50:print("Geçti")
else:print("Kaldı")
print(ort)