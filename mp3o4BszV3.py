import os
import yt_dlp
from pydub import AudioSegment

def print_banner():
    banner = """
    Mp3BszV3 / @AvaStrOficial

    ▶︎ •၊၊||၊|။||||။‌‌‌‌‌၊|• 11:11

    / Descarga Musica De Un Solo Url 
    / Escribe salir si ya no deceas usar la herramienta
    """
    print(banner)

def download_video_from_youtube(link, output_path="downloads", video_format="mp3"):
    if video_format == "mp4":
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'noplaylist': True,
        }
    else:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'noplaylist': True,
        }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(link, download=True)
            filename = ydl.prepare_filename(result)
            print(f"Downloaded video: {filename}")
            return filename
    except Exception as e:
        print(f"Failed to download {link}: {e}")
        return None

def convert_to_mp3(file_path):
    try:
        base, ext = os.path.splitext(file_path)
        new_file = base + '.mp3'
        audio = AudioSegment.from_file(file_path)
        audio.export(new_file, format="mp3")
        os.remove(file_path)
        print(f"Converted to MP3: {new_file}")
    except Exception as e:
        print(f"Failed to convert {file_path}: {e}")

def main():
    print_banner()
    output_path = "downloads"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    while True:
        video_format = input("Seleccione el formato de descarga (mp3 o mp4): ").lower()
        if video_format not in ['mp3', 'mp4']:
            print("Formato no válido. Por favor seleccione 'mp3' o 'mp4'.")
            continue

        links = input("Ingrese las URLs de la música de YouTube separadas por comas: ")
        if links.lower() == 'salir':
            break
        urls = [url.strip() for url in links.split(',')]
        for link in urls:
            file_path = download_video_from_youtube(link, output_path, video_format)
            if file_path and video_format == "mp3":
                convert_to_mp3(file_path)

if __name__ == "__main__":
    main()
