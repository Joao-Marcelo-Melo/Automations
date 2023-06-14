from src.dominio import *
from src.Folha import *

dominio = DominioAutomator
folha = Folha()

# dominio.LogarDominio("pedro@nexxoempresarial.com", "An10203040*")
# dominio.LogarModulo("robofiscal", "int102030", "folha")

with open('src\empresas.json') as arquivo:
    empresas = json.load(arquivo)

for empresa in empresas:
    if empresa["Status"] == "Pendente":
        empresa_id = empresa["id"]              
        # folha.TrocarEmpresa(empresa_id)
        folha.AvisoDeVencimento()


# competencia = "042023"
# caminho_log = os.path.expanduser("~/Desktop/Empresas_Log.txt")
# caminho_empresas = "src\empresas.json"

# while True:
#     if dominio.LoginWeb("rafael@nexxoempresarial.com", "Nexxo123+"):
#         if dominio.LoginModulo("robofiscal", "int102030", "folha"):
#             sistema.AguardarImagem("Aviso_Vencimento")

#             with open(caminho_empresas) as arquivo:
#                 empresas = json.load(arquivo)

#             with open(caminho_log, "w") as arquivo:
#                 arquivo.write("")

#             for empresa in empresas:
#                 if empresa["Status"] == "Pendente":
#                     empresa_id = empresa["id"]
#                     etapas.TrocarEmpresa(empresa_id)
#                     etapas.CalculoFeriasDecimo(competencia, sistema)
#                     etapas.IntegracaoContabil(competencia, sistema)
#                     etapas.AguardarLogEmpresa(caminho_log, empresa_id, sistema, caminho_empresas)
#         else:
#             print("Erro ao logar no Domínio Módulo")
#     else:
#         print("Erro ao logar no Domínio Web")