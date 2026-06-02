from rich.console import Console, Group
from rich.live import Live
from rich.progress import ProgressBar


def gerar_barras(heroi, inimigo, historico):
    """
    Cria uma interface visual, exibindo barras de vida durante o combate.
    :param heroi: Objeto heroi -> classe Heroi.
    :param inimigo: Objeto inimigo -> classe Inimigo.
    :param historico: Histórico de combate coletado.
    :return: Objeto Group do rich contendo as barras de HP e o log de combate.
    """
    texto_historico = ''.join(historico)
    barra_heroi = ProgressBar(total=heroi.hp_max, completed=max(0, heroi.hp), width=20)
    barra_inimigo = ProgressBar(total=inimigo.hp_max, completed=max(0, inimigo.hp), width=20)

    conteudo = Group(f"{heroi.nome:<20} :heart: {max(0, heroi.hp)}/{heroi.hp_max}", barra_heroi,
                     f"\n{inimigo.nome:<20} :heart: {max(0, inimigo.hp)}/{inimigo.hp_max}", barra_inimigo,
                     f"\nNível: {heroi.nivel} | Ouro: {heroi.ouro}",
                     f"Exp atual: {heroi.xp} | Exp necessária: {int((heroi.nivel ** 1.2) * 40)}"
                     "",
                     "",
                     texto_historico
                     )

    return conteudo


def mostrar_hp(heroi, inimigo, historico):
    """
    Inicializa o painel de exibição em tempo real do combate.
    :param heroi: Objeto heroi -> classe Heroi.
    :param inimigo: Objeto inimigo -> classe Inimigo.
    :param historico: Histórico de combate coletado.
    :return: Objeto Live do rich que atualiza a interface do combate em tempo real.
    """
    console = Console()
    return Live(gerar_barras(heroi, inimigo, historico), console = console, refresh_per_second = 4)