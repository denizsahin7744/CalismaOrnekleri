maas = int(input("Maaş girin. >"))
def vergi_Hesaplama(maas_Tutar):
    if maas_Tutar >=50001:
        return (maas_Tutar/100)*15
    elif maas_Tutar >=70001: 
        return (maas_Tutar/100)*25
    else:
        return "Vergi ödemiyecek"

yillik_Maas = maas*12
print("Yıllık Maaş :",yillik_Maas)
print("Ödenicek Vergi :",vergi_Hesaplama(yillik_Maas))

maas = 0

maas = int(input("Maaş girin. >"))*12 ; print("vergi miktarı : ", (maas/100)*15 if maas >50001 else (maas/100)*25 if maas >70001 else "Vergi ödemicek" , "Yıllık Maaş :",maas)
