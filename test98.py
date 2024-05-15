cumle=input("Bir cümle giriniz.\n>")+" "
kelime=""
kelimeler=[]
sayac=0
for harf in cumle:
    if harf == " ":
        kelimeler.append(kelime)
        kelime=""
    else:
        kelime+=harf

print(len(kelimeler[-1]))
