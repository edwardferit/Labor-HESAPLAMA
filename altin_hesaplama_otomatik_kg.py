
import streamlit as st
from PIL import Image
import requests

st.set_page_config(page_title="Altın Hesaplama", layout="centered")

# Logo göster
try:
    logo = Image.open("Siyah-PNG.png")
    st.image(logo, use_container_width=True)
except:
    st.warning("Logo yüklenemedi. Dosya adı doğru mu?")

st.title("Altın Hesaplama")

# USD/KG verisini çeken fonksiyon
@st.cache_data(ttl=300)
def get_usd_kg_birebir():
    try:
        url = "https://api.exchangerate.host/convert?from=XAU&to=USD"
        response = requests.get(url).json()
        usd_per_ounce = response["result"]
        usd_per_kg = usd_per_ounce * 32.1507
        return round(usd_per_kg, 3)
    except:
        return 104.680  # Yedek sabit değer

# Otomatik USD/KG fiyatı al
usd_kg_otomatik = get_usd_kg_birebir()

# Kullanıcıya gösterilen fiyat kutusu
usd_kg_satis = st.number_input("USD/KG Satış Fiyatı (otomatik veya manuel)", value=usd_kg_otomatik, step=0.001, format="%.3f")

# Güncelleme butonu
if st.button("USD/KG Güncelle"):
    st.cache_data.clear()
    st.rerun()

# Gram altın USD fiyatı
gram_altin = usd_kg_satis / 1000
st.write(f"Gram Altın Fiyatı (USD): **{gram_altin:.3f}**")

# Diğer kullanıcı girişleri
altin_gram = st.number_input("Altın Gram", value=1.0, step=1.0)
saflik = st.number_input("Saflık (Milyem)", value=0.585, step=0.001, format="%.3f")
iscilik = st.number_input("İşçilik (Milyem)", value=0.035, step=0.001, format="%.3f")

# Hesaplamalar
sadece_iscilik = iscilik * gram_altin
iscilik_dahil_fiyat = (saflik + iscilik) * gram_altin
toplam_fiyat = iscilik_dahil_fiyat * altin_gram

# Sonuçlar
st.subheader("Sonuçlar")
st.write(f"1 Gram Sadece İşçilik (USD): **{sadece_iscilik:.4f}**")
st.write(f"İşçilik Dahil Gram Fiyatı (USD): **{iscilik_dahil_fiyat:.3f}**")
st.write(f"Toplam Fiyat (USD): **{toplam_fiyat:.2f}**")