from rich.align import Align
from rich.console import Console
from rich.table import Table

from inventario.classe import Inventario


def exibir_inventario(inventario: dict[str, Inventario]):
    console = Console()

    table = Table(style = 'yellow', width = 90)
    table.add_column("ITENS", justify = 'center')
    table.add_column("QUANTIDADE", justify = 'center')
    table.add_column("PREÇO UNITÁRIO", justify = 'center')
    table.add_column("PREÇO TOTAL", justify='center')

    for item in inventario.values():
        table.add_row(Align.left(item.nome_item_inventario),
                      str(item.quantidade_item),
                      str(item.preco_unitario),
                      str(item.calcular_preco(item.quantidade_item)))

    console.print(table)


def exibir_itens_inventario(inventario: dict[str, Inventario]):
    console = Console()

    itens_inventario = Table(style='yellow', width=90)
    itens_inventario.add_column("ITENS", justify='center')
    itens_inventario.add_column("QUANTIDADE", justify='center')
    itens_inventario.add_column("PREÇO UNITÁRIO", justify='center')
    itens_inventario.add_column("PREÇO TOTAL", justify='center')

    for indice_item, item in enumerate(inventario.values(), 1):
        itens_inventario.add_row(Align.left(f"[{indice_item}] {item.nome_item_inventario}"),
                      str(item.quantidade_item),
                      str(item.preco_unitario),
                      str(item.calcular_preco(item.quantidade_item)))

    itens_inventario.add_section()
    itens_inventario.add_row(Align.left(f"[bold #FF8C00][{len(inventario) + 1}] VOLTAR[/]"), "-", "-", "-")

    console.print(itens_inventario)