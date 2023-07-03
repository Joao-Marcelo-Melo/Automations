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

    def IniciarDominio(self):
        self.dominio.LogarDominio(self.email_dominio, self.senha_dominio)
        self.dominio.LogarModulo(self.usuario_modulo, self.senha_modulo, 'folha')

    def ExecutarTarefasFolha(self):
        caminho_empresas = "src\empresas.json"
        with open(caminho_empresas, encoding='utf-8') as arquivo:
            empresas = json.load(arquivo)

        for empresa in empresas:
            empresa_id = empresa['id']
            self.folha.trocar_empresa(empresa_id)
            self.folha.entrar_aviso_de_vencimento()
            self.folha.definir_configuracoes()
            self.folha.baixar_pdf(empresa_id)