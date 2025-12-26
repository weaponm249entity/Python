class SinavKagidi:
    # 1. Özellikler (Attributes): Veriyi tutan kısım
    def __init__(self, ogrenci_adi, vize_notu, final_notu):
        self.isim = ogrenci_adi
        self.vize = vize_notu
        self.final = final_notu
    
    # 2. Metotlar (Methods): İşlemi yapan yetenekler
    def ortalama_hesapla(self):
        """Nesne kendi ortalamasını hesaplamayı 'bilir'."""
        return (self.vize * 0.4) + (self.final * 0.6)

    def rapor_ver(self):
        """Nesne kendini nasıl sunacağını 'bilir'."""
        ort = self.ortalama_hesapla()
        durum = "GEÇTİ" if ort >= 50 else "KALDI"
        print(f"Sayın {self.isim}, Ortalamanız: {ort:.1f} -> Sonuç: {durum}")

# --- ANA PROGRAM (Main) ---
# Burada artık değişkenlerle değil, "Nesnelerle" konuşuyoruz.

# İki farklı nesne yaratıyoruz (Instantiation)
ogrenci1 = SinavKagidi("Ahmet Yılmaz", 40, 60)
ogrenci2 = SinavKagidi("Ayşe Demir", 90, 80)

# Nesnelere "İşini yap" emri veriyoruz
ogrenci1.rapor_ver()
ogrenci2.rapor_ver()