"""
Download a song from youtube and convert it to .wav
"""

from __future__ import unicode_literals
import yt_dlp
import sys


def download_from_url(url):
    ydl.download([url])


args = sys.argv[1:]
if len(args) > 2:
    print("Too many arguments.")
    print("Usage: python download_song.py <youtube url> <output directory>")
    print("If a link is given it will automatically convert it to .wav. Otherwise a prompt will be shown")
    print("Example: python download_song.py https://www.youtube.com/watch?v=k4jDpkAWrdA out")
    exit()
if len(args) == 0:
    url=input("Enter Youtube Video/Playlist URL: ")
    out=input("Enter output directory: ")
else:
    url = args[0]
    out = args[1]

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
    }],
    'outtmpl': out+'/%(title)s.%(ext)s'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    download_from_url(url)
