import time
import pyautogui
import pygetwindow as gw

from selenium import webdriver
from selenium.webdriver.common.by import By

from .sistema import *

class DominioAutomator:

    def LogarDominio(email, senha):
        print("Logando no Domínio Web")
        dominio_login = "https://www.dominioweb.com.br/"

        driver = webdriver.Chrome()
        driver.get(dominio_login)
        driver.maximize_window()

        campo_email = driver.find_element(By.XPATH, "/html/body/app-root/app-login/div/div/fieldset/div/div/section/form/label[1]/span[2]/input")
        campo_email.send_keys(email)
        campo_senha = driver.find_element(By.XPATH, "/html/body/app-root/app-login/div/div/fieldset/div/div/section/form/label[2]/span[2]/input")
        campo_senha.send_keys(senha)

        botao_entrar = driver.find_element(By.XPATH, "/html/body/app-root/app-login/div/div/fieldset/div/div/section/form/div/button")
        botao_entrar.click()
        time.sleep(5)

        pyautogui.press('tab', presses=2)
        pyautogui.press('enter')

        while True:
            janela_ativa = gw.getActiveWindow()
            if janela_ativa is not None and janela_ativa.title == "Lista de Programas":
                return True
            time.sleep(1)


    def LogarModulo(usuario, senha, modulo):
        print("Logando no módulo: "+ modulo)
        SistemaAutomator().CliqueImagem('folha', 2)
        time.sleep(20)
        pyautogui.write(usuario)
        pyautogui.press("tab")
        pyautogui.write(senha)
        pyautogui.press("tab", presses=2)
        pyautogui.press("enter")