import time
import pyautogui
import pygetwindow as gw
import json

from selenium import webdriver
from selenium.webdriver.common.by import By

class SistemaAutomator:
    def CliqueImagem(self, imagem, count=1, botao="LEFT"):
        while True:
            if self.__BuscarImagem(imagem) != False:
                imagem_encontrada = self.__BuscarImagem(imagem)
                self.__Clique(imagem_encontrada, count, botao)
                break
            else:
                continue
            
    def __BuscarImagem(self, imagem):
        caminho_imagem = "img/dominio/" + imagem + ".png"
        posicao = pyautogui.locateOnScreen(caminho_imagem)

        if posicao is not None:
            return posicao
        else:
            return False

    def __Clique(self, posicao="", count=1, botao="LEFT"):
        if posicao is not None:
            centro_x = posicao.left + posicao.width / 2
            centro_y = posicao.top + posicao.height / 2
            pyautogui.click(centro_x, centro_y, clicks=count, button=botao)

    def AguardarImagem(self, imagem, tentativas=0, sleep=1):
        if tentativas == 0:
            while True:
                resultado_busca = self.__BuscarImagem(imagem)

                if resultado_busca == False:
                    time.sleep(sleep)
                else:
                    return True
        else:
            for tentativa in range(tentativas):
                print(tentativa)
                resultado_busca = self.__BuscarImagem(imagem)

                if resultado_busca == False:
                    time.sleep(sleep)
                else:
                    return True
            return False

    def AguardarImagens(self, imagens):
        while True:
            for imagem in imagens:
                PosX, PosY = pyautogui.locateCenterOnScreen(f"img/dominio/{imagem}.png", region=(0, 0, pyautogui.size().width, pyautogui.size().height), grayscale=True, confidence=0.8)
                if PosX is None or PosY is None:
                    time.sleep(1)
                else:
                    return imagem

    def AguardarJanela(self, janela, tempo = 1, tentativas = 0):
        if tentativas == 0:
            while True:
                janela_ativa = gw.getActiveWindow()
                if janela_ativa is not None and janela_ativa.title == janela:
                    return True
                time.sleep(tempo)
        else:
            for tentativa in range(tentativas):
                janela_ativa = gw.getActiveWindow()
                if janela_ativa is not None and janela_ativa.title == janela:
                    return True
                time.sleep(tempo)
            return False
        
    def AlterarValorJson(self, empresa_id, novo_status):
        caminho_json = "src/empresas.json"
        with open(caminho_json) as arquivo:
            conteudo = json.load(arquivo)
        
        for empresa in conteudo:
            if empresa["id"] == empresa_id:
                empresa["status"] = novo_status
        
        with open(caminho_json,'w') as arquivo:
            json.dump(conteudo, arquivo, indent=4)

class DominioAutomator(SistemaAutomator):
    def LogarDominio(self, email, senha):
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

        pyautogui.press('tab', 2)
        pyautogui.press('enter')

        super().AguardarJanela("Lista de Programas")

    def LogarModulo(self, usuario, senha, modulo):
        print("Logando no módulo: " + modulo)
        super().CliqueImagem(modulo, 2)
        time.sleep(20)
        pyautogui.write(usuario)
        pyautogui.press("tab")
        pyautogui.write(senha)
        pyautogui.press("tab", 2)
        pyautogui.press("enter")