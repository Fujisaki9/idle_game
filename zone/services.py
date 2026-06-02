from time import sleep

from rich import print as rprint
from rich.console import Console

from combat.services import preparar_combate
from save.services import salvar_jogo
from utils.console import limpar_console
from utils.ui import mostrar_menu_principal
from utils.validators import validar_integer
from zone.ui import mostrar_menu_zona, mostrar_opcoes_repeticao, mostrar_tabela_zonas



def acessar_proxima_zona(indice_zona, zona, heroi) -> tuple:
    """
    Verifica os requisitos e acessa a próxima zona.
    :param indice_zona: Índice da zona atual na lista de zonas.
    :param zona: Lista de objetos da classe Zona.
    :param heroi: Objeto heroi -> classe Heroi.
    :return: Tupla contendo o novo indice_zona e zona_atual.
    """
    zona_atual = zona[indice_zona]
    if indice_zona + 1 < len(zona):
        if zona[indice_zona + 1].nivel_minimo <= heroi.nivel:
            indice_zona += 1
            zona_atual = zona[indice_zona]
            rprint("[bold #FF8C00]Acessando a próxima zona![/]")
            sleep(1)
            rprint(f"[bold #FF8C00][Zona {indice_zona + 1}] {zona_atual.nome_zona}[/]")
            sleep(1)
        else:
            rprint(f"[bold red]Você não tem nível suficiente para acessar a próxima zona[/]")
            sleep(1)
            rprint(f"[bold red][Zona {indice_zona + 2}] {zona[indice_zona + 1].nome_zona} | "
                   f"Nível mínimo: {zona[indice_zona + 1].nivel_minimo}.[/]")
            sleep(1)
            rprint("[bold red]Repetindo a zona atual.[/]")
            sleep(1)
    else:
        rprint("[bold green]Você completou todas as zonas![/]")
        sleep(1)
    return indice_zona, zona_atual


def escolher_zona(indice_zona, zona, heroi, inventario, codex) -> tuple:
    """
    Exibe as zonas disponíveis e permite ao jogador navegar entre as zonas já desbloqueadas.
    :param indice_zona: Índice da zona atual na lista de zonas.
    :param zona: Lista de objetos da classe Zona.
    :param heroi: Objeto heroi -> classe Heroi.
    :param inventario: Dicionário que contém os objetos da classe Inventário.
    :param codex: Lista de objetos da classe Codex.
    :return: Tupla contendo o novo indice_zona e zona_atual após a escolha do jogador.
    """
    console = Console()
    zona_atual = zona[indice_zona]

    while True:
        mostrar_menu_principal()
        indice_escolhido = escolher_indice_zona(zona)
        if indice_escolhido:
            zona_escolhida = zona[indice_escolhido - 1]
            if zona_escolhida.zona_concluida and heroi.nivel >= zona_escolhida.nivel_minimo:
                indice_zona = indice_escolhido - 1
                zona_atual = zona[indice_zona]
                salvar_jogo(heroi, zona, inventario, indice_zona, codex)
                rprint(f"[bold #FF8C00]Indo para a zona selecionada...[/]")
                sleep(1)
                rprint(f"[bold #FF8C00]Zona atual: [{indice_escolhido}] {zona_atual.nome_zona}.[/]")
                sleep(1)
                break
            else:
                rprint("[bold red]Zona bloqueada![/]")
                sleep(1)
        else:
            break
    console.input("[bold #FF8C00]Pressione ENTER para voltar ao menu principal.[/]")
    limpar_console()
    return indice_zona, zona_atual


def escolher_indice_zona(zona) -> int | bool:
    """
    Exibe as zonas disponíveis e valida a escolha do jogador.
    :param zona: Lista de objetos da classe Zona.
    :return: Índice da zona escolhida (int) ou False caso o usuário deseje retornar.
    """
    while True:
        limpar_console()
        mostrar_tabela_zonas(zona)
        escolha_zona = validar_integer("Escolha uma zona: ")
        if escolha_zona <= len(zona):
            return escolha_zona
        elif escolha_zona == len(zona) + 1:
            return False
        else:
            rprint("[bold red]Comando inválido![/]")
            sleep(1)


def repetir_zona(zona, zona_atual, indice_zona, heroi, inventario):
    """
    Permite ao jogador repetir uma zona já concluída um número determinado de vezes.
    :param zona: Lista de objetos da classe Zona.
    :param zona_atual: Objeto da zona selecionada para repetição.
    :param indice_zona: Índice da zona atual na lista de zonas.
    :param heroi: Objeto heroi -> classe Heroi.
    :param inventario: Dicionário que contém os objetos da classe Inventário.
    """
    while True:
        limpar_console()
        mostrar_menu_zona()
        mostrar_opcoes_repeticao()
        escolher_opcao = validar_integer("Escolha uma opção: ")
        if escolher_opcao in (1, 2, 3):
            if escolher_opcao == 1:
                quantidade_repeticao = 5
            elif escolher_opcao == 2:
                quantidade_repeticao = 10
            else:
                quantidade_repeticao = validar_integer("Quantidade de repetições: ")

            limpar_console()
            fase = repeticao = 0
            while True:
                fase += 1
                rprint(f"[bold #FF8C00][Zona {indice_zona + 1}] {zona_atual.nome_zona} -> Fase {fase}"
                       f" | Repetir [{repeticao + 1}/{quantidade_repeticao}][/]")
                preparar_combate(fase, zona, zona_atual, indice_zona, heroi, inventario)
                if fase == 10:
                    repeticao += 1
                    fase = 0
                if repeticao == quantidade_repeticao:
                    rprint(f"[bold #FF8C00][{quantidade_repeticao}/{quantidade_repeticao}]"
                           f" Repetições concluídas! Retornando ao menu...[/]")
                    sleep(1)
                    break

        elif escolher_opcao == 4:
            rprint(f"[bold #FF8C00]Saindo do modo repetição...[/]")
            sleep(1)
            limpar_console()
            break
        else:
            rprint("[bold red]Digite um comando válido![/]")


def selecionar_zona(zona, indice_zona, heroi) -> tuple:
    """
    Exibe as zonas disponíveis e permite ao jogador selecionar uma zona já concluída para repetição.
    :param zona: Lista de objetos da classe Zona.
    :param indice_zona: Índice da zona atual na lista de zonas.
    :param heroi: Objeto heroi -> classe Heroi.
    :return: Tupla contendo o novo indice_zona e zona_atual após a escolha do jogador.
    """
    zona_atual = zona[indice_zona]

    while True:
        mostrar_menu_zona()
        indice_escolhido = escolher_indice_zona(zona)
        if indice_escolhido:
            zona_escolhida = zona[indice_escolhido - 1]
            if zona_escolhida.zona_concluida and heroi.nivel >= zona_escolhida.nivel_minimo:
                indice_zona = indice_escolhido - 1
                zona_atual = zona[indice_zona]
                rprint(f"[bold #FF8C00]Configurando a zona...[/]")
                sleep(1)
                rprint(f"[bold #FF8C00]Zona atual: [{indice_escolhido}] {zona_atual.nome_zona}.[/]")
                sleep(1)
                break
            else:
                rprint("[bold red]Zona bloqueada![/]")
                sleep(1)
        else:
            break
    limpar_console()
    return indice_zona, zona_atual