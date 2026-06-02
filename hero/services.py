from time import sleep

from rich import print as rprint

from hero.ui import mostrar_menu_equip
from utils.console import limpar_console
from utils.ui import mostrar_menu_principal
from utils.validators import validar_integer


def aprimorar_equipamentos(heroi):
    """
    Utiliza o ouro coletado nos combates para aprimorar o nível dos equipamentos do herói.
    :param heroi: Objeto heroi -> classe Heroi.
    :return: None
    """
    equipamentos_dict = {1: heroi.arma, 2: heroi.armadura, 3: heroi.acessorio}
    while True:
        limpar_console()
        mostrar_menu_principal()
        mostrar_menu_equip()
        opcao_equip = validar_integer("Escolha uma opção: ")
        if opcao_equip in (1, 2, 3):
            rprint(f"[bold #FF8C00]Equipamento: {equipamentos_dict[opcao_equip].nome_equip} |"
                   f" Nível atual: {equipamentos_dict[opcao_equip].nivel_equip}[/]")
            sleep(1)
            evoluir_equipamento(heroi, equipamentos_dict[opcao_equip])
        elif opcao_equip == 4:
            limpar_console()
            break
        else:
            rprint("[bold red]Comando inválido![/]")
        sleep(1)


def evoluir_equipamento(heroi, equipamento):
    """
    Utiliza o ouro coletado em combate para aprimorar os equipamentos desejados.
    :param heroi: Objeto heroi -> classe Heroi
    :param equipamento: Objeto equipamento (criado na classe Heroi) -> classe Equipamento
    :return: None
    """
    custo = equipamento.calcular_custo_upgrade()

    if equipamento.nivel_equip < equipamento.nivel_max:

        if heroi.ouro >= custo:
            heroi.diminuir_ouro(custo)
            equipamento.aumentar_nivel_equip()

            rprint(f"[bold green]{equipamento.nome_equip} aprimorado(a) para o Nível {equipamento.nivel_equip}![/]")
            rprint(f"[bold cyan]Custo: {custo} de ouro | Ouro: {heroi.ouro}[/]")

            bonus = equipamento.calcular_bonus_atual()
            if equipamento == heroi.arma:
                heroi.adicionar_ataque(bonus)
            elif equipamento == heroi.armadura:
                heroi.adicionar_defesa(bonus)
            else:
                heroi.adicionar_hp_max(bonus)

        else:
            rprint(f"[bold red]Recursos insuficientes, falta {custo - heroi.ouro} de ouro![/]")
    else:
        rprint(f"[bold red]{equipamento.nome_equip} está no nível máximo. Vá à Forja e faça o upgrade![/]")


def processar_morte(heroi, zona, indice_zona) -> tuple:
    """
    Realoca o heroi na zona anterior e reseta as fases.
    Se não for possível realocar, apenas reseta as fases.
    :param heroi: Objeto heroi -> class Heroi.
    :param zona: Lista de objetos da classe Zona.
    :param indice_zona: Índice da zona atual na lista de zonas.
    :return: Tupla contendo o novo indice_zona e zona_atual.
    """
    heroi.encher_hp()
    if indice_zona > 1:
        indice_zona -= 1
    return indice_zona, zona[indice_zona]