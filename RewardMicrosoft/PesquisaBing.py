# Código para automatizar as pesquisas no Bing, afim de ganhar pontos para o Reward Microsoft #

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

main()
sleep(2)
