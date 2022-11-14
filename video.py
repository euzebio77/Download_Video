from pytube import YouTube
from pytube import Playlist
import moviepy.editor as mp
import re
import os

link = input('Digite o Link do Vídeo:')
#Crian uma pasta com o nome Download
path = (r"Download")
yt = YouTube(link)

#Fazer o Download
ys = yt.streams.get_highest_resolution()
ys.download()
print("Download Completo")