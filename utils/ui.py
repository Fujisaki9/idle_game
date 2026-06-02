from rich.align import Align
from rich.console import Console
from rich.table import Table


def mostrar_menu_principal():
    """
    Exibe o menu principal com todas as opções disponíveis para o jogador.
    :return: None
    """
    table = Table(style = 'yellow', width = 30)
    table.add_column("MENU PRINCIPAL", justify = 'center')
    table.add_row(Align.left("[1] Mostrar Atributos"))
    table.add_row(Align.left("[2] Aprimorar Equipamentos"))
    table.add_row(Align.left("[3] Forja"))
    table.add_row(Align.left("[4] Abrir Inventário"))
    table.add_row(Align.left("[5] Abrir Codex"))
    table.add_row(Align.left("[6] Escolher zona"))
    table.add_row(Align.left("[7] Continuar"))
    table.add_row(Align.left("[8] Sair do jogo"))
    console = Console()
    console.print(table)
