from copy import deepcopy
from random import random
from time import sleep

from rich import print as rprint

from combat.ui import gerar_barras, mostrar_hp
from inventory.services import dropar_itens
from utils.console import limpar_console
from hero.services import processar_morte

def iniciar_combate(heroi, inimigo) -> bool:
    """
    Executa a dinâmica de combate turno a turno entre herói e inimigo.
    :param heroi: Objeto heroi -> classe Heroi.
    :param inimigo: Objeto inimigo -> classe Inimigo.
    :return: True (vitória), False (derrota).
    """
    turno = 1
    historico_combate = list()
    rprint(f"[bold]Iniciando o combate contra {inimigo.nome}[/]")
    print()
    with mostrar_hp(heroi, inimigo, historico_combate) as live:
        while heroi.verificar_vida() and inimigo.verificar_vida():

            dano_heroi, critico = calcular_dano_combate(heroi, inimigo)
            if critico:
                historico_combate.append(f"[bold yellow][Turno {turno}]: {heroi.nome} acertou um CRÍTICO em "
                                         f"{inimigo.nome} causando {dano_heroi} de dano![/]\n")
            else:
                historico_combate.append(f"[bold][Turno {turno}]: {heroi.nome} causou {dano_heroi} de dano em "
                                     f"{inimigo.nome}.\n")
            inimigo.subtrair_hp(dano_heroi)
            live.update(gerar_barras(heroi, inimigo, historico_combate))
            sleep(0.5)
            turno += 1

            if inimigo.verificar_vida():
                dano_inimigo, critico = calcular_dano_combate(inimigo, heroi, inimigo.calcular_dano_minimo())
                if critico:
                    historico_combate.append(f"[bold red][Turno {turno}]: {inimigo.nome} acertou um golpe CRÍTICO em "
                                             f"{heroi.nome} causando {dano_inimigo} de dano![/]\n")
                else:
                    historico_combate.append(f"[bold][Turno {turno}]: Você sofreu {dano_inimigo} de dano "
                                             f"de {inimigo.nome}.\n")
                heroi.subtrair_hp(dano_inimigo)
                live.update(gerar_barras(heroi, inimigo, historico_combate))
                sleep(0.5)
            turno += 1

        if heroi.verificar_vida():
            historico_combate.append(f"[bold green]O inimigo {inimigo.nome} foi derrotado![/].\n")
            live.update(gerar_barras(heroi, inimigo, historico_combate))
            sleep(0.5)
            heroi.curar_hp(0.3)
        else:
            historico_combate.append(f"[bold red]Você foi morto por {inimigo.nome}[/].\n")
            live.update(gerar_barras(heroi, inimigo, historico_combate))
            sleep(0.5)
    return heroi.verificar_vida()


def calcular_dano_combate(atacante, defensor, dano_minimo = 1) -> tuple:
    """
    Executa os cálculos de combate entre atacantes e defensores.
    :param atacante: Causa o dano.
    :param defensor: Recebe o dano.
    :param dano_minimo: Dano mínimo garantido ao defensor, padrão 1.
    :return: Tupla (dano, critico) - dano causado e se foi critico(True) ou não(False).
    """
    if atacante.acertar_critico():
        return max(dano_minimo, atacante.calcular_dano_critico() - defensor.defesa), True
    return max(dano_minimo, atacante.calcular_dano_normal() - defensor.defesa), False


def processar_recompensas(heroi, inimigo, inventario) -> bool:
    """
    Inicia o combate, processa as recompensas e retorna um valor booleano.
    :param heroi: Objeto heroi -> classe Heroi.
    :param inimigo: Objeto inimigo -> classe Inimigo.
    :param inventario: Dicionário com os objetos da classe Inventario.
    :return: True se o herói venceu o combate, False se o herói morreu.
    """
    combate = iniciar_combate(heroi, inimigo)
    if combate:
        dropar_itens(inimigo, inventario)

        xp_ganho = int(inimigo.recompensa_xp * (1 + heroi.xp_bonus))
        ouro_ganho = int(inimigo.recompensa_ouro * (1 + heroi.ouro_bonus))

        heroi.adicionar_xp(xp_ganho)
        heroi.adicionar_ouro(ouro_ganho)

        rprint(f"[bold #FF8C00]+ {xp_ganho} XP[/]")
        rprint(f"[bold yellow]+ {ouro_ganho} Ouro[/]")
        sleep(0.5)

        while heroi.xp >= heroi.calcular_xp_nivel():
            heroi.diminuir_xp(heroi.calcular_xp_nivel())
            heroi.aumentar_atributos()

    return combate


def preparar_combate(fase, zona, zona_atual, indice_zona, heroi, inventario) -> int:
    """
    Prepara e executa o combate da fase atual, processando recompensas e morte do herói.
    :param fase: Fase atual da zona.
    :param zona: Lista de objetos da classe Zona.
    :param zona_atual: Objeto da zona atual.
    :param indice_zona: Índice da zona atual na lista de zonas.
    :param heroi: Objeto heroi -> classe Heroi.
    :param inventario: Dicionário que contém os objetos da classe Inventário.
    :return: Fase atual (0 se o herói morreu, valor original caso contrário).
    """

    if fase < 10:
        inimigo = zona_atual.gerar_inimigo()
    else:
        inimigo = deepcopy(zona_atual.boss)
    combate = processar_recompensas(heroi, inimigo, inventario)
    if not combate:
        indice_zona, zona = processar_morte(heroi, zona, indice_zona)
        fase = 0
    limpar_console()
    return fase