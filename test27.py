for i in range(1,10):
    for x in range(1,10):
        if x>i:print("-",end=" ")
        if x==i:print("0",end=" ")
        if x<i:print("+",end=" ")
    print()