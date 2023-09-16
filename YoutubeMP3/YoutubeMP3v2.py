from pytube import YouTube
import customtkinter as ctk
import os
from preDefinicoes.gui import Gui
from preDefinicoes.github import github

# Feito por Wilson Júnior. GitHub: https://github.com/wilsondesouza #

# Confguração da Interface #
gui = Gui()
 # Confguração da Interface #

# Funções 'BackEnd' # 
class Player ():
    def __init__(self):
        self.path = ""
    def Download(self):
        try:
            if interface.link.get() == "":
                raise ValueError("Este campo não pode ficar vazio")
            url = interface.link.get()
            self.path = ctk.filedialog.asksaveasfilename(title='Salvar Música', filetypes=(("MP3", ".mp3"), ("Todos os tipos", "*.*")))
            YouTube(url).streams.filter(only_audio=True).first().download(filename=self.path)
        except ValueError as e:
            interface.link.configure(placeholder_text=str(e), placeholder_text_color="white")
            def destruirLabel():
                    interface.link.configure(placeholder_text="") 
            gui.gui.after(3000, destruirLabel)

    def music(self):
        try:
            if self.path == "":
                raise ValueError ("Primeiro insira o link e faça o download da música desejada.")
            os.system(self.path)
        except ValueError as e:
            label = ctk.CTkLabel(gui.gui, text = str(e))
            label.place(relx=0.300, rely=0.715)
            def destruirLabel():
                label.destroy() 
            gui.gui.after(3000, destruirLabel)
player = Player()
# Funções 'BackEnd' # 

# Interface Gráfica #
class Interface():
    def __init__(self,gui):
        self.gui = gui
        desc = ctk.CTkLabel(gui.gui, text = "Insira o link do vídeo a ser baixado: ").pack(pady=2)
        self.link = ctk.CTkEntry(gui.gui, width=500)
        self.link.pack()
        downloadButton = ctk.CTkButton(gui.gui, text= "Download", command=player.Download).place(relx=0.320, rely=0.505)
        playButton = ctk.CTkButton(gui.gui, text= "Tocar Música", command=player.music).place(relx=0.520, rely=0.505)
        ctk.CTkLabel(gui.gui, text = 'O programa não respoderá enquanto baixar o vídeo. Retornará ao normal quando finalizar o download').pack()
        github(gui)
interface = Interface(gui)
# Interface Gráfica #v

gui.gui.mainloop()