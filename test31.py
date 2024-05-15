"""
yukarı yaşlar dizisi içinde en büyük sayıyı bulan sayı
"""
max = 0
yaslar = [13,17,19,32,6,90,23,4]
for sayi in yaslar:
    if sayi>max:
        max=sayi
print(max)