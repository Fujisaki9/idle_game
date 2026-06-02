from rich.align import Align
from rich.console import Console
from rich.table import Table


def mostrar_inventario(inventario: dict):
    """
    Exibe em uma tabela os materiais coletados, a quantidade obtida e o valor total em ouro.
    :param inventario: Dicionário que contém os objetos da classe Inventário.
    :return: None
    """
    console = Console()
    table = Table(style = 'yellow', width = 90)
    table.add_column("ITENS", justify = 'center')
    table.add_column("QUANTIDADE", justify = 'center')
    table.add_column("PREÇO UNITÁRIO", justify = 'center')
    table.add_column("PREÇO TOTAL", justify='center')
    for item in inventario.values():
        table.add_row(Align.left(item.nome_item),
                      str(item.quantidade_item),
                      str(item.preco_unitario),
                      str(item.calcular_preco(item.quantidade_item)))

    console.print(table)


def mostrar_itens_inventario(inventario):
    """
    Exibe os materiais coletados e seus respectivos indices em uma tabela.
    :param inventario: Dicionário que contém os objetos da classe Inventário.
    :return: None
    """
    console = Console()
    table = Table(style = 'yellow', width = 90)
    table.add_column("ITENS", justify = 'center')
    table.add_column("QUANTIDADE", justify = 'center')
    table.add_column("PREÇO UNITÁRIO", justify='center')
    table.add_column("PREÇO TOTAL", justify = 'center')

    for indice, item in enumerate(inventario.values(), 1):
        table.add_row(Align.left(f"[{indice}] {item.nome_item}"),
                      str(item.quantidade_item),
                      str(item.preco_unitario),
                      str(item.calcular_preco(item.quantidade_item)))
    table.add_section()
    table.add_row(Align.left(f"[bold #FF8C00][{len(inventario) + 1}] VOLTAR[/]"), "-", "-", "-")
    console.print(table)

