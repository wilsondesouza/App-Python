# Código para automatizar os pontos ganhos com as missões diárias do Game Pass #

from tkinter import *
from tkinter.ttk import *
from sys import exit
import pyautogui as pag
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from time import sleep
import pygame

def bluestacks():
    pag.press('win')
    pag.write('blu')
    pag.press('enter')

def xbox():
    pag.press('win')
    pag.write('xbox')
    pag.press('enter')

def fallout():
    pag.press('win')
    pag.write('fall')
    pag.press('enter')
    sleep(15)
    pag.press('enter')
    
def cloudGaming():
    options = wd.EdgeOptions()
    options.add_experimental_option("detach", True)
    nav = wd.ChromiumEdge(options=options)
    sleep(2)
    nav.get("https://www.xbox.com/pt-BR/play/games/fortnite/BT5P2X999VH2")
    sleep(11)
    nav.find_element(By.CLASS_NAME, "BaseItem-module__overlayChild___ZHPKo").click()
    sleep(.5)
    pag.click(x=593, y=630)
    sleep(1)
    nav.minimize_window()
    sleep(2)

    pag.click(x=423, y=879)
    sleep(.5)
    pag.click(x=820, y=317)
    sleep(5)
    pag.click(x=1169, y=165)
    pag.click(x=324, y=735)
    
    sleep(300)

    nav.quit()

def iniciar():
    sleep(2)
    xbox()
    sleep(5)
    bluestacks()    
    sleep(2) 
    fallout() 
    sleep(2) 
    cloudGaming()
    stopMusic()
    exit()

def startMusic():
    pygame.mixer.init()
    pygame.mixer.music.load("media/sounds/music.mp3")
    pygame.mixer.music.set_volume(.09)
    pygame.mixer.music.play(1)

def stopMusic():
    pygame.mixer.music.stop()

def restartMusic():
    pygame.mixer.music.load("media/sounds/music.mp3")
    pygame.mixer.music.set_volume(.09)
    pygame.mixer.music.play(1)

startMusic()    

gui = Tk()  
gui.geometry('800x250')  
gui.title('Game Pass')
p1 = PhotoImage(file='media/imgs/icon.png')
gui.iconphoto(False, p1)
gui.resizable(0,0)
style = Style()
style.configure("Custom.TButton", foreground = 'blue', background = 'black', font= "Verdana 10 underline")

# Interface #

def proximo():
    desc1 = '2) Deixe logada - e para sua comobidade, marque a opção "Permanecer conectado", no navegador - a conta que pretende "farmar" os pontos'
    desc0.config(text = desc1)
    desc3 = '3) OBS: O navegador utilizado será o Edge, caso não o tenha instalado e/ou a conta esteja logada em outro navegador, poderá haver erros'
    desc2.config(text = desc3)

def voltar():
    desc1 = "Para utilizar este programa sem maiores erros, é necessário ter instalado alguns programas específicos: "
    desc0.config(text = desc1)
    desc3 = 'Tratam-se do game "Fallout Shelter" e do emulador "Bluestacks"'
    desc2.config(text = desc3)

descButton1 = Button(gui, text = "Próximo ", command = proximo).place(x = 400, y = 50)
desc0 = Label(gui, text = "Para utilizar este programa sem maiores erros, é necessário ter instalado alguns programas específicos: ")
desc0.pack()
descButton2 = Button(gui, text = "Voltar ", command = voltar).place(x = 320, y = 50)
desc2 = Label(gui, text = 'Tratam-se do game "Fallout Shelter" e do emulador "Bluestacks"')
desc2.pack()
desc4 = Label(gui, text = 'Caso tenha resolvido estas pendências, clique em "Iniciar" logo abaixo').place(x = 200, y = 100)
desc5 = Label(gui, text = 'O programa será encerrado automaticamente').place(x = 275, y = 120)
start_button = Button(gui, text= "Iniciar", command=iniciar, style= "Custom.TButton").place(x = 350, y = 140)

# Música de Fundo #
play = PhotoImage(file = "media/imgs/play.png")
play_icon = play.subsample(5, 5)
stop = PhotoImage(file = "media/imgs/stop.png")
stop_icon = stop.subsample(13, 13) 
stop_music = Button(gui, image = stop_icon, command=stopMusic).place(x = 80, y = 180) 
restart_music = Button(gui, image = play_icon, command=restartMusic).place(x = 30, y = 180) 

gui.mainloop()