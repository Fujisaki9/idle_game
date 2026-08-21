from rich.console import Console, Group
from rich.live import Live
from rich.progress import ProgressBar

from base.inimigo import Inimigo
from heroi.classe import Heroi


def exibir_interface_combate(heroi: Heroi,
                            inimigo: Inimigo,
                            historico: list[str]):

    console = Console()

    return Live(criar_interface_combate(heroi, inimigo, historico), console=console, refresh_per_second=4)


def criar_interface_combate(heroi: Heroi,
                            inimigo: Inimigo,
                            historico: list[str]):
    """
    Cria uma interface visual, exibindo barras de vida durante o combate.
    :param heroi: Objeto heroi -> classe Heroi.
    :param inimigo: Objeto inimigo -> classe Inimigo.
    :param historico: Histórico de combate coletado.
    :return: Objeto Group do rich contendo as barras de HP e o log de combate.
    """
    mensagens_combate = ''.join(historico)

    barra_heroi = ProgressBar(total=heroi.hp_max, completed=max(0, heroi.hp), width=20)
    barra_inimigo = ProgressBar(total=inimigo.hp_max, completed=max(0, inimigo.hp), width=20)

    interface_combate = Group(f"{heroi.nome_personagem:<20} :heart: {max(0, heroi.hp)}/{heroi.hp_max}", barra_heroi,
                     f"\n{inimigo.nome_personagem:<20} :heart: {max(0, inimigo.hp)}/{inimigo.hp_max}", barra_inimigo,
                     f"\nNível: {heroi.nivel_personagem} | Ouro: {heroi.ouro}",
                     f"Exp atual: {heroi.xp} | Exp necessária: {heroi.calcular_xp_nivel()}",
                     "",
                     "",
                     mensagens_combate
                     )

    return interface_combate