import requests
import pandas as pd

def extract_videos(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        videos_json = response.json()
    except Exception as e:
        print(f"Erro ao acessar ou processar o JSON: {e}")
        return pd.DataFrame()

    df_data = []

    for video in videos_json:
        df_data.append({
            'ID': video.get('id', ''),
            'Source': video.get('source', ''),
            'Title': video.get('title', ''),
            'Description': video.get('description', ''),
            'Video URL': video.get('video_url', ''),
            'Thumbnail URL': video.get('thumbnail_url', ''),
            'Language': video.get('language', '')
        })

    return pd.DataFrame(df_data)
