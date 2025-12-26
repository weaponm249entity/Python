#boolean
sayi1 = 10
sayi2 = 20
sayiKontrol = sayi1>sayi2

print(sayiKontrol)
print(type(sayiKontrol))

# list

sayi = 10
sayiListesi = [10,20,5,7,8,10]
print(type(sayiListesi))
print(sayiListesi[0])

sayiListesi[1] = 100
print(sayiListesi)

index = 0
toplam = 0
# len(sayiListesi) listenin uzunluğunu (bu örnekte 6) döndürür.
# Böylece index en fazla 5'e kadar gidebilir.
while index < len(sayiListesi):
    print(sayiListesi[index])
    toplam = toplam + sayiListesi[index]
    index += 1

print(f"Sayıların Toplamı: {toplam}")
# dict (dictionary)

kisi_1 = {
    "isim":"mehmetbilen",
    "yas":"39",
    "sehir":"Burdur"
}
kisi_2 = {
    "isim":"atahan",
    "yas":"19",
    "sehir":"Kocaeli"
}
print(kisi_1["isim"])
kisi_2["sehir"] = "İzmit"
yasKontrol = kisi_1["yas"]>kisi_2["yas"]

kisiLisesi = [kisi_1, kisi_2]


# 20 kişilik bir kişi listesi oluştur, başlangıç değerlerini ver.
# Kişi listesi içerisindeki yaş ortalamasını hesapla
# Yaş ortalaması ortalamanın yukarısında olan kişilerin isimlerini ver.