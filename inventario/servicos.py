from random import random
from time import sleep

from rich import print as rprint
from rich.console import Console

from base.inimigo import Inimigo
from heroi.classe import Heroi
from inventario.classe import Inventario
from inventario.interface import exibir_inventario, exibir_itens_inventario
from utilitario.console import limpar_console
from utilitario.interface import exibir_menu_principal
from utilitario.validacao import validar_inteiro, validar_confirmacao


def abrir_inventario(inventario: dict[str, Inventario],
                     heroi: Heroi):

    console = Console()

    while True:
        limpar_console()
        exibir_menu_principal()
        exibir_inventario(inventario)

        rprint(f"[bold cyan]OURO ATUAL: {heroi.ouro}[/]")
        vender_item = validar_confirmacao("Deseja vender algum item? [S/N]: ")

        if vender_item == 'S':
            if not inventario:
                rprint("[bold red]Inventário vazio![/]")
                break
            vender_itens_inventario(inventario, heroi)

        else:
            break

    console.input("[bold #FF8C00]Pressione ENTER para voltar ao menu principal.[/]")
    limpar_console()


def vender_itens_inventario(inventario: dict[str, Inventario],
                            heroi: Heroi):

    while True:
        indice_escolhido = escolher_indice_item(inventario)
        if not indice_escolhido:
            break

        item = list(inventario.keys())[indice_escolhido - 1]

        item_escolhido = inventario[item].nome_item_inventario
        quantidade_item_escolhido = inventario[item].quantidade_item

        rprint(f"[bold cyan]Item: {item_escolhido} | Quantidade: {quantidade_item_escolhido} | "
               f"Preço: {inventario[item].preco_total}[/]")

        while True:
            quantidade_escolhida, preco_total = obter_quantidade_venda(inventario, item)
            rprint(f"[bold cyan]Item: {item_escolhido} | Quantidade: {quantidade_escolhida} | "
                   f"Preço: {preco_total}[/]")

            confirmar_venda = validar_confirmacao("Confirmar venda? [S/N]: ")

            if confirmar_venda == 'S':
                heroi.adicionar_ouro(preco_total)
                inventario[item].subtrair_quantidade(quantidade_escolhida)
                inventario[item].subtrair_preco_total(preco_total)
                rprint(f"[bold green]Item vendido com sucesso | Ouro Atual: {heroi.ouro}[/]")
                sleep(1.5)

                if inventario[item].quantidade_item == 0:
                    del inventario[item]
            break

def escolher_indice_item(inventario: dict[str, Inventario]) -> int | bool:
    while True:
        limpar_console()
        exibir_menu_principal()
        exibir_itens_inventario(inventario)

        indice_escolhido = validar_inteiro("Digite o índice do item que deseja vender: ")

        opcao_valida = indice_escolhido <= len(inventario)
        opcao_saida = indice_escolhido == len(inventario) + 1

        if opcao_valida:
            return indice_escolhido

        elif opcao_saida:
            return False

        else:
            rprint("[bold red]Insira um comando válido![/]")
            sleep(1)


def obter_quantidade_venda(inventario: dict[str, Inventario],
                           item: str) -> tuple:
    while True:
        quantidade_escolhida = validar_inteiro("Quantas unidades deseja vender?: ")

        if quantidade_escolhida <= inventario[item].quantidade_item:
            preco_total = inventario[item].calcular_preco(quantidade_escolhida)
            return quantidade_escolhida, preco_total
        else:
            rprint("[bold red]Quantidade insuficiente de materiais![/]")
            sleep(1)


def coletar_drops(inimigo: Inimigo,
                  inventario: dict[str, Inventario]):

    for item in inimigo.drops:

        if random() <= item.chance_drop:
            rprint(f"[bold #FF8C00]Drop: {item.nome_item} x1.[/]")

            if item.nome_item in inventario:
                nome_item_coletado = inventario[item.nome_item]
                nome_item_coletado.adicionar_quantidade()
                nome_item_coletado.adicionar_preco_total(item.valor_item)

            else:
                inventario[item.nome_item] = Inventario(item.nome_item,
                                                             1,
                                                              item.valor_item,
                                                              item.valor_item)
    sleep(0.5)
