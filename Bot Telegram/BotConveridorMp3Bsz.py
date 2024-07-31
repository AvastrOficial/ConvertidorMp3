import os
import yt_dlp
import telebot
from pydub import AudioSegment
from telebot import types

TOKEN = input("[•]Ingresa El Token: ")

bot = telebot.TeleBot(TOKEN)

def print_banner():
    banner = """
    Mp3BszV3 / @AvaStrOficial

    ▶︎ •၊၊||၊|။||||။‌‌‌‌‌၊|• 11:11

    / Descarga Musica De Un Solo Url 
    / Escribe salir si ya no deceas usar la herramienta
    """
    print(banner)

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
        return new_file
    except Exception as e:
        print(f"Failed to convert {file_path}: {e}")
        return None

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    button_github = types.InlineKeyboardButton("𝐆𝐢𝐭𝐡𝐮𝐛 🌑", url="https://github.com/AvastrOficial")
    button_telegram = types.InlineKeyboardButton("𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 🌪", url="https://t.me/+sOf-gqn6SClmNDcx")
    keyboard.add(button_github, button_telegram)

    image_url = "https://telegra.ph/file/695a46e871f1634305bc6.jpg"
    bot.send_photo(message.chat.id, image_url, caption=''' » 𝐄𝐧𝐦𝐚𝐬𝐜𝐚𝐫𝐨 𝐔𝐑𝐋𝐬 𝐲 𝐭𝐞 𝐝𝐨𝐲 𝐞𝐥 𝐜𝐨𝐧𝐭𝐫𝐨𝐥 𝐩𝐚𝐫𝐚 𝐩𝐞𝐫𝐬𝐨𝐧𝐚𝐥𝐢𝐳𝐚𝐫𝐥𝐚𝐬. 🖇

» 𝐄𝐥𝐢𝐠𝐞 𝐮𝐧 𝐧𝐨𝐦𝐛𝐫𝐞 𝐨 𝐭𝐞𝐱𝐭𝐨 𝐩𝐚𝐫𝐚 𝐭𝐮 𝐔𝐑𝐋 𝐞𝐧𝐦𝐚𝐬𝐜𝐚𝐫𝐚𝐝𝐚.🪄''', reply_markup=keyboard)
    bot.reply_to(message, "💨𝐄𝐧𝐯𝐢́𝐚𝐦𝐞 𝐮𝐧𝐚 𝐔𝐑𝐋 𝐝𝐞 𝐲𝐨𝐮𝐭𝐮𝐛𝐞 𝐩𝐚𝐫𝐚 𝐝𝐞𝐬𝐜𝐚𝐫𝐠𝐚𝐫 𝐥𝐚 𝐦𝐮́𝐬𝐢𝐜𝐚:")
    bot.register_next_step_handler(message, download_and_convert)

def download_and_convert(message):
    link = message.text
    if link.startswith("https://") or link.startswith("http://"):
        bot.reply_to(message, "🎶𝐃𝐞𝐬𝐜𝐚𝐫𝐠𝐚𝐧𝐝𝐨 𝐲 𝐜𝐨𝐧𝐯𝐞𝐫𝐭𝐢𝐞𝐧𝐝𝐨 𝐚 𝐌𝐏𝟑...")
        output_path = "downloads"
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        mp4_file = download_video_from_youtube(link, output_path)
        if mp4_file:
            mp3_file = convert_to_mp3(mp4_file)
            if mp3_file:
                with open(mp3_file, 'rb') as audio:
                    bot.send_audio(message.chat.id, audio)
                os.remove(mp3_file)
            else:
                bot.reply_to(message, "💢𝐄𝐫𝐫𝐨𝐫 𝐚𝐥 𝐜𝐨𝐧𝐯𝐞𝐫𝐭𝐢𝐫 𝐞𝐥 𝐚𝐫𝐜𝐡𝐢𝐯𝐨 𝐚 𝐌𝐏𝟑.")
        else:
            bot.reply_to(message, "💢𝐄𝐫𝐫𝐨𝐫 𝐚𝐥 𝐝𝐞𝐬𝐜𝐚𝐫𝐠𝐚𝐫 𝐞𝐥 𝐯𝐢𝐝𝐞𝐨 𝐝𝐞 𝐘𝐨𝐮𝐓𝐮𝐛𝐞.")
    else:
        bot.reply_to(message, "📌𝐏𝐨𝐫 𝐟𝐚𝐯𝐨𝐫, 𝐞𝐧𝐯𝐢́𝐚 𝐮𝐧𝐚 𝐔𝐑𝐋 𝐝𝐞 𝐘𝐨𝐮𝐓𝐮𝐛𝐞 𝐯𝐚́𝐥𝐢𝐝𝐚.")

bot.polling(none_stop=True)
