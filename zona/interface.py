from rich.console import Console
from rich.align import Align
from rich.table import Table

from zona.classe import Zona

def exibir_menu_zonas():
    console = Console()

    menu_zonas = Table(style='yellow', width=40)
    menu_zonas.add_column("MENU", justify='center')

    menu_zonas.add_row(Align.left("[1] Acessar a próxima zona"))
    menu_zonas.add_row(Align.left("[2] Entrar no modo repetição"))
    menu_zonas.add_row(Align.left("[3] Acessar o menu principal"))

    console.print(menu_zonas)


def exibir_tabela_zonas(zonas: list[Zona]):
    console = Console()

    tabela_zonas = Table(style = 'yellow')
    tabela_zonas.add_column("ZONAS", justify='center')
    tabela_zonas.add_column("NV. MÍNIMO", justify='center')
    tabela_zonas.add_column("STATUS", justify='center')

    for indice_zona, zona in enumerate(zonas, 1):

        if zona.zona_concluida:
            status = "[bold green]Completo[/]"
        else:
            status = "[bold red]Bloqueado[/]"
        tabela_zonas.add_row(Align.left(f"[{indice_zona}] {zona.nome_zona}"), str(zona.nivel_minimo), status)

    tabela_zonas.add_section()
    tabela_zonas.add_row(Align.left(f"[bold #FF8C00][{len(zonas) + 1}] VOLTAR[/]"), "-", "-")

    console.print(tabela_zonas)


def exibir_opcoes_repeticao():
    console = Console()

    menu_repeticoes = Table(style='yellow')
    menu_repeticoes.add_column("MENU DE OPÇÕES", justify='center')

    menu_repeticoes.add_row(Align.left("[1] 5 Repetições"))
    menu_repeticoes.add_row(Align.left("[2] 10 Repetições"))
    menu_repeticoes.add_row(Align.left("[3] Escolher quantidade"))

    menu_repeticoes.add_section()
    menu_repeticoes.add_row(Align.left("[bold #FF8C00][4] VOLTAR[/]"))

    console.print(menu_repeticoes)
