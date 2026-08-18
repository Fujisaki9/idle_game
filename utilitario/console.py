import os


def limpar_console():
    if os.name == 'nt':
        comando = 'cls'
    else:
        comando = 'clear'
    os.system(comando)