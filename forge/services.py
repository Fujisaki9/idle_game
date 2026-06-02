from time import sleep

from rich import print as rprint
from rich.console import Console

from forge.database import criar_recipes_forja
from forge.ui import mostrar_materiais_recipe, mostrar_menu_forja, mostrar_menu_recipes
from utils.console import limpar_console
from utils.formatters import formatar_strings
from utils.ui import mostrar_menu_principal
from utils.validators import validar_integer, validar_pergunta


def forjar_equipamentos(heroi, inventario):
    """
    Utiliza os materiais coletados nos combates para criar equipamentos avançados.
    :param heroi: Objeto heroi -> classe Heroi.
    :param inventario: Dicionário que contém os objetos da classe Inventário.
    :return: None
    """
    console = Console()
    equipamentos_heroi = {1: heroi.arma, 2: heroi.armadura, 3: heroi.acessorio}
    indice_equipamento, indice_recipes, recipe_escolhido, = mostrar_itens_forja(heroi, inventario)

    if indice_recipes:
        for item in recipe_escolhido['materiais']:

            nome_item = formatar_strings(item.nome_material)
            if nome_item in inventario:

                if inventario[nome_item].quantidade_item >= item.quantidade:
                    item.obter()
                    rprint(f"[bold green][{inventario[nome_item].quantidade_item}/{item.quantidade}] " 
                           f"{nome_item} | Zona: {formatar_strings(item.zona_obtencao)}[/]")
                else:
                    rprint(f"[bold red][{inventario[nome_item].quantidade_item}/{item.quantidade}] "  
                           f"{nome_item} | Zona: {formatar_strings(item.zona_obtencao)}[/]")

            else:
                rprint(f"[bold red]Você não possui {nome_item} |"       
                       f" Zona: {formatar_strings(item.zona_obtencao)}[/]")

        if all(material.obtido for material in recipe_escolhido['materiais']):
            for item in recipe_escolhido['materiais']:

                nome_item = formatar_strings(item.nome_material)

                inventario[nome_item].subtrair_quantidade(item.quantidade)
                if inventario[nome_item].quantidade_item <= 0:
                    del inventario[nome_item]

            item_completo = equipamentos_heroi[indice_equipamento]
            item_completo.raridade = recipe_escolhido['raridade']
            item_completo.nivel_max = recipe_escolhido['nivel_maximo']
            item_completo.nome_equip = recipe_escolhido['nome']

            rprint(f"[bold cyan]Materiais prontos para a forja![/]")
            sleep(1.5)
            rprint(f"[bold cyan]:hammer: Forjando o item...[/]")
            sleep(1.5)
            rprint(f"[bold green]:sparkles:  O item {item_completo.nome_equip.upper()} foi forjado com sucesso![/]")
            sleep(1)
            console.input("[bold #FF8C00]Pressione ENTER para voltar ao menu principal.[/]")
        else:
            rprint("[bold #FF8C00]Materiais insuficientes para craftar![/]")
            console.input("[bold #FF8C00]Pressione ENTER para voltar ao menu principal.[/]")

    rprint("[bold #FF8C00]Saindo da Forja...[/]")
    sleep(1)
    limpar_console()


def mostrar_itens_forja(heroi, inventario) -> tuple:
    """
    Exibe o menu de equipamentos e seus respectivos recipes.
    :param heroi: Objeto heroi -> classe Heroi
    :param inventario: Dicionário que contém os objetos da classe Inventário.
    :return: Tupla contendo o indice do equipamento, o dicionário do recipe e o índice da raridade escolhida.
    """
    equipamentos_heroi = {1: heroi.arma, 2: heroi.armadura, 3: heroi.acessorio}
    raridade_ordem = {"comum": 0, "epico": 1, "unico": 2, "lendario": 3}

    indice_recipe = None

    while True:
        indice_equipamento = escolher_equipamento_forja()
        if indice_equipamento:

            while True:
                indice_recipe = escolher_recipe_equipamento(indice_equipamento)
                if indice_recipe:

                    recipes_equipamento = criar_recipes_forja(indice_equipamento)
                    recipe_escolhido = recipes_equipamento[indice_recipe]

                    mostrar_materiais_recipe(recipe_escolhido, inventario)

                    equipamento_atual = equipamentos_heroi[indice_equipamento]
                    raridade_exigida = recipe_escolhido["raridade_necessaria"]
                    raridade_indice = recipe_escolhido["indice_raridade"]

                    craftar_item = validar_pergunta("Deseja craftar esse item? [S/N]: ")
                    if craftar_item == 'S':

                        if equipamento_atual.raridade == raridade_exigida:
                            return indice_equipamento, indice_recipe, recipe_escolhido

                        elif raridade_ordem[equipamento_atual.raridade] > raridade_indice:
                            rprint("[bold red]Você já possui este item ou uma versão superior![/]")
                            sleep(1.5)

                        else:
                            rprint(f"[bold red]Você precisa ter o item de raridade anterior para craftar este![/]")
                            sleep(1.5)
                else:
                    break
        else:
            break

    return indice_equipamento, None, None


def escolher_equipamento_forja() -> int | bool:
    """
    Exibe as opções de equipamento e valida a escolha do jogador.
    :return: Índice do equipamento escolhido (int) ou False caso o usuário deseje sair da Forja.
    """
    while True:
        limpar_console()
        mostrar_menu_principal()
        mostrar_menu_forja()
        indice_equipamento = validar_integer("Escolha uma opção: ")
        if indice_equipamento in (1, 2, 3):
            return indice_equipamento
        elif indice_equipamento == 4:
            sleep(0.5)
            return False
        else:
            rprint("[bold red]Insira um comando válido![/]")


def escolher_recipe_equipamento(indice_equipamento) -> int | bool:
    while True:
        limpar_console()
        mostrar_menu_principal()
        mostrar_menu_recipes(indice_equipamento)
        indice_recipe = validar_integer("Escolha um Recipe: ")
        if indice_recipe in (1, 2, 3):
            return indice_recipe
        elif indice_recipe == 4:
            return False
        else:
            rprint("[bold red]Insira um comando válido![/]")