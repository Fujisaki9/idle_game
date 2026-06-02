from time import sleep

from rich import print as rprint
from rich.console import Console

from codex.ui import mostrar_codex, mostrar_colecao_codex, mostrar_indice_codex
from utils.console import limpar_console
from utils.formatters import formatar_strings
from utils.validators import validar_integer, validar_pergunta


def acessar_codex(codex, inventario, heroi):
    """
    Orquestra o fluxo de interação com o Codex, delegando a lógica para funções específicas.
    :param codex: Lista de objetos da classe Codex.
    :param inventario: Dicionário que contém os objetos da classe Inventário.
    :param heroi: Objeto heroi -> classe Heroi.
    :return: None
    """
    console = Console()

    while True:
        abrir_codex = validar_escolha_codex(codex)
        if abrir_codex:
            while True:
                indice_colecao = escolher_colecao_codex(codex)# segunda
                if indice_colecao:
                    while True:
                        indice_material = escolher_material_colecao(codex, indice_colecao, inventario)
                        if indice_material:
                            dados_material = escolher_quantidade_material(codex, indice_colecao, inventario,
                                                                                   indice_material)
                            if dados_material:
                                nome_item, quantidade_item, inserir_material = dados_material
                                rprint("[bold #FF8C00]Material inserido com sucesso![/]")
                                sleep(1)
                                (codex[indice_colecao - 1].requisitos[indice_material - 1].subtrair_materiais
                                (inserir_material))
                                quantidade_material = (codex[indice_colecao - 1].requisitos[indice_material - 1].
                                                       quantidade)
                                if quantidade_material == 0:
                                    codex[indice_colecao - 1].requisitos[indice_material - 1].obter()
                                    if all(item.obtido for item in codex[indice_colecao - 1].requisitos):
                                        codex[indice_colecao - 1].concluir()
                                        rprint(f"[bold #FF8C00]A coleção "
                                               f"{formatar_strings(codex[indice_colecao - 1].nome_colecao)} "
                                               f"foi concluída![/]")
                                        heroi.aplicar_recompensas(codex[indice_colecao - 1].recompensa_colecao)
                                inventario[nome_item].subtrair_quantidade(inserir_material)
                                quantidade_item = inventario[nome_item].quantidade_item
                                if quantidade_item == 0:
                                    del inventario[nome_item]
                        else:
                            break
                else:
                    break
        else:
            break

    console.input("[bold #FF8C00]Pressione ENTER para voltar ao menu principal.[/]")
    limpar_console()


def validar_escolha_codex(codex) -> bool:
    """
    Valida o input do usuário retornando um valor booleano.
    :param codex: Lista que contem os objetos da classe Codex.
    :return: True se o usuário desejar acessar o Codex, False caso contrário.
    """
    limpar_console()
    mostrar_codex(codex)
    pergunta = validar_pergunta("Deseja acessar alguma coleção no Codex? [S/N]: ")
    if pergunta == 'S':
        return True
    return False


def escolher_colecao_codex(codex) -> int | bool:
    """
    Valida o input do usuário retornando um valor inteiro/booleano.
    :param codex: Lista de objetos da classe Codex.
    :return: Índice da coleção escolhida (int) ou False caso o usuário deseje retornar.
    """
    while True:
        limpar_console()
        mostrar_indice_codex(codex)
        indice = validar_integer("Escolha uma coleção: ")
        if indice <= len(codex):
            if not codex[indice - 1].conclusao:
                return indice
            else:
                rprint(f"[bold #FF8C00]A coleção {formatar_strings(codex[indice - 1].nome_colecao)} "
                       f"já foi concluída.[/]")
                sleep(1)
        elif indice == len(codex) + 1:
            return False
        else:
            rprint("[bold red]Insira um comando válido![/]")
            sleep(1)


def escolher_material_colecao(codex, indice_colecao, inventario) -> int | bool:
    """
    Valida o input do usuário retornando um valor inteiro/booleano.
    :param codex: Lista de objetos da classe Codex.
    :param indice_colecao: Índice da coleção escolhida.
    :param inventario: Dicionário que contém as objetos da classe Inventário.
    :return: Indice do material escolhido(int) dentro da coleção escolhida ou False caso o usuário deseje retornar.
    """
    while True:
        limpar_console()
        mostrar_colecao_codex(codex, indice_colecao, inventario)
        material = validar_integer("Escolha o material: ")
        if (material <= len(codex[indice_colecao - 1].requisitos) and
                codex[indice_colecao - 1].requisitos[material - 1].obtido == False):
            return material
        elif material == len(codex[indice_colecao - 1].requisitos) + 1:
            return False
        else:
            if material > len(codex[indice_colecao - 1].requisitos):
                rprint("[bold red]Insira um comando válido![/]")
                sleep(1)
            else:
                rprint("[bold #FF8C00]Material já cadastrado![/]")
                sleep(1)


def escolher_quantidade_material(codex, indice_colecao, inventario, indice_material) -> tuple | bool:
    """
    Verifica se o usuário possui o material no inventário.
    :param codex: Lista de objetos da classe Codex.
    :param indice_colecao: Índice da coleção escolhida.
    :param inventario: Dicionário que contém os objetos da classe Inventário.
    :param indice_material: Índice do material dentro da lista de requisitos da coleção escolhida.
    :return: Tupla (nome_item, quantidade_item, inserir_material) ou False caso o material não exista no inventário.
    """
    nome_item = formatar_strings(codex[indice_colecao - 1].requisitos[indice_material - 1].nome_material)
    if nome_item not in inventario:
        rprint("[bold red]Você não possui esse material![/]")
        sleep(1)
        return False
    else:
        quantidade_item = inventario[nome_item].quantidade_item
        inserir_material = validar_integer("Quantidade: ")
        inserir_material = min(inserir_material, codex[indice_colecao - 1].requisitos[indice_material - 1].quantidade)
        return nome_item, quantidade_item, inserir_material