for i1 in range(1,6):
    for i2 in range(1,6):
        if i1+i2==6 or i1==i2:
            print("*",end="") 
        else:
            print("-",end="")
    print()