import os
import pygame
from tkinter import *
from tkinter import filedialog
from pytube import YouTube

def download_audio(url, output_path):
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download(output_path)
    return stream.default_filename

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def choose_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
    play_audio(file_path)

def download_and_play():
    url = url_entry.get()
    output_path = os.path.join(os.path.expanduser("~"), "Downloads")
    filename = download_audio(url, output_path)
    play_audio(os.path.join(output_path, filename))

# Interface gráfica
root = Tk()
root.title("Download e Reprodução de Música")

url_label = Label(root, text="URL do vídeo:")
url_label.pack()

url_entry = Entry(root, width=50)
url_entry.pack()

download_button = Button(root, text="Baixar e Reproduzir", command=download_and_play)
download_button.pack()

choose_button = Button(root, text="Escolher Arquivo para Reproduzir", command=choose_file)
choose_button.pack()

root.mainloop()
