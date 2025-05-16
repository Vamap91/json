import streamlit as st
import pandas as pd
from utils.video_scraper import extract_videos
from utils.youtube_scraper import extract_youtube_video

st.set_page_config(page_title="VideoSniffer", layout="centered")
st.title("🎥 VideoSniffer")

url = st.text_input("Cole aqui o link da página com vídeos")

if url:
    with st.spinner("Extraindo vídeos..."):
        if "youtube.com" in url or "youtu.be" in url:
            data = extract_youtube_video(url)
            if data:
                df = pd.DataFrame([data])
                st.success("Vídeo do YouTube encontrado!")
                st.dataframe(df)
                st.download_button("📥 Baixar como CSV", df.to_csv(index=False), "youtube_video.csv", "text/csv")
            else:
                st.warning("Não foi possível extrair os dados do vídeo do YouTube.")
        else:
            df = extract_videos(url)
            if df.empty:
                st.warning("Nenhum vídeo encontrado ou link inválido.")
            else:
                st.success(f"{len(df)} vídeos encontrados!")
                st.dataframe(df)
                st.download_button("📥 Baixar como CSV", df.to_csv(index=False), "videos.csv", "text/csv")
