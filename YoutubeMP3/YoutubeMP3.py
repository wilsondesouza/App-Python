from pytube import YouTube
import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk
import webbrowser
from pygame import mixer

# Feito por Wilson Júnior. GitHub: https://github.com/wilsondesouza #

# Confguração da Interface #
gui = ctk.CTk() 
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
gui.geometry('800x400')  
gui.title('AnyVideo Downloader')
gui.resizable(0,0)
# Confguração da Interface #

# Funções 'BackEnd' # 
class Music():
    def music():
        mixer.music.load("AppPython/YoutubeMP3/media/sounds/music.mp3")
        mixer.music.set_volume(.09)
        mixer.music.play(1)
    def startMusic():
        mixer.init()
        Music.music()
    def stopMusic():
        mixer.music.stop()
    def restartMusic():
        Music.music()

def Download():
    url = Interface.link.get()
    path = ctk.filedialog.asksaveasfilename(title='Salvar Música', filetypes=(("MP3", ".mp3"), ("Todos os tipos", "*.*")))
    YouTube(url).streams.filter(only_audio=True).first().download(filename=path)
def tocarMusica(path):
        mixer.music.load(path)
        mixer.music.set_volume(.09)
        mixer.music.play(1)
# Funções 'BackEnd' # 

Music.startMusic()  


# Funções Visuais #
def callback():
    webbrowser.open_new_tab("https://github.com/wilsondesouza")
# Funções Visuais #

# Interface Gráfica #
class Interface():
    desc = ctk.CTkLabel(gui, text = "Insira o link do vídeo a ser baixado: ")
    desc.pack()
    link = ctk.CTkEntry(gui, width=60)
    link.pack()
    startButton = ctk.CTkButton(gui, text= "Download", command=Download).place(x = 350, y = 50)
    ctk.CTkLabel(gui, text = 'O programa não respoderá enquanto baixar o vídeo. Retornará ao normal quando finalizar o download').place(x = 120, y = 100)
    github = Image.open("AppPython/YoutubeMP3/media/imgs/github.png")
    resizeGitHub = github.resize((30,30))
    finalGitHub = ImageTk.PhotoImage(resizeGitHub)
    link1 = ctk.CTkButton(gui, text=" ", cursor="hand2",image=finalGitHub, bg_color="transparent", hover=False ,fg_color="transparent", width=1, command=callback)
    link1.place(relx=0.785, rely=0.875,)
# Interface Gráfica #

# Música de Fundo #
class BG_Music():
    play = PhotoImage(file = "AppPython/YoutubeMP3/media/imgs/play.png")
    play_icon = play.subsample(5, 5)
    stop = PhotoImage(file = "AppPython/YoutubeMP3/media/imgs/stop.png")
    stop_icon = stop.subsample(13, 13) 
    stop_music = ctk.CTkButton(gui, text="",image = stop_icon, command=Music.stopMusic).place(x = 80, y = 140) 
    restart_music = ctk.CTkButton(gui, text="",image = play_icon, command=Music.restartMusic).place(x = 30, y = 140) 
# Música de Fundo #

gui.mainloop()