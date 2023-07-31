# Código para automatizar as pesquisas no Bing, afim de ganhar pontos para o Reward Microsoft #

from tkinter import *
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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

def iniciar ():
    sleep(2)
    main()
    sleep(2)

gui = Tk()  
gui.geometry('800x300')  
gui.title('Pesquisa Bing')
gui.iconbitmap("reward.ico")

desc0 = Label(gui, text = "Para utilizar este programa sem maiores erros, é necessário seguir alguns procedimentos").place(x = 170, y = 60) 
desc1 = Label(gui, text = 'Caso tenha alguma conta de estudante e/ou outra logada em seu computador, desconecte-a').place(x = 155, y = 90) 
desc2 = Label(gui, text = 'Deixe logada, e para sua comobidade, marque a opção "Permanecer conectado", no navegador, a conta que pretende "farmar" os pontos').place(x = 40, y = 120) 
desc3 = Label(gui, text = 'OBS: O navegador utilizado será o Edge, caso não o tenha instalado e/ou a conta esteja logada em outro navegador, poderão haver erros').place(x = 40, y = 150)
desc4 = Label(gui, text = 'Caso tenha seguido todos os procedimentos, clique em "Iniciar" logo abaixo').place(x = 200, y = 180) 
 
start_button = Button(gui, text = "Iniciar", command=iniciar).place(x = 400, y = 230)

gui.mainloop()
