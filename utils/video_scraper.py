import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_videos(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Erro ao acessar a URL: {e}")
        return pd.DataFrame()

    soup = BeautifulSoup(response.content, 'html.parser')

    # Exemplo genérico — personalize conforme a estrutura da página
    video_elements = soup.find_all('div', class_='video-container')

    df_data = []

    for video in video_elements:
        df_data.append({
            'ID': video.get('data-id') or '',
            'Source': url,
            'Title': video.find('h3').text.strip() if video.find('h3') else '',
            'Description': video.find('p').text.strip() if video.find('p') else '',
            'Video URL': video.find('a')['href'] if video.find('a') else '',
            'Thumbnail URL': video.find('img')['src'] if video.find('img') else '',
            'Language': 'pt-BR'  # ou use uma detecção automática se necessário
        })

    return pd.DataFrame(df_data)
