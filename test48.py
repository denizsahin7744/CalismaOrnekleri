"""

* - - - *
- * - * -
- - * - -
- * - * -
* - - - *
"""
sayac1 = 1
sayac2 = 5 
for i in range(1,6):
    for i2 in range(1,6):
        if i2 == sayac1:print("\t*",end="")
        elif i2 == sayac2:print("\t*",end="")
        else:print("\t-",end="")
    print()
    sayac1+=1
    sayac2-=1

