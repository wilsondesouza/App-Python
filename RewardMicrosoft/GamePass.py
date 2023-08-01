# Código para automatizar os pontos ganhos com as missões diárias do Game Pass #

import pyautogui as pag
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from time import sleep

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

xbox()
sleep(5)
bluestacks()    
sleep(2) 
fallout() 
sleep(2) 
cloudGaming()


