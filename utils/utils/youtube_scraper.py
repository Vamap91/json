from pytube import YouTube

def extract_youtube_video(url):
    try:
        yt = YouTube(url)
        return {
            'ID': yt.video_id,
            'Source': 'YouTube',
            'Title': yt.title,
            'Description': yt.description,
            'Video URL': yt.watch_url,
            'Thumbnail URL': yt.thumbnail_url,
            'Language': 'en'
        }
    except Exception as e:
        print(f"Erro ao extrair vídeo do YouTube: {e}")
        return None
