from .DominioAutomator import *
from setup import *

class Folha:
    def __init__(self):
        self.dominio = DominioAutomator()

    def trocar_empresa(self, empresa_id):
        self.dominio.definir_etapa('Trocando de Empresa')
        pyautogui.press('f8')
        self.dominio.AguardarImagem('dominio/TrocarEmpresa-DEV')
        pyautogui.write(str(empresa_id))
        time.sleep(2)
        pyautogui.press('enter')

    def entrar_aviso_de_vencimento(self):
        self.dominio.CliqueImagem('dominio/Relatorios')
        self.dominio.CliqueImagem('dominio/Outros')
        self.dominio.CliqueImagem('dominio/AvisodeVencimento')

    def definir_configuracoes(self):
        pyautogui.write('01072023')
        pyautogui.press('tab')
        pyautogui.write('30072023')
        self.dominio.CliqueImagem('dominio/ok')

    def checar_dados_existente(self):
        imagem_dados = ['AguardarVencimento', 'sem_dados_para_emitir']
        imagens_dados_verificar = self.dominio.AguardarImagens(imagem_dados)
        return imagens_dados_verificar

    def salvar_pdf(self, empresa_id, primeira_interacao):
        if self.checar_dados_existente() == 'dominio/sem_dados_para_emitir':
            pyautogui.press('enter')
            self.dominio.AlterarValorJson(empresa_id, 'dominio/sem_dados_para_emitir')
        else:
            if primeira_interacao:
                self.dominio.CliqueImagem('dominio/baixarPDF')
                self.dominio.AguardarImagem('dominio/aguardar_janela_baixar_pdf')
                pyautogui.press('tab', 4)
                pyautogui.press('down', 2)
                pyautogui.press('enter')
                self.dominio.CliqueImagem('dominio/Users', 2)
                self.dominio.CliqueImagem('dominio/nexxo', 2)
                self.dominio.CliqueImagem('dominio/desktop', 2)
                self.dominio.CliqueImagem('dominio/envio', 2)
                time.sleep(2)
                pyautogui.press('tab', 4)
                pyautogui.press('enter')
                pyautogui.press('esc')
                print('enviou')

        # while True:
        #     self.dominio.CliqueImagem('save')
        #     time.sleep(10)