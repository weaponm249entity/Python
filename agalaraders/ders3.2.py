import time
import json

def zamaniBul():
    zaman = time.ctime()
    return zaman

bilgi = zamaniBul()

with open("zamanBilgisi.json","w",encoding="utf-8") as acikJson:
    json.dump(bilgi,acikJson,ensure_ascii=False)