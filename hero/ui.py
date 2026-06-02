from rich.align import Align
from rich.console import Console
from rich.table import Table

from utils.console import limpar_console
from utils.formatters import formatar_porcentagem
from utils.ui import mostrar_menu_principal

def mostrar_atributos(heroi):
    """
    Exibe todos os atributos do herói.
    :param heroi: Objeto heroi -> classe Heroi.
    :return: None
    """
    console = Console()
    mostrar_menu_principal()
    mostrar_atributos_heroi(heroi)
    console.input("[bold #FF8C00]Pressione ENTER para voltar ao menu principal.[/]")
    limpar_console()


def mostrar_atributos_heroi(heroi):
    """
    Exibe os equipamentos e todos os atributos do herói organizados em uma tabela.
    :param heroi: Objeto heroi -> heroi.nome é acessado via "getter".
    :return: None
    """
    console = Console()
    table = Table(style = 'green')
    table.add_column("HEROI", justify = 'center')
    table.add_column("ATRIBUTOS", justify = 'center')
    table.add_row(Align.left("Nome do personagem"), Align.right(heroi.nome))
    table.add_row(Align.left("Level do personagem"), Align.right(str(heroi.nivel)))
    table.add_row(Align.left("Experiência atual"), Align.right(str(round(heroi.xp))))
    table.add_row(Align.left("Ouro obtido"), Align.right(str(round(heroi.ouro))))
    table.add_row(Align.left("Ataque total (ATK)"), Align.right(str(round(heroi.ataque))))
    table.add_row(Align.left("Defesa total (DEF)"), Align.right(str(round(heroi.defesa))))
    table.add_row(Align.left("HP total (HP)"), Align.right(str(round(heroi.hp_max))))
    table.add_row(Align.left("HP Atual"), Align.right(str(round(heroi.hp))))
    table.add_row(Align.left("Chance de Crítico"), Align.right(formatar_porcentagem(heroi.chance_critico)))
    table.add_row(Align.left("Dano Crítico"), Align.right(formatar_porcentagem(heroi.dano_critico)))
    table.add_section()

    equipamentos_heroi = [heroi.arma, heroi.armadura, heroi.acessorio]
    atributos = ["ATK:", "DEF:", "HP:"]
    cores = {"epico": "bold yellow", "unico": "bold magenta", "lendario": "bold red"}

    for item, atributo in zip(equipamentos_heroi, atributos):
        cor = cores.get(item.raridade, "")
        texto = f"{item.nome_equip} ({item.raridade}) (Nv.{item.nivel_equip})"
        if cor:
            nome_formatado = f"[{cor}]{texto}[/]"
        else:
            nome_formatado = texto
        table.add_row(Align.left(nome_formatado),
                      Align.left(f"{atributo:<5} {item.calcular_bonus_atual()}"))

    console.print(table)


def mostrar_menu_equip():
    """
    Exibe o menu de aprimoramento dos equipamentos do herói.
    :return: None
    """
    console = Console()
    table = Table(style = 'yellow')
    table.add_column("EQUIPAMENTOS", justify = 'center')
    table.add_row(Align.left("[1] Aprimorar Arma"))
    table.add_row(Align.left("[2] Aprimorar Armadura"))
    table.add_row(Align.left("[3] Aprimorar Acessório"))
    table.add_section()
    table.add_row(Align.left("[bold #FF8C00][4] VOLTAR PARA O MENU PRINCIPAL[/]"))
    console.print(table)