import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_videos(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    video_elements = soup.find_all('div', class_='video-container')

    df_data = []
    for video in video_elements:
        df_data.append({
            'ID': video.get('data-id'),
            'Source': url,
            'Title': video.find('h3').text if video.find('h3') else '',
            'Description': video.find('p').text if video.find('p') else '',
            'Video URL': video.find('a')['href'] if video.find('a') else '',
            'Thumbnail URL': video.find('img')['src'] if video.find('img') else '',
            'Language': 'pt-BR'
        })

    return pd.DataFrame(df_data)
