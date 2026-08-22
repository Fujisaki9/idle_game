import os
from time import sleep

from rich import print as rprint

from codex.classe import Codex
from codex.database import criar_colecoes_codex
from codex.servicos import acessar_codex
from forja.servicos import forjar_equipamentos
from heroi.classe import Heroi
from heroi.interface import exibir_atributos_heroi
from heroi.servicos import aprimorar_equipamentos
from inventario.classe import Inventario
from inventario.servicos import abrir_inventario
from persistencia.servicos import carregar_jogo, continuar_jogo, encerrar_jogo, salvar_progresso_jogo
from utilitario.console import limpar_console
from utilitario.interface import exibir_menu_principal
from utilitario.validacao import validar_inteiro
from zona.classe import Zona
from zona.database import criar_zonas
from zona.interface import exibir_menu_zonas
from zona.servicos import acessar_proxima_zona, escolher_zona, repetir_zona, selecionar_zona


def inicializar_jogo() -> tuple[Heroi, dict[str, Inventario], list[Codex], list[Zona], int, Zona]:
    """
    Inicializa ou carrega o estado do jogo (herói, inventário, codex, zonas).
    :return: Tupla (heroi, inventario, codex, zona, indice_zona, zona_atual).
    """
    if os.path.exists("save.json"):
        heroi = Heroi(nome_personagem="")
        rprint("Carregando o jogo...")
        sleep(1)

    else:
        heroi = Heroi(nome_personagem=input("Insira o nome do seu personagem: ").strip())

    inventario = dict()
    codex = criar_colecoes_codex()
    zonas = criar_zonas()

    _, indice_zona = carregar_jogo(heroi, zonas, inventario, codex)
    zona_atual = zonas[indice_zona]

    return heroi, inventario, codex, zonas, indice_zona, zona_atual


def executar_menu_zona_concluida(indice_zona: int,
                                 zonas: list[Zona],
                                 zona_atual: Zona,
                                 heroi: Heroi,
                                 inventario: dict[str, Inventario]) -> tuple[int, Zona, bool]:
    """
    Exibe o menu de opções após a conclusão de uma zona (10 fases).
    :return: Tupla (indice_zona, zona_atual, acessar_menu_principal).
    """
    while True:
        exibir_menu_zonas()
        opcao = validar_inteiro("Escolha uma opção: ")

        match opcao:
            case 1:
                indice_zona, zona_atual = acessar_proxima_zona(indice_zona, zonas, heroi)
                return indice_zona, zona_atual, False
            case 2:
                indice_zona, zona_atual = selecionar_zona(zonas, indice_zona, heroi)
                rprint(f"[bold #FF8C00]Zona atual: [{indice_zona + 1}] {zona_atual.nome_zona}.[/]")
                sleep(0.5)
                repetir_zona(zonas, zona_atual, indice_zona, heroi, inventario)
                continue
            case 3:
                return indice_zona, zona_atual, True
            case _:
                rprint("[bold red]Digite uma opção válida![/]")


def executar_menu_principal(indice_zona: int,
                             zona: list[Zona],
                             zona_atual: Zona,
                             heroi: Heroi,
                             inventario: dict[str, Inventario],
                             codex: list[Codex]) -> tuple[int, Zona, bool, bool]:
    """
    Exibe o menu principal (fora de combate) e executa a opção escolhida.
    :return: Tupla (indice_zona, zona_atual, continuar_gameplay, jogo_encerrado).
    """
    while True:
        exibir_menu_principal()
        rprint(f"[bold #FF8C00]Zona atual: [{indice_zona + 1}] {zona_atual.nome_zona}.[/]")

        opcao = validar_inteiro("Escolha uma opção: ")

        limpar_console()

        match opcao:
            case 1:
                exibir_atributos_heroi(heroi)
            case 2:
                aprimorar_equipamentos(heroi)
            case 3:
                forjar_equipamentos(heroi, inventario)
            case 4:
                abrir_inventario(inventario, heroi)
            case 5:
                acessar_codex(codex, inventario, heroi)
                salvar_progresso_jogo(heroi, zona, inventario, indice_zona, codex)
            case 6:
                indice_zona, zona_atual = escolher_zona(indice_zona, zona, heroi, inventario, codex)
            case 7:
                continuar_jogo(heroi, zona, inventario, indice_zona, codex)
                return indice_zona, zona_atual, True, False
            case 8:
                encerrar_jogo(heroi, zona, inventario, indice_zona, codex)
                return indice_zona, zona_atual, True, True
            case _:
                rprint("[bold red]ERRO: Algo aconteceu![/]")