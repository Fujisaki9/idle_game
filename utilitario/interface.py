from rich.align import Align
from rich.console import Console
from rich.table import Table


def exibir_menu_principal():
    console = Console()

    menu_principal = Table(style='yellow', width=30)
    menu_principal.add_column("MENU PRINCIPAL", justify='center')

    menu_principal.add_row(Align.left("[1] Mostrar Atributos"))
    menu_principal.add_row(Align.left("[2] Aprimorar Equipamentos"))
    menu_principal.add_row(Align.left("[3] Forja"))
    menu_principal.add_row(Align.left("[4] Abrir Inventário"))
    menu_principal.add_row(Align.left("[5] Abrir Codex"))
    menu_principal.add_row(Align.left("[6] Escolher zona"))
    menu_principal.add_row(Align.left("[7] Continuar"))
    menu_principal.add_row(Align.left("[8] Sair do jogo"))

    console.print(menu_principal)
