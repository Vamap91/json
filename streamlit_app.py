import streamlit as st
import pandas as pd
from utils.video_scraper import extract_videos

# Configuração da página
st.set_page_config(page_title="VideoSniffer", layout="centered")
st.markdown("<h1 style='text-align: center;'>🎥 VideoSniffer</h1>", unsafe_allow_html=True)

# Entrada do link
url = st.text_input("Cole aqui o link para o JSON de vídeos")

# Processamento
if url:
    with st.spinner("🔍 Extraindo vídeos..."):
        df = extract_videos(url)
        if df.empty:
            st.warning("⚠️ Nenhum vídeo encontrado ou link inválido.")
        else:
            st.success(f"✅ {len(df)} vídeo(s) encontrado(s)!")
            st.dataframe(df)
            st.download_button("📥 Baixar como CSV", df.to_csv(index=False), "videos.csv", "text/csv")
