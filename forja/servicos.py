from time import sleep

from rich import print as rprint
from rich.console import Console

from forja.database import escolher_recipe_forja
from forja.interface import exibir_materiais_recipe, exibir_menu_forja, exibir_menu_recipes
from heroi.classe import Heroi
from inventario.classe import Inventario
from utilitario.console import limpar_console
from utilitario.formatadores import formatar_texto
from utilitario.interface import exibir_menu_principal
from utilitario.validadores import validar_inteiro, validar_confirmacao


def forjar_equipamentos(heroi: Heroi,
                        inventario: dict[str, Inventario]):
    """
    Gerencia o fluxo de forja de equipamentos usando materiais do inventário.

    Exibe os requisitos do recipe selecionado, valida a disponibilidade dos materiais, subtrai os itens consumidos do
    inventário e atualiza as propriedades do equipamento do herói.
    :return: None
    """
    console = Console()
    equipamentos_heroi = {1: heroi.arma, 2: heroi.armadura, 3: heroi.acessorio}
    indice_equipamento, indice_recipe, recipe_escolhido, = exibir_equipamentos_forja(heroi, inventario)

    if indice_recipe:
        # 1. Checa a quantidade no inventário e exibe o status de cada item
        for item in recipe_escolhido['materiais']:
            nome_item_formatado = formatar_texto(item.nome_material)
            nome_zona_formatado = formatar_texto(item.zona_obtencao)

            if nome_item_formatado in inventario:
                quantidade_item_inventario = inventario[nome_item_formatado].quantidade_item

                if quantidade_item_inventario >= item.quantidade_exigida:
                    item.coleta_concluida()
                    rprint(f"[bold green][{quantidade_item_inventario}/{item.quantidade_exigida}] " 
                           f"{nome_item_formatado} | Zona: {nome_zona_formatado}[/]")
                else:
                    rprint(f"[bold red][{quantidade_item_inventario}/{item.quantidade_exigida}] "  
                           f"{nome_item_formatado} | Zona: {nome_zona_formatado}[/]")

            else:
                rprint(f"[bold red]Você não possui {nome_item_formatado} | Zona: {nome_zona_formatado}[/]")

        # 2. Valida se TODOS os materiais têm material_obtido == True
        forjar_equipamento = True
        for material in recipe_escolhido['materiais']:
            if not material.material_obtido:
                forjar_equipamento = False
                break

        # 3. Processa a forja ou avisa que faltam materiais
        if forjar_equipamento:
            for item_recipe in recipe_escolhido['materiais']:
                nome_item_formatado = formatar_texto(item_recipe.nome_material)
                item_escolhido = inventario[nome_item_formatado]

                item_escolhido.subtrair_quantidade(item_recipe.quantidade_exigida)
                if item_escolhido.quantidade_item <= 0:
                    del inventario[nome_item_formatado]

            item_completo = equipamentos_heroi[indice_equipamento]
            item_completo.raridade = recipe_escolhido['raridade']
            item_completo.nivel_maximo = recipe_escolhido['nivel_maximo']
            item_completo.nome_equipamento = recipe_escolhido['nome']

            rprint(f"[bold cyan]Materiais prontos para a forja![/]")
            sleep(1.5)
            rprint(f"[bold cyan]:hammer: Forjando o item...[/]")
            sleep(1.5)
            rprint(f"[bold green]:sparkles:  O item {item_completo.nome_equipamento.upper()} foi forjado com sucesso![/]")
            sleep(1)
            console.input("[bold #FF8C00]Pressione ENTER para voltar ao menu principal.[/]")
        else:
            rprint("[bold #FF8C00]Materiais insuficientes para craftar![/]")
            console.input("[bold #FF8C00]Pressione ENTER para voltar ao menu principal.[/]")

    rprint("[bold #FF8C00]Saindo da Forja...[/]")
    sleep(1)
    limpar_console()


def exibir_equipamentos_forja(heroi: Heroi,
                              inventario: dict[str, Inventario]) -> tuple[int, int, dict] | tuple[bool, bool, None]:
    """
    Exibe o menu de equipamentos e seus respectivos recipes para seleção do jogador.

    :return: Tupla (indice_equipamento, indice_recipe, recipe_escolhido) se selecionado,
             ou (False, False, None) caso o jogador cancele a seleção.
    """
    equipamentos_heroi = {1: heroi.arma, 2: heroi.armadura, 3: heroi.acessorio}
    ordem_raridade = {"comum": 0, "epico": 1, "unico": 2, "lendario": 3}

    while True:
        indice_equipamento = escolher_indice_equipamento()
        if not indice_equipamento:
            break

        while True:
            indice_recipe = escolher_indice_recipe(indice_equipamento)
            if not indice_recipe:
                break

            recipes_equipamento_escolhido = escolher_recipe_forja(indice_equipamento)
            recipe_escolhido = recipes_equipamento_escolhido[indice_recipe]

            exibir_materiais_recipe(recipe_escolhido, inventario)

            equipamento_atual = equipamentos_heroi[indice_equipamento]
            raridade_exigida = recipe_escolhido["raridade_necessaria"]
            indice_raridade = recipe_escolhido["indice_raridade"]

            confirmacao_craft = validar_confirmacao("Deseja craftar esse item? [S/N]: ")
            if confirmacao_craft == 'S':

                if equipamento_atual.raridade == raridade_exigida:
                    return indice_equipamento, indice_recipe, recipe_escolhido

                elif ordem_raridade[equipamento_atual.raridade] > indice_raridade:
                    rprint("[bold red]Você já possui este item ou uma versão superior![/]")
                    sleep(1.5)

                else:
                    rprint(f"[bold red]Você precisa ter o item de raridade anterior para craftar este![/]")
                    sleep(1.5)

    return False, False, None


def escolher_indice_equipamento() -> int | bool:
    while True:
        limpar_console()
        exibir_menu_principal()
        exibir_menu_forja()

        indice_equipamento = validar_indice_escolhido("Escolha um equipamento: ")
        return indice_equipamento


def escolher_indice_recipe(indice_equipamento: int) -> int | bool:
    while True:
        limpar_console()
        exibir_menu_principal()
        exibir_menu_recipes(indice_equipamento)

        indice_recipe = validar_indice_escolhido("Escolha um Recipe: ")
        return indice_recipe


def validar_indice_escolhido(mensagem: str) -> int | bool:
    while True:
        indice_escolhido = validar_inteiro(mensagem)

        if indice_escolhido in (1, 2, 3):
            return indice_escolhido
        elif indice_escolhido == 4:
            return False
        else:
            rprint("[bold red]Insira um comando válido![/]")