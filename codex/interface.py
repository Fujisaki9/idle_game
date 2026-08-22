from rich.align import Align
from rich.console import Console
from rich.table import Table

from codex.classe import Codex
from base.recompensa import Recompensa
from utilitario.formatacao import formatar_texto


def exibir_tabela_codex(colecoes: list[Codex]):
    console = Console(width=120)

    tabela_codex = Table(style='yellow')
    tabela_codex.add_column("COLEÇÕES", justify='center', vertical='middle')
    tabela_codex.add_column("MATERIAIS", justify='center')
    tabela_codex.add_column("RECOMPENSAS", justify='center', vertical='middle')
    tabela_codex.add_column("STATUS", justify='center', vertical='middle')

    for colecao in colecoes:
        status_conclusao = formatar_status_colecao(colecao.colecao_concluida)

        materiais_necessarios = []

        for item in colecao.requisitos_colecao:
            materiais_necessarios.append(f"{formatar_texto(item.nome_material)} [{item.quantidade_exigida}]")
        materiais_formatados = "\n".join(materiais_necessarios)

        tabela_codex.add_row(formatar_texto(colecao.nome_colecao),
                             materiais_formatados,
                             formatar_bonus_recompensa(colecao.recompensa_colecao),
                             status_conclusao)

        tabela_codex.add_section()

    console.print(tabela_codex)


def exibir_status_colecoes(colecoes: list[Codex]):
    console = Console()

    tabela_colecoes = Table(style='yellow')
    tabela_colecoes.add_column("COLEÇÕES", justify='center')
    tabela_colecoes.add_column("STATUS", justify='center')

    for indice_colecao, colecao in enumerate(colecoes, 1):
        status_conclusao = formatar_status_colecao(colecao.colecao_concluida)
        tabela_colecoes.add_row(Align.left(f"[{indice_colecao}] {formatar_texto(colecao.nome_colecao)}"),
                                status_conclusao)

    tabela_colecoes.add_section()
    tabela_colecoes.add_row(Align.left(f"[bold #FF8C00][{len(colecoes) + 1}] VOLTAR[/]"))

    console.print(tabela_colecoes)


def exibir_colecao_escolhida(colecoes: list[Codex],
                             indice: int):

    console = Console()

    colecao_codex = Table(style='yellow')
    colecao_codex.add_column("COLEÇÕES", justify='center', vertical='middle')
    colecao_codex.add_column("MATERIAIS NECESSÁRIOS", justify='center')
    colecao_codex.add_column("ZONA DE OBTENÇÃO", justify='center')
    colecao_codex.add_column("RECOMPENSAS", justify='center', vertical='middle')
    colecao_codex.add_column("STATUS", justify='center', vertical='middle')

    colecao_escolhida = colecoes[indice - 1]
    status_conclusao = formatar_status_colecao(colecao_escolhida.colecao_concluida)

    materiais_necessarios = []
    zonas_de_obtencao = []

    for indice_item, item in enumerate(colecao_escolhida.requisitos_colecao, 1):
        zonas_de_obtencao.append(f"{formatar_texto(item.zona_obtencao)}")
        materiais_necessarios.append(f"[{indice_item}] {formatar_texto(item.nome_material)} ({item.quantidade_exigida})")

    zonas_formatadas = "\n".join(zonas_de_obtencao)
    materiais_formatados = "\n".join(materiais_necessarios)

    colecao_codex.add_row(formatar_texto(colecao_escolhida.nome_colecao),
                          Align.left(materiais_formatados),
                          Align.left(zonas_formatadas),
                          formatar_bonus_recompensa(colecao_escolhida.recompensa_colecao),
                          status_conclusao)

    colecao_codex.add_section()
    colecao_codex.add_row("-",
                          f"[bold #FF8C00][{len(colecao_escolhida.requisitos_colecao) + 1}] VOLTAR[/]", "-", "-")

    console.print(colecao_codex)


def formatar_status_colecao(colecao_concluida: bool) -> str:
    if colecao_concluida:
        return "[bold green]Completo[/]"

    return "[bold red]Incompleto[/]"


def formatar_bonus_recompensa(recompensa: Recompensa) -> str:
    bonus_formatados = []

    if recompensa.ataque_bonus != 0:
        bonus_formatados.append(f"+{recompensa.ataque_bonus * 100:.0f}% Ataque")
    if recompensa.defesa_bonus != 0:
        bonus_formatados.append(f"+{recompensa.defesa_bonus * 100:.0f}% Defesa")
    if recompensa.hp_max_bonus != 0:
        bonus_formatados.append(f"+{recompensa.hp_max_bonus * 100:.0f}% HP")
    if recompensa.chance_critico_bonus != 0:
        bonus_formatados.append(f"+{recompensa.chance_critico_bonus * 100:.0f}% Chance Crítico")
    if recompensa.dano_critico_bonus != 0:
        bonus_formatados.append(f"+{recompensa.dano_critico_bonus * 100:.0f}% Dano Crítico")
    if recompensa.xp_bonus != 0:
        bonus_formatados.append(f"+{recompensa.xp_bonus * 100:.0f}% XP")
    if recompensa.ouro_bonus != 0:
        bonus_formatados.append(f"+{recompensa.ouro_bonus * 100:.0f}% Ouro")

    return "\n".join(bonus_formatados)