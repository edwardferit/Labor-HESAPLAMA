import streamlit as st
from PIL import Image

st.set_page_config(page_title="Altın Hesaplama", layout="centered")

# Logo (varsa)
try:
    logo = Image.open("Siyah-PNG.png")
    st.image(logo, use_container_width=True)
except:
    st.warning("Logo yüklenemedi.")

st.title("Altın Hesaplama")

# USD/KG fiyat girişi (manuel)
usd_kg_satis = st.number_input("USD/KG Satış Fiyatı", value=104.680, step=0.001, format="%.3f")

# Kullanıcı girişleri
altin_gram = st.number_input("Altın Gram", value=1.0, step=1.0)
saflik = st.number_input("Saflık (Milyem)", value=0.585, step=0.001, format="%.3f")
iscilik = st.number_input("İşçilik (Milyem)", value=0.035, step=0.001, format="%.3f")

# Hesaplamalar (USD)
gram_altin = usd_kg_satis
sadece_iscilik = iscilik * gram_altin
iscilik_dahil_fiyat = (saflik + iscilik) * gram_altin
toplam_fiyat_usd = iscilik_dahil_fiyat * altin_gram

# Sonuçlar
st.subheader("Sonuçlar (USD)")
st.write(f"1 Gram Sadece İşçilik: **{sadece_iscilik:.4f} USD**")
st.write(f"İşçilik Dahil Gram Fiyatı: **{iscilik_dahil_fiyat:.3f} USD**")
st.write(f"Toplam Fiyat: **{toplam_fiyat_usd:.2f} USD**")