import pyautogui
import time
import json

class SistemaAutomator:
    def __BuscarImagem(self, imagem):
        caminho_imagem = "img/dominio/" + imagem + ".png"
        posicao = pyautogui.locateOnScreen(caminho_imagem)

        if posicao is not None:
            return posicao
        else:
            return False

    def __Clique(self, posicao="", count=1, botao="LEFT"):
        if posicao is not None:
            print(posicao)
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
                    pyautogui.sleep(1)
                
                else:
                    return imagem

    def CliqueImagem(self, imagem, count=1, botao="LEFT"):
        while True:
            if self.__BuscarImagem(imagem) != False:
                imagem_encontrada = self.__BuscarImagem(imagem)
                self.__Clique(imagem_encontrada, count, botao)
                break
            else:
                continue

    def AlterarValorJson(self, caminho_arquivo, empresa_id, novo_status):
        with open(caminho_arquivo) as arquivo:
            conteudo = json.load(arquivo)
        
        for empresa in conteudo:
            if empresa["id"] == empresa_id:
                empresa["Status"] = novo_status
        
        with open(caminho_arquivo,'w') as arquivo:
            json.dump(conteudo, arquivo, indent=4)