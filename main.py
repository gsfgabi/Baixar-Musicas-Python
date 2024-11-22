import os
from yt_dlp import YoutubeDL

def download_playlist_as_mp3(playlist_url, output_dir="downloads"):
    # Cria a pasta de saída se ela não existir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Opções de configuração do yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',  
        'outtmpl': f'{output_dir}/%(title)s.%(ext)s',  
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  
            'preferredcodec': 'mp3',  
            'preferredquality': '192',  
        }],
        'noplaylist': False,  
        '--ffmpeg-location': 'C:YOUTUBE/ffmpeg/bin',
        'ignoreerrors': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        print("Iniciando o download da música/playlist...")
        ydl.download([playlist_url])
        print("Download concluído!")

if __name__ == "__main__":
    
    playlist_url = input("Digite o link da música/playlist do YouTube: ")
    output_directory = input("Digite o nome da pasta de destino (pressione Enter para usar 'downloads'): ") or "downloads"

    try:
        download_playlist_as_mp3(playlist_url, output_dir=output_directory)
        print(f"Arquivos MP3 salvos na pasta '{output_directory}'.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
