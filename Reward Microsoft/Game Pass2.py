# Código para automatizar os pontos ganhos com as missões diárias do Game Pass #

# Programa incompleto #

from time import sleep
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui as pag

def bluestacks():
    pag.press('win')
    pag.write('blu')
    pag.press('enter')

def xbox():
    pag.press('win')
    pag.click(x=209, y=455) # Xbox

def main():
    bluestacks()
    xbox()
    sleep(10)
    pag.click(x=116, y=33) # Perfil
    pag.click(x=116, y=104) # Ir para Perfil
    sleep(3)
    pag.click(x=811, y=396) # Reward
    pag.click(x=1593, y=270) # Detalhe Cloud Gaming
    pag.click(x=815, y=385) # Jogar Cloud Gaming
    sleep(5)
    pag.click(x=207, y=598) # Jogar
    pag.click(x=895, y=643) # Continuar
    sleep(2)
    xbox()
    pag.click(x=45, y=474,clicks=2, interval=.5) # Fallout
    sleep(1)
    bluestacks()
    pag.click(x=815, y=323) # Xbox Mobile 
    sleep(9)
    pag.click(x=319, y=735, clicks=2, interval=.5) # Ícone
    pag.moveTo(x=1304, y=794)
    pag.dragTo(x=1373, y=106)
    pag.click(x=493, y=539) # Jóia
    pag.click(x=959, y=542) # Iniciar Jóia
    sleep(7)
    pag.click(x=909, y=676) # Continue
    pag.press('win')
    pag.write('fall')
    pag.press('enter')
    pag.click(x=800, y=696) # Enter Vault
    bluestacks()

main()
