import os


def limpar_console():
    """
    Limpa o console de acordo com o sistema operacional.
    :return: None
    """
    if os.name == 'nt':
        comando = 'cls'
    else:
        comando = 'clear'
    os.system(comando)