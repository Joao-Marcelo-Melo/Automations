from .DominioAutomator import *
from source import *

class Folha:
    def __init__(self):
        self.dominio = DominioAutomator()


    def TrocarEmpresa(self, empresa_id):
        pyautogui.press('f8')
        self.dominio.AguardarImagem('TrocarEmpresas')
        pyautogui.write(str(empresa_id))
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(5)

    def CalculodeFerias(self):
        print('Calculando Ferias e Decimo Terceiro')
        self.dominio.CliqueImagem('Processos')
        time.sleep(2)
        self.dominio.CliqueImagem('ProvisoesFerias')
        time.sleep(5)
        pyautogui.write('062023')
        time.sleep(1)
        pyautogui.press('tab')
        pyautogui.write('062023')
        time.sleep(1)
        pyautogui.press('tab', 3)
        pyautogui.press('enter')
        self.dominio.AguardarImagem('Aviso_Ferias')
        time.sleep(5)
        pyautogui.press('enter')
        time.sleep(5)

    def IntegracaoContabil(self):
        print('Executando a Integracao contabil')
        self.dominio.CliqueImagem('Processos')
        self.dominio.CliqueImagem('Integracao')
        self.dominio.AguardarImagem('Integracao_Aguardar')
        pyautogui.write('062023')
        pyautogui.press('tab', 2)
        pyautogui.write('062023')
        self.dominio.CliqueImagem('Exportar_Ferias')
        self.dominio.CliqueImagem('Exportar_13')
        pyautogui.press('tab', 5)
        pyautogui.press('enter')

    def AguardarLogEmpresa(self):
        print("Aguardando tela 'Integracao Final'")
        if self.dominio.AguardarImagem('Integracao_Final', 30):
            pyautogui.press('enter')

            if self.dominio.AguardarImagem('Atencao', 5):
                pyautogui.press('enter')
                pyautogui.press('esc', 4)

            elif self.dominio.AguardarImagem('Gravado', 5):
                pyautogui.press('esc', 4)

            elif self.dominio.AguardarImagem('Aviso_Final', 5):
                pyautogui.press('enter')
                pyautogui.press('esc', 3)

            elif self.dominio.AguardarImagens('Rubricas', 5):
                pyautogui.press('esc', 4)

            elif self.dominio.AguardarImagens('Aviso_Integracao', 5):
                pyautogui.press('esc', 4)

            elif self.dominio.AguardarImagens('Lancamentos_Nao_lancados', 5):
                pyautogui.press('esc', presses=4)

        elif self.dominio.AguardarImagem('Rubrica1', 30):
            pyautogui.press('esc', presses=3)
