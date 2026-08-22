from time import sleep

from rich import print as rprint
from rich.console import Console

from codex.classe import Codex
from codex.interface import exibir_colecao_escolhida, exibir_status_colecoes, exibir_tabela_codex
from heroi.classe import Heroi
from inventario.classe import Inventario
from utilitario.console import limpar_console
from utilitario.formatacao import formatar_texto
from utilitario.validacao import validar_confirmacao, validar_inteiro


def acessar_codex(colecoes: list[Codex],
                  inventario: dict[str, Inventario],
                  heroi: Heroi):
    """
    Orquestra o fluxo completo do Codex (menus, validações e entregas).

    Gerencia a navegação entre as coleções, a seleção e validação de materiais do inventário
    e o registro das entregas, aplicando os bônus diretamente ao herói quando uma coleção
    é concluída.

    :param colecoes: Lista com todas as coleções do Codex.
    :param inventario: Dicionário contendo os itens disponíveis do jogador.
    :param heroi: Instância do herói que receberá as atualizações e bônus.
    """
    console = Console()

    while True:
        abrir_codex = confirmar_acesso_codex(colecoes)
        if not abrir_codex:
            break

        while True:
            indice_colecao = escolher_indice_colecao(colecoes)
            if not indice_colecao:
                break

            while True:
                indice_material = escolher_material_colecao(colecoes, indice_colecao)
                if not indice_material:
                    break

                dados_material = escolher_quantidade_material(colecoes, indice_colecao, inventario, indice_material)
                if not dados_material:
                    break

                nome_item_escolhido, quantidade_atual, quantidade_escolhida = dados_material

                colecao_escolhida = colecoes[indice_colecao - 1]
                material_escolhido = colecao_escolhida.requisitos_colecao[indice_material - 1]

                rprint("[bold #FF8C00]Material inserido com sucesso![/]")
                sleep(1)

                material_escolhido.subtrair_materiais(quantidade_escolhida)
                quantidade_material = material_escolhido.quantidade_exigida

                if quantidade_material == 0:
                    material_escolhido.coleta_concluida()

                    colecao_concluida = True
                    for item in colecao_escolhida.requisitos_colecao:
                        if not item.material_obtido:
                            colecao_concluida = False
                            break

                    if colecao_concluida:
                        colecao_escolhida.concluir_colecao()
                        rprint(f"[bold #FF8C00]A coleção "
                               f"{formatar_texto(colecao_escolhida.nome_colecao)} foi concluída![/]")
                        heroi.aplicar_recompensas(colecao_escolhida.recompensa_colecao)

                item_escolhido = inventario[nome_item_escolhido]
                item_escolhido.subtrair_quantidade(quantidade_escolhida)

                if item_escolhido.quantidade_item == 0:
                    del inventario[nome_item_escolhido]

    console.input("[bold #FF8C00]Pressione ENTER para voltar ao menu principal.[/]")
    limpar_console()


def confirmar_acesso_codex(colecoes: list[Codex]) -> bool:
    limpar_console()
    exibir_tabela_codex(colecoes)

    resposta = validar_confirmacao("Deseja acessar alguma coleção no Codex? [S/N]: ")

    if resposta == 'S':
        return True

    return False


def escolher_indice_colecao(colecoes: list[Codex]) -> int | bool:
    while True:
        limpar_console()
        exibir_status_colecoes(colecoes)

        indice_escolhido = validar_inteiro("Escolha uma coleção: ")
        quantidade_colecoes = len(colecoes)

        opcao_valida = indice_escolhido <= quantidade_colecoes
        opcao_saida = indice_escolhido == quantidade_colecoes + 1

        if opcao_valida:
            colecao_selecionada = colecoes[indice_escolhido - 1]

            if not colecao_selecionada.colecao_concluida:
                return indice_escolhido

            rprint(f"[bold #FF8C00]A coleção {formatar_texto(colecao_selecionada.nome_colecao)} "
                   f"já foi concluída.[/]")
            sleep(1)

        elif opcao_saida:
            return False

        else:
            rprint("[bold red]Insira um comando válido![/]")
            sleep(1)


def escolher_material_colecao(colecoes: list[Codex],
                              indice_colecao: int) -> int | bool:

    colecao_escolhida = colecoes[indice_colecao - 1]

    while True:
        limpar_console()
        exibir_colecao_escolhida(colecoes, indice_colecao)

        requisitos = colecao_escolhida.requisitos_colecao
        quantidade_requisitos = len(requisitos)

        opcao_escolhida = validar_inteiro("Escolha o índice do material: ")

        opcao_valida = opcao_escolhida <= quantidade_requisitos
        opcao_saida =  opcao_escolhida == quantidade_requisitos + 1

        if opcao_valida:
            material_escolhido = requisitos[opcao_escolhida - 1]

            if not material_escolhido.material_obtido:
                return opcao_escolhida

            rprint("[bold #FF8C00]Material já cadastrado![/]")
            sleep(1)

        elif opcao_saida:
            return False

        else:
            rprint("[bold red]Insira um comando válido![/]")
            sleep(1)


def escolher_quantidade_material(colecoes: list[Codex],
                                 indice_colecao: int,
                                 inventario: dict[str, Inventario],
                                 indice_material: int) -> tuple[str, int, int] | bool:

    colecao_escolhida = colecoes[indice_colecao - 1]
    material_escolhido = colecao_escolhida.requisitos_colecao[indice_material - 1]
    nome_material_escolhido = formatar_texto(material_escolhido.nome_material)

    if nome_material_escolhido not in inventario:
        rprint("[bold red]Você não possui esse material![/]")
        sleep(1)
        return False

    quantidade_atual = inventario[nome_material_escolhido].quantidade_item
    quantidade_necessaria = material_escolhido.quantidade_exigida
    quantidade_desejada = validar_inteiro("Quantidade: ")

    quantidade_maxima_permitida = min(quantidade_necessaria, quantidade_atual)
    quantidade_escolhida = min(quantidade_desejada, quantidade_maxima_permitida)

    return nome_material_escolhido, quantidade_atual, quantidade_escolhida