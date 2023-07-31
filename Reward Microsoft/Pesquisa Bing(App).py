# Código para automatizar as pesquisas no Bing, afim de ganhar pontos para o Reward Microsoft #

from tkinter import *
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pygame
from time import sleep

def main():
    global nav
    nav = wd.Edge()
    sleep(2)
    nav.get("https://www.bing.com/")
    sleep(6.5)
    pontos()

def pontos():
    i = 0
    for j in range(35):
        sleep(.5),
        nav.find_element(By.ID, "sb_form_q").send_keys(i),
        nav.find_element(By.ID, "sb_form_q").send_keys(Keys.ENTER),
        sleep(.5),
        i += 1
        while i == 10:
            i = 0

def startMusic():
    pygame.mixer.init()
    pygame.mixer.music.load("media/sounds/music.mp3")
    pygame.mixer.music.set_volume(.09)
    pygame.mixer.music.play()

def stopMusic():
    pygame.mixer.music.stop()

def restartMusic():
    pygame.mixer.music.load("media/sounds/music.mp3")
    pygame.mixer.music.set_volume(.09)
    pygame.mixer.music.play()

startMusic()
def iniciar ():
    sleep(2)
    main()
    sleep(2)
    quit()

gui = Tk()  
gui.geometry('800x300')  
gui.title('Pesquisa Bing')
gui.iconbitmap("media/imgs/reward.ico")

# Interface #
desc0 = Label(gui, text = "Para utilizar este programa sem maiores erros, é necessário seguir alguns procedimentos").place(x = 170, y = 60) 
desc1 = Label(gui, text = 'Caso tenha alguma conta de estudante e/ou outra logada em seu computador, desconecte-a').place(x = 155, y = 90) 
desc2 = Label(gui, text = 'Deixe logada, e para sua comobidade, marque a opção "Permanecer conectado", no navegador, a conta que pretende "farmar" os pontos').place(x = 40, y = 120) 
desc3 = Label(gui, text = 'OBS: O navegador utilizado será o Edge, caso não o tenha instalado e/ou a conta esteja logada em outro navegador, poderão haver erros').place(x = 40, y = 150)
desc4 = Label(gui, text = 'Caso tenha seguido todos os procedimentos, clique em "Iniciar" logo abaixo').place(x = 200, y = 180)
start_button = Button(gui, text= "Iniciar", command=iniciar).place(x = 400, y = 230)

# Música de Fundo #
play = PhotoImage(file = "media/imgs/play.png")
play_icon = play.subsample(5, 5)
stop = PhotoImage(file = "media/imgs/stop.png")
stop_icon = stop.subsample(13, 13) 
stop_music = Button(gui, image = stop_icon, command=stopMusic).place(x = 80, y = 230) 
restart_music = Button(gui, image = play_icon, command=restartMusic).place(x = 30, y = 230) 

gui.mainloop()
