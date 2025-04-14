import streamlit as st
from PIL import Image

st.set_page_config(page_title="Altın Hesaplama", layout="centered")

# Logo (isteğe bağlı)
try:
    logo = Image.open("Siyah-PNG.png")
    st.image(logo, use_container_width=True)
except:
    st.warning("Logo yüklenemedi.")

st.title("Altın Hesaplama")

# Kullanıcı manuel USD/KG fiyatı giriyor
usd_kg_satis = st.number_input("USD/KG Satış Fiyatı (manuel giriş)", value=104.680, step=0.001, format="%.3f")

# Kullanıcıdan diğer veriler
altin_gram = st.number_input("Altın Gram", value=1.0, step=1.0)
saflik = st.number_input("Saflık (Milyem)", value=0.585, step=0.001, format="%.3f")
iscilik = st.number_input("İşçilik (Milyem)", value=0.035, step=0.001, format="%.3f")
usd_to_try = st.number_input("Döviz Kuru (1 USD kaç TL?)", value=32.00, step=0.01)

# Hesaplamalar
gram_altin = usd_kg_satis
sadece_iscilik = iscilik * gram_altin
iscilik_dahil_fiyat = (saflik + iscilik) * gram_altin
toplam_fiyat_usd = iscilik_dahil_fiyat * altin_gram

# TL Hesaplamaları
sadece_iscilik_tl = sadece_iscilik * usd_to_try
iscilik_dahil_fiyat_tl = iscilik_dahil_fiyat * usd_to_try
toplam_fiyat_tl = toplam_fiyat_usd * usd_to_try

# Sonuçlar
st.subheader("Sonuçlar (USD)")
st.write(f"1 Gram Sadece İşçilik: **{sadece_iscilik:.4f} USD**")
st.write(f"İşçilik Dahil Gram Fiyatı: **{iscilik_dahil_fiyat:.3f} USD**")
st.write(f"Toplam Fiyat: **{toplam_fiyat_usd:.2f} USD**")

st.subheader("Sonuçlar (TL)")
st.write(f"1 USD = **{usd_to_try:.2f} TL**")
st.write(f"1 Gram Sadece İşçilik: **{sadece_iscilik_tl:.2f} TL**")
st.write(f"İşçilik Dahil Gram Fiyatı: **{iscilik_dahil_fiyat_tl:.2f} TL**")
st.write(f"Toplam Fiyat: **{toplam_fiyat_tl:.2f} TL**")