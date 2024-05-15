line =1
for i1 in range(5):
    for i2 in range(12):
        if line ==1 or line==5:
            print("*",end="")
        else:
            if i2 ==0 or i2==11:
                print("*",end="")
            else:
                print(" ",end="")
    line+=1
    print()