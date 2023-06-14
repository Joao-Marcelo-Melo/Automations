import logging
from source import *

logging.basicConfig(filename='log.txt', level=logging.ERROR,format='%(asctime)s [%(levelname)s]: %(message)s')
debug_mode = os.getenv('DEBUG')

if debug_mode == "TRUE":
    try:
        AppTest()
    except Exception as e:
        logging.error("Ocorreu uma exceção: %s", str(e))
else:
    try:
        App()
    except Exception as e:
        logging.error("Ocorreu uma exceção: %s", str(e))