for x in range(1,11):
    for y in range(1,11):
        if x-y>0:print("+", end=" | ")
        if x-y == 0:print("0", end=" | ")
        if x-y<0:print("-", end=" | ")
    print()