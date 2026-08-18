from rich.align import Align
from rich.console import Console
from rich.table import Table

from heroi.classe import Heroi
from utilitario.console import limpar_console
from utilitario.formatadores import formatar_porcentagem
from utilitario.interface import exibir_menu_principal

def exibir_atributos_heroi(heroi: Heroi):
    console = Console()
    exibir_menu_principal()
    exibir_tabela_atributos_heroi(heroi)

    console.input("[bold #FF8C00]Pressione ENTER para voltar ao menu principal.[/]")
    limpar_console()


def exibir_tabela_atributos_heroi(heroi: Heroi):
    console = Console()

    tabela_atributos = Table(style='green')

    tabela_atributos.add_column("HEROI", justify='center')
    tabela_atributos.add_column("ATRIBUTOS", justify='center')

    tabela_atributos.add_row(Align.left("Nome do personagem"), Align.right(heroi.nome_personagem))
    tabela_atributos.add_row(Align.left("Level do personagem"), Align.right(str(heroi.nivel_personagem)))
    tabela_atributos.add_row(Align.left("Experiência atual"), Align.right(str(round(heroi.xp))))
    tabela_atributos.add_row(Align.left("Ouro obtido"), Align.right(str(round(heroi.ouro))))
    tabela_atributos.add_row(Align.left("Ataque total (ATK)"), Align.right(str(round(heroi.ataque))))
    tabela_atributos.add_row(Align.left("Defesa total (DEF)"), Align.right(str(round(heroi.defesa))))
    tabela_atributos.add_row(Align.left("HP total (HP)"), Align.right(str(round(heroi.hp_max))))
    tabela_atributos.add_row(Align.left("HP Atual"), Align.right(str(round(heroi.hp))))
    tabela_atributos.add_row(Align.left("Chance de Crítico"), Align.right(formatar_porcentagem(heroi.chance_critico)))
    tabela_atributos.add_row(Align.left("Dano Crítico"), Align.right(formatar_porcentagem(heroi.dano_critico)))
    tabela_atributos.add_section()

    equipamentos_heroi = [heroi.arma, heroi.armadura, heroi.acessorio]
    atributos_heroi = ["ATK:", "DEF:", "HP:"]
    cor_raridade = {"epico": "bold yellow", "unico": "bold magenta", "lendario": "bold red"}

    for equipamento_heroi, atributo_heroi in zip(equipamentos_heroi, atributos_heroi):
        cor_equipamento = cor_raridade.get(equipamento_heroi.raridade, "")
        descricao_equipamento = (f"{equipamento_heroi.nome_equipamento} ({equipamento_heroi.raridade})"
                                 f" (Nv.{equipamento_heroi.nivel_equipamento})")

        if cor_equipamento:
            nome_formatado = f"[{cor_equipamento}]{descricao_equipamento}[/]"
        else:
            nome_formatado = descricao_equipamento

        tabela_atributos.add_row(Align.left(nome_formatado),
                                 Align.left(f"{atributo_heroi:<5} {equipamento_heroi.calcular_bonus_atual()}"))

    console.print(tabela_atributos)


def exibir_menu_equipamentos():
    console = Console()

    table = Table(style='yellow')
    table.add_column("EQUIPAMENTOS", justify='center')

    table.add_row(Align.left("[1] Aprimorar Arma"))
    table.add_row(Align.left("[2] Aprimorar Armadura"))
    table.add_row(Align.left("[3] Aprimorar Acessório"))
    table.add_section()
    table.add_row(Align.left("[bold #FF8C00][4] VOLTAR PARA O MENU PRINCIPAL[/]"))

    console.print(table)