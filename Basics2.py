araba = {
  "marka": "Ford",
  "model": "Mustang",
  "yil": 1964,
  "yil": 2020 #bir dict aynı key'i 2 kere kullanmamıza izin vermez
              #bu yüzden en son girilen değeri kullanır
}
print(araba)#araba hakkında tüm bilgileri gösterir
#Çıktı:
'''
{'marka': 'Ford', 'model': 'Mustang', 'yil': 2020}
'''

print(len(araba))#İçinde kaçtane anahtar olduğunu gösterir.

araba2 = {  #Dictler içine string(yazı),bool(pozitif/negatif),int(sayı) ve listeleri alabilir 
  "marka": "Ford",
  "elektrikli": False,
  "yil": 1964,
  "renk": ["kırmızı", "beyaz", "mavi"]
}