kullaniciAdi = input("Kullanıcı Adı girin. \n>")
kullanicisifre = input("Kullanıcı Şifre girin. \n>")

kullanicilar = ["demouser:demosifre","test:testsifre"]

for user in kullanicilar:
    if kullaniciAdi+":"+kullanicisifre ==user:
        print("Giriş Başarılı.")
    else:
        print("Kullanıcı Bulunamadı.")