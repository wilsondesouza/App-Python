from pytube import YouTube
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import pygame


class Music():

    def music():
        pygame.mixer.music.load("YoutubeMP3/media/sounds/music.mp3")
        pygame.mixer.music.set_volume(.09)
        pygame.mixer.music.play(1)

    def startMusic():
        pygame.mixer.init()
        Music.music()

    def stopMusic():
        pygame.mixer.music.stop()

    def restartMusic():
        Music.music()

def Download():
    url = Interface.link.get()
    path = filedialog.asksaveasfilename(title='Salvar Música', filetype=(("MP3", ".mp3"), ("Todos os tipos", "*.*")))
    YouTube(url).streams.filter(only_audio=True).first().download(filename=path)

Music.startMusic()  

# Configuração Interface #

gui = Tk()  
gui.geometry('800x200')  
gui.title('Youtube MP3')
p1 = PhotoImage(file='YoutubeMP3/media/imgs/reward.png')
gui.iconphoto(False, p1)
gui.resizable(0,0)
style = Style()
style.configure("Custom.TButton", foreground = 'blue', background = 'black', font= "Verdana 10 underline")

# Interface #

class Interface():
    desc = Label(gui, text = "Insira o link do vídeo a ser baixado: ")
    desc.pack()
    link = Entry(gui, width=60)
    link.pack()
    startButton = Button(gui, text= "Download", command=Download, style= "Custom.TButton").place(x = 350, y = 50)
    Label(gui, text = 'O programa não respoderá enquanto baixar o vídeo. Retornará ao normal quando finalizar o download').place(x = 120, y = 100)

# Música de Fundo #
class BG_Music():
    play = PhotoImage(file = "YoutubeMP3/media/imgs/play.png")
    play_icon = play.subsample(5, 5)
    stop = PhotoImage(file = "YoutubeMP3/media/imgs/stop.png")
    stop_icon = stop.subsample(13, 13) 
    stop_music = Button(gui, image = stop_icon, command=Music.stopMusic).place(x = 80, y = 140) 
    restart_music = Button(gui, image = play_icon, command=Music.restartMusic).place(x = 30, y = 140) 

gui.mainloop()