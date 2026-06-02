from rich.align import Align
from rich.console import Console
from rich.table import Table

from utils.formatters import formatar_strings


def mostrar_codex(codex):
    """
    Exibe o Codex, mostrando as coleções, materiais necessários, recompensas e status de conclusão.
    :param codex: Lista de objetos da classe Codex.
    :return: None
    """
    console = Console(width = 120)
    table = Table(style = 'yellow')
    table.add_column("COLEÇÕES", justify = 'center', vertical = 'middle')
    table.add_column("MATERIAIS", justify = 'center')
    table.add_column("RECOMPENSAS", justify = 'center', vertical = 'middle')
    table.add_column("STATUS", justify = 'center', vertical = 'middle')
    for colecao in codex:
        if colecao.conclusao:
            status = "[bold green]Completo[/]"
        else:
            status = "[bold red]Incompleto[/]"
        materiais = list()
        for item in colecao.requisitos:
            materiais.append(f"{formatar_strings(item.nome_material)} [{item.quantidade}]")
        materiais_formatados =  "\n".join(materiais)
        table.add_row(formatar_strings(colecao.nome_colecao),
                      materiais_formatados,
                      formatar_recompensa_codex(colecao.recompensa_colecao),
                      status)
        table.add_section()
    console.print(table)


def mostrar_indice_codex(codex):
    """
    Exibe em uma tabela os nomes das coleções e seus status de conclusão.
    :param codex: Lista de objetos da classe Codex.
    :return: None
    """
    console = Console()
    table = Table(style='yellow')
    table.add_column("COLEÇÕES", justify='center')
    table.add_column("STATUS", justify='center')
    for indice, colecao in enumerate(codex, 1):
        if colecao.conclusao:
            status = "[bold green]Completo[/]"
        else:
            status = "[bold red]Incompleto[/]"
        table.add_row(Align.left(f"[{indice}] {formatar_strings(colecao.nome_colecao)}"), status)
    table.add_section()
    table.add_row(Align.left(f"[bold #FF8C00][{len(codex) + 1}] VOLTAR[/]"))
    console.print(table)


def mostrar_colecao_codex(codex, indice, inventario):
    """
    Exibe em uma tabela uma coleção específica do Codex.
    :param codex: Lista de objetos da classe Codex.
    :param indice: Indica uma coleção específica dentro da lista de coleções.
    :param inventario: Dicionário que contém as objetos da classe Inventário.
    :return: None.
    """
    console = Console()
    table = Table(style = 'yellow')
    table.add_column("COLEÇÕES", justify='center', vertical = 'middle')
    table.add_column("MATERIAIS NECESSÁRIOS", justify='center')
    table.add_column("ZONA DE OBTENÇÃO", justify='center')
    table.add_column("RECOMPENSAS", justify='center', vertical='middle')
    table.add_column("STATUS", justify='center', vertical='middle')
    colecao = codex[indice - 1]
    if colecao.conclusao:
        status = "[bold green]Completo[/]"
    else:
        status = "[bold red]Incompleto[/]"
    materiais = list()
    zonas_drop = list()
    for num, item in enumerate(colecao.requisitos, 1):
        zonas_drop.append(f"{formatar_strings(item.zona_obtencao)}")
        materiais.append(f"[{num}] {formatar_strings(item.nome_material)} ({item.quantidade})")
    zonas_formatadas = "\n".join(zonas_drop)
    materiais_formatados = "\n".join(materiais)
    table.add_row(formatar_strings(colecao.nome_colecao),
                  Align.left(materiais_formatados),
                  Align.left(zonas_formatadas),
                  formatar_recompensa_codex(colecao.recompensa_colecao),
                  status)
    table.add_section()
    table.add_row("-", f"[bold #FF8C00][{len(colecao.requisitos) + 1}] VOLTAR[/]", "-", "-")

    console.print(table)


def formatar_recompensa_codex(recompensa_colecao):
    """
    Formata os valores das recompensas para exibição na tabela.
    :param recompensa_colecao: Recompensa final da coleção.
    :return: String formatada com os bônus da recompensa separados por quebra de linha.
    """
    resultado = list()
    if recompensa_colecao.ataque != 0:
        resultado.append(f"+{recompensa_colecao.ataque * 100:.0f}% Ataque")
    if recompensa_colecao.defesa != 0:
        resultado.append(f"+{recompensa_colecao.defesa * 100:.0f}% Defesa")
    if recompensa_colecao.hp_max != 0:
        resultado.append(f"+{recompensa_colecao.hp_max * 100:.0f}% HP")
    if recompensa_colecao.chance_critico != 0:
        resultado.append(f"+{recompensa_colecao.chance_critico * 100:.0f}% Chance Crítico")
    if recompensa_colecao.dano_critico != 0:
        resultado.append(f"+{recompensa_colecao.dano_critico * 100:.0f}% Dano Crítico")
    if recompensa_colecao.xp_bonus != 0:
        resultado.append(f"+{recompensa_colecao.xp_bonus * 100:.0f}% XP")
    if recompensa_colecao.ouro_bonus != 0:
        resultado.append(f"+{recompensa_colecao.ouro_bonus * 100:.0f}% Ouro")
    return "\n".join(resultado)