from __future__ import unicode_literals
import youtube_dl
import os

print("Insert the link")
link = input("")

SAVE_PATH = '/'.join(os.path.abspath(
    'C:/Users/<$USERNAME>/Music/').split('/')[:3])

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    'outtmpl': SAVE_PATH + '/%(title)s.%(ext)s',
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
