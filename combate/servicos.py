from copy import deepcopy
from time import sleep

from rich import print as rprint

from combate.interface import criar_interface_combate, exibir_interface_combate
from base.inimigo import Inimigo
from heroi.classe import Heroi
from heroi.servicos import processar_derrota
from inventario.classe import Inventario
from inventario.servicos import coletar_drops
from utilitario.console import limpar_console
from zona.classe import Zona


def preparar_combate(fase: int,
                     zonas: list[Zona],
                     zona_atual: Zona,
                     indice_zona: int,
                     heroi: Heroi,
                     inventario: dict[str, Inventario]) -> int:

    if fase < 10:
        inimigo = zona_atual.gerar_inimigo()
    else:
        inimigo = deepcopy(zona_atual.boss)

    resultado_combate = processar_recompensas_combate(heroi, inimigo, inventario)

    if not resultado_combate:
        indice_zona, zonas = processar_derrota(heroi, zonas, indice_zona)
        fase = 0

    limpar_console()
    return fase


def processar_recompensas_combate(heroi: Heroi,
                                  inimigo: Inimigo,
                                  inventario: dict[str, Inventario]) -> bool:

    resultado_combate = iniciar_combate(heroi, inimigo)

    if resultado_combate:
        coletar_drops(inimigo, inventario)

        xp_ganho = int(inimigo.recompensa_xp * (1 + heroi.xp_bonus_heroi))
        ouro_ganho = int(inimigo.recompensa_ouro * (1 + heroi.ouro_bonus_heroi))

        heroi.adicionar_xp(xp_ganho)
        heroi.adicionar_ouro(ouro_ganho)

        rprint(f"[bold #FF8C00]+ {xp_ganho} XP[/]")
        rprint(f"[bold yellow]+ {ouro_ganho} Ouro[/]")
        sleep(0.5)

        while heroi.xp >= heroi.calcular_xp_nivel():
            heroi.diminuir_xp(heroi.calcular_xp_nivel())
            heroi.aumentar_atributos()

    return resultado_combate


def iniciar_combate(heroi: Heroi,
                    inimigo: Inimigo) -> bool:

    turno = 1
    historico_combate = []

    rprint(f"[bold]Iniciando o combate contra {inimigo.nome_personagem}[/]")
    print()

    with exibir_interface_combate(heroi, inimigo, historico_combate) as interface_combate:

        while heroi.verificar_vida() and inimigo.verificar_vida():
            dano_heroi, critico_heroi = calcular_dano_combate(heroi, inimigo)

            if critico_heroi:
                historico_combate.append(f"[bold yellow][Turno {turno}]: {heroi.nome_personagem} acertou um CRÍTICO em "
                                         f"{inimigo.nome_personagem} causando {dano_heroi} de dano![/]\n")
            else:
                historico_combate.append(f"[bold][Turno {turno}]: {heroi.nome_personagem} causou {dano_heroi} de dano em "
                                         f"{inimigo.nome_personagem}.\n")

            inimigo.subtrair_hp(dano_heroi)
            interface_combate.update(criar_interface_combate(heroi, inimigo, historico_combate))
            sleep(0.5)
            turno += 1

            if inimigo.verificar_vida():
                dano_inimigo, critico_inimigo = calcular_dano_combate(inimigo, heroi, inimigo.calcular_dano_minimo())

                if critico_inimigo:
                    historico_combate.append(f"[bold red][Turno {turno}]: {inimigo.nome_personagem} acertou um golpe "
                                             f"CRÍTICO em {heroi.nome_personagem} causando {dano_inimigo} de dano![/]\n")
                else:
                    historico_combate.append(f"[bold][Turno {turno}]: Você sofreu {dano_inimigo} de dano "
                                             f"de {inimigo.nome_personagem}.\n")

                heroi.subtrair_hp(dano_inimigo)
                interface_combate.update(criar_interface_combate(heroi, inimigo, historico_combate))
                sleep(0.5)

            turno += 1

        if heroi.verificar_vida():
            historico_combate.append(f"[bold green]O inimigo {inimigo.nome_personagem} foi derrotado![/].\n")
            interface_combate.update(criar_interface_combate(heroi, inimigo, historico_combate))
            sleep(0.5)
            heroi.curar_hp()
        else:
            historico_combate.append(f"[bold red]Você foi morto por {inimigo.nome_personagem}[/].\n")
            interface_combate.update(criar_interface_combate(heroi, inimigo, historico_combate))
            sleep(0.5)

    return heroi.verificar_vida()


def calcular_dano_combate(atacante, defensor, dano_minimo=1) -> tuple[int, bool]:
    if atacante.acertar_critico():
        return max(dano_minimo, atacante.calcular_dano_critico() - defensor.defesa), True

    return max(dano_minimo, atacante.calcular_dano_normal() - defensor.defesa), False