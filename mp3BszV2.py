import os
import yt_dlp
from pydub import AudioSegment

def download_video_from_youtube(link, output_path="downloads"):
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

def download_and_convert_youtube_videos(links, output_path="downloads"):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    for link in links:
        audio_file = download_video_from_youtube(link, output_path)
        if audio_file:
            convert_to_mp3(audio_file)

if __name__ == "__main__":
    youtube_links = [
        "",
        ""
  
      
    ]
    download_and_convert_youtube_videos(youtube_links)
