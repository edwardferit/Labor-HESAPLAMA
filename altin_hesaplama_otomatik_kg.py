
import streamlit as st
from PIL import Image
import requests

st.set_page_config(page_title="Altın Hesaplama", layout="centered")

# Logo (varsa göster)
try:
    logo = Image.open("Siyah-PNG.png")
    st.image(logo, use_container_width=True)
except:
    st.warning("Logo yüklenemedi.")

st.title("Altın Hesaplama")

# --- Altın Fiyatı: exchangerate.host (ons → USD → kg) ---
@st.cache_data(ttl=300)
def get_usd_kg():
    try:
        url = "https://api.exchangerate.host/convert?from=XAU&to=USD"
        response = requests.get(url)
        data = response.json()

        st.subheader("Altın API Yanıtı")
        st.json(data)  # DEBUG: yanıtı göster

        if "result" not in data:
            st.warning("Altın fiyatı alınamadı (result bulunamadı).")
            return 104.680

        usd_per_ounce = data["result"]
        usd_per_kg = usd_per_ounce * 32.1507
        return round(usd_per_kg, 3)
    except Exception as e:
        st.error(f"Altın fiyatı alınamadı: {e}")
        return 104.680

# --- USD → TRY kuru: exchangerate.host ---
@st.cache_data(ttl=300)
def get_usd_to_try():
    try:
        url = "https://api.exchangerate.host/latest?base=USD&symbols=TRY"
        response = requests.get(url)
        data = response.json()
        return round(data["rates"]["TRY"], 2)
    except:
        return 32.00

# Verileri al
usd_kg_otomatik = get_usd_kg()
usd_to_try = get_usd_to_try()

# USD/KG fiyatı kutusu
usd_kg_satis = st.number_input(
    "USD/KG Satış Fiyatı",
    value=usd_kg_otomatik,
    step=0.001,
    format="%.3f"
)

# Yenile butonu
if st.button("USD/KG Güncelle"):
    st.cache_data.clear()
    st.rerun()

# Kullanıcı girişleri
altin_gram = st.number_input("Altın Gram", value=1.0, step=1.0)
saflik = st.number_input("Saflık (Milyem)", value=0.585, step=0.001, format="%.3f")
iscilik = st.number_input("İşçilik (Milyem)", value=0.035, step=0.001, format="%.3f")

# Hesaplamalar
gram_altin = usd_kg_satis
sadece_iscilik = iscilik * gram_altin
iscilik_dahil_fiyat = (saflik + iscilik) * gram_altin
toplam_fiyat_usd = iscilik_dahil_fiyat * altin_gram

# TL karşılığı
sadece_iscilik_tl = sadece_iscilik * usd_to_try
iscilik_dahil_fiyat_tl = iscilik_dahil_fiyat * usd_to_try
toplam_fiyat_tl = toplam_fiyat_usd * usd_to_try

# Sonuçlar
st.subheader("Sonuçlar (USD)")
st.write(f"1 Gram Sadece İşçilik: **{sadece_iscilik:.4f} USD**")
st.write(f"İşçilik Dahil Gram Fiyatı: **{iscilik_dahil_fiyat:.3f} USD**")
st.write(f"Toplam Fiyat: **{toplam_fiyat_usd:.2f} USD**")

st.subheader("Sonuçlar (TL)")
st.write(f"1 USD = **{usd_to_try} TL**")
st.write(f"1 Gram Sadece İşçilik: **{sadece_iscilik_tl:.2f} TL**")
st.write(f"İşçilik Dahil Gram Fiyatı: **{iscilik_dahil_fiyat_tl:.2f} TL**")
st.write(f"Toplam Fiyat: **{toplam_fiyat_tl:.2f} TL**")