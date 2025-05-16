import streamlit as st
import pandas as pd
from utils.video_scraper import extract_videos

st.set_page_config(page_title="VideoSniffer", layout="centered")
st.title("🎥 VideoSniffer")

url = st.text_input("Cole aqui o link da página com vídeos")

if url:
    with st.spinner("Extraindo vídeos..."):
        df = extract_videos(url)
        if df.empty:
            st.warning("Nenhum vídeo encontrado ou link inválido.")
        else:
            st.success(f"{len(df)} vídeos encontrados!")
            st.dataframe(df)
            st.download_button("📥 Baixar como CSV", df.to_csv(index=False), "videos.csv", "text/csv")
