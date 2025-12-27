import time
import json

def faktoriyel(x):
    if x<=0:
        return 1
    return x * faktoriyel(x-1)

def ciftFaktoriyel(x):
    bilgi = {
        "Sayi" : x,
        "Faktoriyel" : [],
        "Cift_Faktoriyel" : [],
        "Suanki_Zaman" : [],
        }
    bilgi["Faktoriyel"].append(faktoriyel(x))
    bilgi["Cift_Faktoriyel"].append(faktoriyel(faktoriyel(x)))
    bilgi["Suanki_Zaman"].append(time.ctime())
    return bilgi



kullaniciBilgisi = ciftFaktoriyel(int(input()))


with open("faktoriyelBilgisi.json","w", encoding="utf-8") as acikJson:
    json.dump(kullaniciBilgisi,acikJson,ensure_ascii=False)