from time import sleep

from rich import print as rprint
from rich.console import Console

from codex.classe import Codex
from combate.servicos import preparar_combate
from heroi.classe import Heroi
from inventario.classe import Inventario
from persistencia.servicos import salvar_progresso_jogo
from utilitario.console import limpar_console
from utilitario.interface import exibir_menu_principal
from utilitario.validacao import validar_inteiro
from zona.classe import Zona
from zona.interface import exibir_menu_zonas, exibir_opcoes_repeticao, exibir_tabela_zonas


def acessar_proxima_zona(indice_zona: int,
                         zona: list[Zona],
                         heroi: Heroi) -> tuple[int, Zona]:
    """
    Verifica os requisitos e acessa a próxima zona.
    :param indice_zona: Índice da zona atual na lista de zonas.
    :param zona: Lista de objetos da classe Zona.
    :param heroi: Objeto heroi -> classe Heroi.
    :return: Tupla contendo o novo indice_zona e zona_atual.
    """

    zona_atual = zona[indice_zona]
    if indice_zona + 1 < len(zona):

        if zona[indice_zona + 1].nivel_minimo <= heroi.nivel_personagem:
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


def repetir_zona(zona: list[Zona],
                 zona_atual: Zona,
                 indice_zona: int,
                 heroi: Heroi,
                 inventario: dict[str, Inventario]):

    while True:
        limpar_console()
        exibir_menu_zonas()
        exibir_opcoes_repeticao()

        escolher_opcao = validar_inteiro("Escolha uma opção: ")

        if escolher_opcao in (1, 2, 3):

            if escolher_opcao == 1:
                quantidade_repeticao = 5
            elif escolher_opcao == 2:
                quantidade_repeticao = 10
            else:
                quantidade_repeticao = validar_inteiro("Quantidade de repetições: ")

            sleep(1)
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


def escolher_zona(indice_zona: int,
                  zona: list[Zona],
                  heroi: Heroi,
                  inventario: dict[str, Inventario],
                  codex: list[Codex]) -> tuple[int, Zona]:

    console = Console()
    zona_atual = zona[indice_zona]

    novo_indice = selecionar_indice_zona_valido(zona, heroi, exibir_menu_principal)

    if novo_indice is not None:
        indice_zona = novo_indice
        zona_atual = zona[indice_zona]
        salvar_progresso_jogo(heroi, zona, inventario, indice_zona, codex)
        rprint(f"[bold #FF8C00]Indo para a zona selecionada...[/]")
        sleep(1)
        rprint(f"[bold #FF8C00]Zona atual: [{novo_indice}] {zona_atual.nome_zona}.[/]")
        sleep(1)

    console.input("[bold #FF8C00]Pressione ENTER para voltar ao menu principal.[/]")
    limpar_console()
    return indice_zona, zona_atual


def selecionar_zona(zona: list[Zona],
                    indice_zona: int,
                    heroi: Heroi) -> tuple[int, Zona]:

    zona_atual = zona[indice_zona]

    novo_indice = selecionar_indice_zona_valido(zona, heroi, exibir_menu_zonas)

    if novo_indice is not None:
        indice_zona = novo_indice
        zona_atual = zona[indice_zona]
        rprint(f"[bold #FF8C00]Configurando a zona...[/]")
        sleep(1)
        rprint(f"[bold #FF8C00]Zona atual: [{novo_indice}] {zona_atual.nome_zona}.[/]")
        sleep(1)

    limpar_console()
    return indice_zona, zona_atual


def selecionar_indice_zona_valido(zona: list[Zona],
                                   heroi: Heroi,
                                   exibir_menu) -> int | None:
    """
    Exibe o menu informado em loop até o jogador escolher uma zona liberada ou sair.
    :param zona: Lista de objetos da classe Zona.
    :param heroi: Objeto heroi -> classe Heroi.
    :param exibir_menu: Função usada para exibir o menu (ex: exibir_menu_zonas, exibir_menu_principal).
    :return: Índice da zona escolhida (base 0), ou None se o jogador cancelou.
    """
    while True:
        exibir_menu()

        indice_escolhido = escolher_indice_zona(zona)

        if not indice_escolhido:
            return None

        zona_escolhida = zona[indice_escolhido - 1]

        if zona_escolhida.zona_concluida and heroi.nivel_personagem >= zona_escolhida.nivel_minimo:
            return indice_escolhido - 1

        rprint("[bold red]Zona bloqueada![/]")
        sleep(1)


def escolher_indice_zona(zona: list[Zona]) -> int | bool:
    while True:
        limpar_console()
        exibir_tabela_zonas(zona)

        escolha_zona = validar_inteiro("Escolha uma zona: ")

        opcao_valida = escolha_zona <= len(zona)
        opcao_saida = escolha_zona == len(zona) + 1

        if opcao_valida:
            return escolha_zona
        elif opcao_saida:
            return False
        else:
            rprint("[bold red]Comando inválido![/]")
            sleep(1)
