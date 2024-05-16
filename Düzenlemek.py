araba = {
"marka": "Ford",
"model": "Mustang",
"yıl": 1964
}

print(araba) #Değişiklik yapmadan önceki hali

araba["renk"] = "beyaz" #içinde bir renk anahtarı olmamasına rağmen sonradan ekleyebiliyoruz.

print(araba) #Değişiklik yaptıktan sonraki hali

araba["yıl"] = 2020 #içindeki bir anahtarı sonradan değiştirebiliyoruz.
araba.update({"yil":2020})# Buda aynı işi yapıyor.

print(araba) #Değişiklik yaptıktan sonraki hali

if "model" in araba:    #Bir Anahtarın dict'in içinde olup olmadığını kontrol eder.
  print("Model anahtarı bu dict'in içinde bulunmakta.")