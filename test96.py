girilenYaricap=int(input("Yarı Çap Giriniz\n>"))

hesaplancakPi = 3

def cevre(yaricap,pi):
    return 2*pi*yaricap

def alan(yaricap,pi):
    return pi*yaricap*yaricap

print("Kullanılan Pi :",hesaplancakPi)
print("Çevre :",cevre(girilenYaricap,hesaplancakPi))
print("Alan :",alan(girilenYaricap,hesaplancakPi))