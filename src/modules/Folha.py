from .DominioAutomator import *
from setup import *

class Folha:
    def __init__(self):
        self.dominio = DominioAutomator()

    def trocar_empresa(self, empresa_id):
        pyautogui.press('f8')
        self.dominio.AguardarImagem('dominio/trocar_empresa')
        pyautogui.write(str(empresa_id))
        time.sleep(2)
        pyautogui.press('enter')

    def entrar_aviso_de_vencimento(self):
        self.dominio.CliqueImagem('dominio/relatorios')
        self.dominio.CliqueImagem('dominio/outros')
        self.dominio.CliqueImagem('dominio/aviso_vencimento')

    def definir_configuracoes(self):
        pyautogui.write('01082023')
        pyautogui.press('tab')
        pyautogui.write('31082023')
        self.dominio.CliqueImagem('dominio/ok')

    def checar_dados_existente(self):
        imagem_dados = ['dominio/aguardar_vencimento', 'dominio/sem_dados_para_emitir']
        imagens_dados_verificar = self.dominio.AguardarImagens(imagem_dados)
        return imagens_dados_verificar

    def salvar_pdf(self, empresa_id, primeira_interacao):
        if self.checar_dados_existente() == 'dominio/sem_dados_para_emitir':
            pyautogui.press('enter')
            pyautogui.press('esc', 2)
            self.dominio.AlterarValorJson(empresa_id, 'status', 'sem_dados_para_emitir')
        elif self.checar_dados_existente() == 'dominio/aguardar_vencimento':
            if primeira_interacao:
                self.dominio.CliqueImagem('dominio/baixar_pdf')
                self.dominio.AguardarImagem('dominio/aguardar_janela_baixar_pdf')
                pyautogui.write(str(empresa_id))
                pyautogui.press('tab', 4)
                pyautogui.press('down', 2)
                pyautogui.press('enter')
                self.dominio.CliqueImagem('dominio/users', 2)
                self.dominio.CliqueImagem('dominio/user_pc', 2)
                self.dominio.CliqueImagem('dominio/desktop', 2)
                self.dominio.CliqueImagem('dominio/envio', 2)
                time.sleep(2)
                pyautogui.press('tab', 4)
                pyautogui.press('enter')

                self.dominio.AguardarImagem('dominio/adobe')
                pyautogui.press('esc', 2)
                time.sleep(5)
                pyautogui.press('esc', 2)
                self.dominio.AlterarValorJson(empresa_id, 'status', 'concluido')
            else:
                self.dominio.CliqueImagem('dominio/baixar_pdf')
                self.dominio.AguardarImagem('dominio/aguardar_janela_baixar_pdf')
                pyautogui.write(str(empresa_id))
                pyautogui.press('tab', 2)
                pyautogui.press('enter')
                self.dominio.AguardarImagem('dominio/adobe')
                pyautogui.press('esc', 3)
                time.sleep(5)
                pyautogui.press('esc', 3)
                self.dominio.AlterarValorJson(empresa_id, 'status', 'concluido')
