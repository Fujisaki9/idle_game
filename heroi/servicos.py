from time import sleep

from rich import print as rprint

from base.equipamento import Equipamento
from heroi.classe import Heroi
from heroi.interface import exibir_menu_equipamentos
from utilitario.console import limpar_console
from utilitario.interface import exibir_menu_principal
from utilitario.validadores import validar_inteiro
from zona.classe import Zona


def aprimorar_equipamentos(heroi: Heroi):
    dicionario_equipamentos = {1: heroi.arma, 2: heroi.armadura, 3: heroi.acessorio}
    while True:
        limpar_console()
        exibir_menu_principal()
        exibir_menu_equipamentos()

        equipamento_escolhido = validar_inteiro("Escolha uma opção: ")
        if equipamento_escolhido in (1, 2, 3):
            rprint(f"[bold #FF8C00]Equipamento: {dicionario_equipamentos[equipamento_escolhido].nome_equipamento} |"
                   f" Nível atual: {dicionario_equipamentos[equipamento_escolhido].nivel_equipamento}[/]")
            sleep(1)
            evoluir_equipamento(heroi, dicionario_equipamentos[equipamento_escolhido])
        elif equipamento_escolhido == 4:
            limpar_console()
            break
        else:
            rprint("[bold red]Comando inválido![/]")
        sleep(1)


def evoluir_equipamento(heroi: Heroi,
                        equipamento: Equipamento):

    custo_aprimoramento = equipamento.calcular_custo_upgrade()

    if equipamento.nivel_equipamento < equipamento.nivel_maximo:

        if heroi.ouro >= custo_aprimoramento:
            heroi.diminuir_ouro(custo_aprimoramento)

            bonus_anterior = equipamento.calcular_bonus_atual()
            equipamento.aumentar_nivel_equip()
            bonus_atual = equipamento.calcular_bonus_atual()
            ganho = bonus_atual - bonus_anterior

            rprint(f"[bold green]{equipamento.nome_equipamento} aprimorado(a) para o Nível {equipamento.nivel_equipamento}![/]")
            rprint(f"[bold cyan]Custo: {custo_aprimoramento} de ouro | Ouro: {heroi.ouro}[/]")

            if equipamento == heroi.arma:
                heroi.adicionar_ataque(ganho)

            elif equipamento == heroi.armadura:
                heroi.adicionar_defesa(ganho)

            else:
                heroi.adicionar_hp_max(ganho)

        else:
            rprint(f"[bold red]Recursos insuficientes, falta {custo_aprimoramento - heroi.ouro} de ouro![/]")
    else:
        rprint(f"[bold red]{equipamento.nome_equipamento} está no nível máximo. Vá à Forja e faça o upgrade![/]")


def processar_derrota(heroi: Heroi,
                      zona: list[Zona],
                      indice_zona: int) -> tuple[int, Zona]:

    heroi.curar_hp_total()
    if indice_zona > 1:
        indice_zona -= 1

    return indice_zona, zona[indice_zona]