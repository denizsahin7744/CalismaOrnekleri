kullanici_ad = input("Kullanıcı adı girin. >")
kullanici_sifre = input("Şifre girin. >")
dogru_ad = "Bilişim"
dogru_sifre = "9prg"
mesaj = ""
if kullanici_ad == dogru_ad and kullanici_sifre == dogru_sifre:
    mesaj = "Hoşgeldin "+kullanici_ad
elif kullanici_ad == dogru_ad and kullanici_sifre != dogru_sifre:
    mesaj = "Şifre Hatalı"
elif kullanici_ad != dogru_ad and kullanici_sifre != dogru_sifre:
    mesaj = "Kullanıcı adı ve şifre hatalı."
print(mesaj)