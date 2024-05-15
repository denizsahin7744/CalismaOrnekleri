listem = [[1,4,7],[2,5,8],[3,6,9]]
listem2=[[],[],[]]
sayac = 0
sayac2 = 0
for listeEleman in listem:
    for i in range(len(listem)):
        try:
            if listem[i][sayac]!=None:
                listem2[sayac2].append(listem[i][sayac])
                print(listem[i][sayac], end="\t")
        except:print(end="\t")
    print()
    sayac2+=1
    if sayac!= len(max(listem,key=len))-1: sayac+=1
    else: break

print(listem)
print(listem2)