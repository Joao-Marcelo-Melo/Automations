import pyautogui
import time
from .sistema import *

class Folha(SistemaAutomator):
    def TrocarEmpresa(self, empresa_id):
        pyautogui.press('f8')
        time.sleep(2)
        pyautogui.write(str(empresa_id))
        time.sleep(4)
        pyautogui.press('enter')
        time.sleep(5)

    def AvisoDeVencimento(self):
        self.CliqueImagem('Relatorios')
        self.CliqueImagem('Outros')
        self.CliqueImagem('AvisodeVencimento')

        pyautogui.write('01072023')
        pyautogui.press('tab')
        pyautogui.write('30072023')
        # self.CliqueImagem('SelecionarEmpresas')
        # self.CliqueImagem('SelecionarTodasEmpresas')
        # self.CliqueImagem('ok')
        # self.CliqueImagem('GerarRelatoriosIndividualizados')
        self.CliqueImagem('ok')

        self.AguardarImagem('AguardarVencimento')
        self.CliqueImagem('baixarPDF')
        time.sleep(5)
        # self.AguardarImagem('SalvarPDF')
        print("achou")
        pyautogui.press('tab', 4)
        pyautogui.press('down', 2)
        pyautogui.press('enter')
        time.sleep(2)
        self.CliqueImagem('Users', 2)
        self.CliqueImagem('nexxo', 2)
        self.CliqueImagem('desktop', 2)
        self.CliqueImagem('envio', 2)
        time.sleep(3)
        self.CliqueImagem('save')
        time.sleep(10)


# def CalculoFeriasDecimo(competencia, sistema):
#     print('Calculando Ferias e Decimo Terceiro')
#     sistema.CliqueImagem('Processos')
#     time.sleep(2)
#     sistema.CliqueImagem('Ferias')
#     time.sleep(5)
#     pyautogui.write(competencia)
#     time.sleep(1)
#     pyautogui.press('tab')
#     pyautogui.write(competencia)
#     time.sleep(1)
#     pyautogui.press('tab', presses=3)
#     pyautogui.press('enter')
#     sistema.AguardarImagem('Aviso_Ferias')
#     time.sleep(5)
#     pyautogui.press('enter')
#     time.sleep(5)

# def IntegracaoContabil(competencia, sistema):
#     print('Executando a Integracao contabil')
#     sistema.CliqueImagem('Processos')
#     time.sleep(2)
#     sistema.CliqueImagem('Integracao')
#     time.sleep(7)
#     pyautogui.write(competencia)
#     pyautogui.press('tab', presses=2)
#     pyautogui.write(competencia)
#     time.sleep(1)
#     sistema.CliqueImagem('Exportar_Ferias')
#     sistema.CliqueImagem('Exportar_13')
#     pyautogui.press('tab', presses=5)
#     pyautogui.press('enter')


# def AguardarLogEmpresa(caminho_log, empresa_id, sistema, caminho_empresas):
#     print('Aguardando tela 'Integracao Final'')
#     if sistema.AguardarImagem('Integracao_Final', 30):
#         pyautogui.press('enter')

#         if sistema.AguardarImagem('Atencao', 5):
#             print('Aguardando tela 'Erro de Valor'')
#             pyautogui.press('enter')
#             pyautogui.press('esc', presses=4)
#             sistema.RegistraLog(str(empresa_id) + ' Erro de valor\n', caminho_log)
#             sistema.AlterarValorJson(caminho_empresas, empresa_id, 'ErroValor')

#         elif sistema.AguardarImagem('Gravado', 5):
#             print('Aguardando tela 'Integracao ja gravada'')
#             pyautogui.press('esc', presses=4)
#             sistema.RegistraLog(str(empresa_id) + ' Ja gravada\n', caminho_log)
#             sistema.AlterarValorJson(caminho_empresas, empresa_id, 'JaGravada')

#         elif sistema.AguardarImagem('Aviso_Final', 5):
#             print('Aguardando tela 'Integracao bem sucedida'')
#             pyautogui.press('{Enter}')
#             pyautogui.press('esc', presses=3)
#             sistema.RegistraLog(str(empresa_id) + ' Deu Certo\n', caminho_log)
#             sistema.AlterarValorJson(caminho_empresas, empresa_id, 'Concluida')

#         elif sistema.AguardarImagens('Rubricas', 5):
#             print('Aguardando tela 'Erro de Rubricas'')
#             pyautogui.press('esc', presses=4)
#             sistema.RegistraLog(str(empresa_id) + ' Erro Rubrica\n', caminho_log)
#             sistema.AlterarValorJson(caminho_empresas, empresa_id, 'Rubrica')

#         elif sistema.AguardarImagens('Aviso_Integracao', 5):
#             pyautogui.press('esc', presses=4)
#             sistema.RegistraLog(str(empresa_id) + ' Aviso\n', caminho_log)
#             sistema.AlterarValorJson(caminho_empresas, empresa_id, 'Aviso')

#         elif sistema.AguardarImagens('Lancamentos_Nao_lancados', 5):
#             pyautogui.press('esc', presses=4)
#             sistema.RegistraLog(str(empresa_id) + ' Lancamentos_nao_gravados\n', caminho_log)
#             sistema.AlterarValorJson(caminho_empresas, empresa_id, 'Lancamentos_nao_gravados')

#     elif sistema.AguardarImagem('Rubrica1', 30):
#         pyautogui.press('esc', presses=3)
#         sistema.RegistraLog(str(empresa_id) + ' Erro Rubrica\n', caminho_log)
#         sistema.AlterarValorJson(caminho_empresas, empresa_id, 'Rubrica')