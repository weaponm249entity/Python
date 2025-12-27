from functools import reduce

# --- 1. NESNE YÖNELİMLİ KISIM (OOP) ---
# Ürünleri ve Müşteriyi "Nesne" olarak modelliyoruz.
# Neden? Çünkü bunlar gerçek hayat varlıklarıdır, özellikleri vardır.

class Urun:
    def __init__(self, isim, fiyat):
        self.isim = isim
        self.fiyat = fiyat

class Musteri:
    def __init__(self, isim, bakiye):
        self.isim = isim
        self.bakiye = bakiye

# --- 2. FONKSİYONEL PROGRAMLAMA KISMI (FP) ---
# Hesaplamaları "Saf Fonksiyonlar" ile yapıyoruz.
# Dikkat: Bu fonksiyonlar dışarıdaki hiçbir veriyi değiştirmez, sadece yeni değer üretir.
# Neden? Hesaplama hatası olmasın, test etmesi kolay olsun diye.

def kdv_uygula(fiyat):
    """Saf fonksiyon: Sadece girdiği işler, çıktı verir."""
    return fiyat * 1.18

def toplam_hesapla(fiyatlar_listesi):
    """Reduce kullanarak listeyi tek bir toplama indirger."""
    return reduce(lambda x, y: x + y, fiyatlar_listesi)

def sepet_islemcisi(urun_listesi):
    """
    Veri akışı (Pipeline):
    1. Ürünlerden fiyatları çek (Map)
    2. Fiyatlara KDV ekle (Map)
    3. Hepsini topla (Reduce)
    """
    fiyatlar = map(lambda u: u.fiyat, urun_listesi) # Sadece fiyatları al
    kdvli_fiyatlar = map(kdv_uygula, fiyatlar)      # KDV ekle
    genel_toplam = toplam_hesapla(kdvli_fiyatlar)   # Topla
    return genel_toplam

# --- 3. YAPISAL PROGRAMLAMA KISMI (Structured) ---
# Parçaları birleştiren, adım adım çalışan ana blok.
# Neden? Programın bir başlangıcı, akışı ve bitişi olmalı.

def main():
    # Adım 1: Verileri oluştur (Sequence)
    musteri = Musteri("Ahmet", 5000)
    sepet = [
        Urun("Laptop", 3000),
        Urun("Mouse", 200),
        Urun("Klavye", 500)
    ]

    # Adım 2: Fonksiyonel motoru çalıştır
    print(f"Sayın {musteri.isim}, sepetiniz hesaplanıyor...")
    odenecek_tutar = sepet_islemcisi(sepet)

    # Adım 3: Karar ver (Selection - if/else)
    print(f"Toplam Tutar: {odenecek_tutar:.2f} TL")
    
    if musteri.bakiye >= odenecek_tutar:
        musteri.bakiye -= odenecek_tutar # Durum değişimi (State Mutation) burada yapılır
        print("Ödeme Başarılı! Kalan Bakiye: {:.2f} TL".format(musteri.bakiye))
    else:
        print("Yetersiz Bakiye!")

# Programı Başlat
if __name__ == "__main__":
    main()