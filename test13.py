ort = int(input("Ortalama girin. >"))
while ort >100 or ort <0:
    print("Hatalı Giriş")
    ort= int(input("Ortalama girin. >"))
if ort >= 80:
    print("Pek İyi")
elif ort> 50:
    print("Geçti")
else:
    print("Kaldı")
print(ort)