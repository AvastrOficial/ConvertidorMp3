import os
from pytube import YouTube
from pydub import AudioSegment

def download_video_from_youtube(link, output_path="downloads"):
    try:
        yt = YouTube(link)
        video = yt.streams.filter(file_extension='mp4').first()
        out_file = video.download(output_path)
        print(f"Downloaded video: {out_file}")
        return out_file
    except Exception as e:
        print(f"Failed to download {link}: {e}")
        return None

def convert_mp4_to_mp3(file_path):
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
        mp4_file = download_video_from_youtube(link, output_path)
        if mp4_file:
            convert_mp4_to_mp3(mp4_file)

if __name__ == "__main__":
  
    youtube_links = [
        "",
        "",
        "",
        ""
        # Agrega más enlaces aquí
    ]
    download_and_convert_youtube_videos(youtube_links)
