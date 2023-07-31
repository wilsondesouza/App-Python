# Código para automatizar os pontos ganhos com as missões diárias do Game Pass #

from tkinter import *
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
    pag.click(x=798, y=697)
    
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

gui = Tk()  
gui.geometry('800x300')  
gui.title('Game Pass')
gui.iconbitmap("media/imgs/reward.ico")

# Interface #
desc0 = Label(gui, text = "Para utilizar este programa sem maiores erros, é necessário ter instalado alguns programas específicos").place(x = 130, y = 60) 
desc1 = Label(gui, text = 'Tratam-se do game "Fallout Shelter" e do emulador "Bluestacks"').place(x = 250, y = 90) 
desc2 = Label(gui, text = 'OBS: O navegador utilizado será o Edge, caso não o tenha instalado e/ou a conta esteja logada em outro navegador, poderão haver erros').place(x = 40, y = 120)
desc3 = Label(gui, text = 'Caso tenha resolvido estas pendências, clique em "Iniciar" logo abaixo').place(x = 220, y = 150) 
start_button = Button(gui, text = "Iniciar", command=iniciar).place(x = 400, y = 200)

# Música de Fundo #
play = PhotoImage(file = "media/imgs/play.png")
play_icon = play.subsample(5, 5)
stop = PhotoImage(file = "media/imgs/stop.png")
stop_icon = stop.subsample(13, 13) 
stop_music = Button(gui, image = stop_icon, command=stopMusic).place(x = 80, y = 230) 
restart_music = Button(gui, image = play_icon, command=restartMusic).place(x = 30, y = 230) 

gui.mainloop()