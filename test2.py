def not_al(sinav_adi):
    """Kullanıcıdan geçerli bir not alana kadar soran fonksiyon (Alt Modül)"""
    while True:
        try:
            not_degeri = float(input(f"{sinav_adi} notunu girin (0-100): "))
            if 0 <= not_degeri <= 100:
                return not_degeri
            else:
                print("Hata: Not 0-100 arasında olmalıdır!")
        except ValueError:
            print("Hata: Lütfen sayısal bir değer girin.")

def durum_belirle(ortalama):
    """Ortalamaya göre geçme/kalma kararı veren fonksiyon (Karar Yapısı)"""
    if ortalama >= 50:
        return "GEÇTİ"
    else:
        return "KALDI"

def ana_program():
    """Programın ana yönetim merkezi (Main Block)"""
    print("--- ÖĞRENCİ NOT SİSTEMİ BAŞLATILIYOR ---")

    # 1. Adım: Verileri Topla
    vize = not_al("Vize")
    final = not_al("Final")

    # 2. Adım: Hesaplama Yap
    ortalama = (vize * 0.4) + (final * 0.6)

    # 3. Adım: Sonucu Göster
    sonuc = durum_belirle(ortalama)
    
    print("-" * 30)
    print(f"Ortalama: {ortalama:.1f}")
    print(f"Sonuç: {sonuc}")
    print("-" * 30)

# Programı Başlat
if __name__ == "__main__":
    ana_program()