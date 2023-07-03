from .modules.DominioAutomator import *
from .modules.Folha import *
from setup import *

class App():
    def __init__(self):
        self.email_dominio = os.getenv('EMAIL_DOMINIO')
        self.senha_dominio = os.getenv('SENHA_DOMINIO')
        self.usuario_modulo = os.getenv('USUARIO_MODULO')
        self.senha_modulo = os.getenv('SENHA_MODULO')

        self.dominio = DominioAutomator()
        self.folha = Folha()

    def iniciar_dominio(self):
        self.dominio.LogarDominio(self.email_dominio, self.senha_dominio)
        self.dominio.LogarModulo(self.usuario_modulo, self.senha_modulo, 'folha')

    def executar_tarefas_folha(self):
        empresas = self.dominio.carregar_json()
        primeira_interacao = True

        for empresa in empresas:
            if empresa['status'] == 'pendente':
                empresa_id = empresa['id']
                self.folha.trocar_empresa(empresa_id)
                self.folha.entrar_aviso_de_vencimento()
                self.folha.definir_configuracoes()
                self.folha.salvar_pdf(empresa_id, primeira_interacao)
                primeira_interacao = False