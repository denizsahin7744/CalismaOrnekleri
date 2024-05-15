'''
klavyeden girilen sayının faktoriyelini hesaplayan program | while
'''

userinput = int(input("Sayı Girin.\n>"))
sayac = userinput
hesaplama =1

while userinput != 0:
    hesaplama = hesaplama * userinput
    userinput = userinput - 1
print(hesaplama)
