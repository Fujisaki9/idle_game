from rich.console import Console
from rich.align import Align
from rich.table import Table


def mostrar_menu_zona():
    """
    Exibe o menu de opções com todas as opções disponíveis para o jogador.
    :return: None
    """
    console = Console()
    table = Table(style = 'yellow', width = 40)
    table.add_column("MENU", justify = 'center')
    table.add_row(Align.left("[1] Acessar a próxima zona"))
    table.add_row(Align.left("[2] Entrar no modo repetição"))
    table.add_row(Align.left("[3] Acessar o menu principal"))
    console.print(table)


def mostrar_tabela_zonas(zonas):
    """
    Exibe todas as zonas disponíveis e o status de conclusão.
    :param zonas: Lista de objetos da classe Zona.
    :return: None
    """
    console = Console()
    table = Table(style = 'yellow')
    table.add_column("ZONAS", justify = 'center')
    table.add_column("NV. MÍNIMO", justify = 'center')
    table.add_column("STATUS", justify = 'center')

    for indice, zona in enumerate(zonas, 1):
        if zona.zona_concluida:
            status = "[bold green]Completo[/]"
        else:
            status = "[bold red]Bloqueado[/]"
        table.add_row(Align.left(f"[{indice}] {zona.nome_zona}"), str(zona.nivel_minimo), status)
    table.add_section()
    table.add_row(Align.left(f"[bold #FF8C00][{len(zonas) + 1}] VOLTAR[/]"), "-", "-")

    console.print(table)


def mostrar_opcoes_repeticao():
    """
    Exibe o menu de seleção de repetições para a zona escolhida.
    Opções: 5, 10 ou quantidade personalizada.
    :return: None
    """
    console = Console()
    table = Table(style = 'yellow')
    table.add_column("MENU DE OPÇÕES", justify = 'center')
    table.add_row(Align.left("[1] 5 Repetições"))
    table.add_row(Align.left("[2] 10 Repetições"))
    table.add_row(Align.left("[3] Escolher quantidade"))
    table.add_section()
    table.add_row(Align.left("[bold #FF8C00][4] VOLTAR[/]"))
    console.print(table)
