from rich.align import Align
from rich.console import Console
from rich.table import Table

from base.material import MaterialRequerido
from forja.database import escolher_recipe_forja
from inventario.classe import Inventario
from utilitario.formatacao import formatar_texto


def exibir_menu_forja():
    console = Console()

    menu_forja = Table(style='yellow', width=40)
    menu_forja.add_column("RECIPES", justify='center')

    menu_forja.add_row(Align.left("[bold][1] Armas[/]"))
    menu_forja.add_row(Align.left("[bold][2] Armaduras[/]"))
    menu_forja.add_row(Align.left("[bold][3] Acessórios[/]"))

    menu_forja.add_section()
    menu_forja.add_row(Align.left("[bold #FF8C00][4] Sair da Forja[/]"))

    console.print(menu_forja)


def exibir_menu_recipes(indice_escolhido: int):
    console = Console()
    recipes = escolher_recipe_forja(indice_escolhido)

    menu_recipes = Table(style='yellow', width=50)
    menu_recipes.add_column(recipes["titulo"], justify='center')

    for indice_recipe in recipes:
        if indice_recipe != "titulo":
            nome_recipe_formatado = formatar_texto(recipes[indice_recipe]["nome"])
            menu_recipes.add_row(Align.left(f"[{indice_recipe}] {nome_recipe_formatado}"))

    menu_recipes.add_section()
    menu_recipes.add_row(Align.left(f"[bold #FF8C00][{len(recipes)}] Voltar[/]"))

    console.print(menu_recipes)


def exibir_materiais_recipe(recipe_escolhido: dict[int, MaterialRequerido],
                            inventario: dict[str, Inventario]):

    console = Console()

    materiais_recipe = Table(style='yellow', width=80)
    materiais_recipe.add_column("ITENS", justify='center')
    materiais_recipe.add_column("MATERIAIS", justify='center')
    materiais_recipe.add_column("ZONA", justify='center')

    for material in recipe_escolhido["materiais"]:
        nome_material_formatado = formatar_texto(material.nome_material)
        item_inventario = inventario.get(nome_material_formatado, None)
        zona_obtencao_formatada = formatar_texto(material.zona_obtencao)

        quantidade_possuida = item_inventario.quantidade_item if item_inventario else 0

        unidades = f"{quantidade_possuida}/{material.quantidade_exigida}"

        materiais_recipe.add_row(Align.left(nome_material_formatado),
                                 unidades,
                                 Align.left(zona_obtencao_formatada))

    console.print(materiais_recipe)