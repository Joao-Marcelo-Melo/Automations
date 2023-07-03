from setup import *

logging.basicConfig(level=logging.ERROR, format='%(asctime)s [%(levelname)s]: %(message)s')

def handle_exception(exception):
    logging.exception("Ocorreu uma exceção: %s", str(exception))

debug_mode = os.getenv('DEBUG')

if debug_mode == "FALSE": 
    try:
        App().iniciar_dominio()
        App().executar_tarefas_folha()
    except Exception as e:
        handle_exception(e)
else:
    try:
        AppTest().iniciar_dominio()
        AppTest().executar_tarefas_folha()
    except Exception as e:
        handle_exception(e)