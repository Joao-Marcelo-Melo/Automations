from source import *

debug_mode = os.getenv('DEBUG')


if debug_mode == "TRUE":
    AppTest()
else:
    App()