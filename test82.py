kitaplar={
    "Col_Cicegi":{
        "ad":"Çöl Çiçeği",
        "sayfa":256,
        "stok":99,
        "fiyat":60
    },
    "Copluk":{
        "ad":"Çöplük",
        "sayfa":213,
        "stok":99,
        "fiyat":60
    },
    "Agri_Dagi_Efsanesi":{
        "ad":"Ağrı Dağı Efsanesi",
        "sayfa":117,
        "stok":99,
        "fiyat":60
    }
}
keys= list(kitaplar.keys())
keys2= list(kitaplar[keys[0]].keys())
values = kitaplar.values()
print(keys)
for y in keys2:
    for x in keys:
        print(y,":",kitaplar[x][y]," ",end="")
    print()



