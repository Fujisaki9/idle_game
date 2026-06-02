from random import random
from time import sleep

from rich import print as rprint
from rich.console import Console

from inventory.models import Inventario
from inventory.ui import mostrar_inventario, mostrar_itens_inventario
from utils.console import limpar_console
from utils.ui import mostrar_menu_principal
from utils.validators import validar_integer, validar_pergunta



def abrir_inventario(inventario, heroi):
    """
    Exibe o inventário do herói e oferece a opção de vender os itens coletados.
    :param inventario: Dicionário que contém os objetos da classe Inventário.
    :param heroi: Objeto heroi -> classe Heroi.
    :return: None
    """
    console = Console()
    while True:
        limpar_console()
        mostrar_menu_principal()
        mostrar_inventario(inventario)
        rprint(f"[bold cyan]OURO ATUAL: {heroi.ouro}[/]")
        vender_item = validar_pergunta("Deseja vender algum item? [S/N]: ")
        if vender_item == 'S':
            if not inventario:
                rprint("[bold red]Inventário vazio![/]")
                break
            else:
                vender_itens_inventario(heroi, inventario)
        else:
            break
    console.input("[bold #FF8C00]Pressione ENTER para voltar ao menu principal.[/]")
    limpar_console()


def vender_itens_inventario(heroi, inventario):
    """
    Permite que o usuário venda os materiais coletados em combate.
    :param heroi: Objeto heroi -> classe Heroi.
    :param inventario: Dicionário que contèm os objetos da classe Inventário.
    :return: None
    """
    while True:
        indice = escolher_indice_inventario(inventario)
        if indice:
            item = list(inventario.keys())[indice - 1]
            rprint(f"[bold cyan]Item: {inventario[item].nome_item} | Quantidade: {inventario[item].quantidade_item} | "
                   f"Preço: {inventario[item].preco_total}[/]")

            while True:
                quantidade, valor_total = escolher_quantidade_item(inventario, item)
                rprint(f"[bold cyan]Item: {inventario[item].nome_item} | Quantidade: {quantidade} | "
                       f"Preço: {valor_total}[/]")

                pergunta = validar_pergunta("Confirmar venda? [S/N]: ")
                if pergunta == 'S':
                    heroi.adicionar_ouro(valor_total)
                    inventario[item].subtrair_quantidade(quantidade)
                    inventario[item].subtrair_preco_total(valor_total)
                    rprint(f"[bold green]Item vendido com sucesso | Ouro Atual: {heroi.ouro}[/]")
                    sleep(1.5)

                    if inventario[item].quantidade_item == 0:
                        del inventario[item]

                    break
                else:
                    break
        else:
            break


def escolher_indice_inventario(inventario) -> int | bool:
    """
    Exibe os itens obtidos e valida o input do jogador.
    :param inventario: Dicionário que contém os objetos da classe Inventário.
    :return: Indice do item escolhido (int) ou False caso o usuário deseje sair do inventário.
    """

    while True:
        limpar_console()
        mostrar_menu_principal()
        mostrar_itens_inventario(inventario)

        indice = validar_integer("Digite o índice do item que deseja vender: ")
        if indice <= len(inventario):
            return indice
        elif indice == len(inventario) + 1:
            return False
        else:
            rprint("[bold red]Insira um comando válido![/]")
            sleep(1)


def escolher_quantidade_item(inventario, item) -> tuple:
    """
    Define a quantidade do material escolhido pelo usuário.
    :param inventario: Dicionário que contém os objetos da classe Inventário.
    :param item: Item escolhido pelo usuário.
    :return: Tupla (quantidade, valor_total) com a quantidade escolhida e o valor total da venda.
    """
    while True:
        quantidade = validar_integer("Quantas unidades deseja vender?: ")
        if quantidade <= inventario[item].quantidade_item:
            valor_total = inventario[item].calcular_preco(quantidade)
            return quantidade, valor_total
        else:
            rprint("[bold red]Quantidade insuficiente de materiais![/]")
            sleep(1)


def dropar_itens(inimigo, inventario):
    """
    Sorteia e adiciona os itens dropados pelo inimigo ao inventário do herói.
    :param inimigo: Objeto inimigo -> classe Inimigo.
    :param inventario: Dicionário que contém os objetos da classe Inventário.
    :return: None
    """
    for item in inimigo.drops:
        if random() <= item.chance_drop:
            rprint(f"[bold #FF8C00]Drop: {item.nome} x1.[/]")
            if item.nome in inventario:
                inventario[item.nome].adicionar_quantidade()
                inventario[item.nome].adicionar_preco_total(item.valor_item)
            else:
                inventario[item.nome] = Inventario(item.nome, 1, item.valor_item, item.valor_item)
    sleep(0.5)
