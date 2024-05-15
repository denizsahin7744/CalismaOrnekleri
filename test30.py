"""
tanımlanış olan yaşlar dizisiniz içerisindeki 20 den küçük sayıların kaçtane olduğunu bulan programı yazınız
"""

yaslar = [13,17,19,32,6,90,23,4]
counter = 0
for yas in yaslar:
    if yas<=20:
        counter+= 1
        print(yas)
print("20 Yaş altında toplam :",  counter)

