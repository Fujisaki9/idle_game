from rich.align import Align
from rich.console import Console
from rich.table import Table

from forge.database import criar_recipes_forja
from utils.formatters import formatar_strings



def mostrar_menu_forja():
    """
    Exibe o menu de equipamentos na forja.
    :return: None
    """
    console = Console()
    menu_forja = Table(style = 'yellow', width = 40)
    menu_forja.add_column("RECIPES", justify='center')
    menu_forja.add_row(Align.left("[bold][1] Armas[/]"))
    menu_forja.add_row(Align.left("[bold][2] Armaduras[/]"))
    menu_forja.add_row(Align.left("[bold][3] Acessórios[/]"))
    menu_forja.add_section()
    menu_forja.add_row(Align.left("[bold #FF8C00][4] Sair da Forja[/]"))
    console.print(menu_forja)


def mostrar_menu_recipes(indice):
    """
    Exibe o menu de recipes do equipamento escolhido pelo usuário.
    :param indice: Índice do equipamento escolhido (1 = Arma, 2 = Armadura, 3 = Acessório).
    :return: None
    """
    console = Console()
    recipes = criar_recipes_forja(indice)

    menu_recipes = Table(style = 'yellow', width = 50)
    menu_recipes.add_column(recipes["titulo"], justify = 'center')

    for indice_recipe in recipes:
        if indice_recipe != "titulo":
            nome_formatado = formatar_strings(recipes[indice_recipe]["nome"])
            menu_recipes.add_row(Align.left(f"[{indice_recipe}] {nome_formatado}"))

    menu_recipes.add_section()
    menu_recipes.add_row(Align.left(f"[bold #FF8C00][{len(recipes)}] Voltar[/]"))
    console.print(menu_recipes)


def mostrar_materiais_recipe(recipe, inventario):
    """
    Exibe uma tabela com os materiais necessários para completar o recipe.
    :param recipe: Índice do recipe escolhido.
    :param inventario: Dicionario que contém os objetos da classe Inventário.
    :return: None.
    """
    console = Console()
    materiais_recipe = Table(style = 'yellow', width = 80)
    materiais_recipe.add_column("ITENS", justify='center')
    materiais_recipe.add_column("MATERIAIS", justify='center')
    materiais_recipe.add_column("ZONA", justify='center')

    for material in recipe["materiais"]:
        nome_formatado = formatar_strings(material.nome_material)
        quantidade_atual = inventario.get(nome_formatado, None)
        zona_formatada = formatar_strings(material.zona_obtencao)

        if quantidade_atual:
            contador = f"{quantidade_atual.quantidade_item}/{material.quantidade}"
        else:
            contador = f"0/{material.quantidade}"

        materiais_recipe.add_row(Align.left(nome_formatado), contador, Align.left(zona_formatada))
    console.print(materiais_recipe)