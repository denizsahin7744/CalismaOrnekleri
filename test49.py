boyut = 5
for i in range(5):
    for j in range(5):
        if i == j or i + j == boyut-1:
            print("x ", end="")
        else:
            print("- ", end="")
    print()