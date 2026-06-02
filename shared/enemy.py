from shared.base import Entidade
from shared.item import Item


class Inimigo(Entidade):
    """
    Representa os inimigos encontrados nas zonas do jogo.
    Herda os atributos base da classe Entidade e adiciona recompensas de XP, ouro e sistema de drops.
    :param nome: Nome do inimigo.
    :param hp: HP inicial e máximo do inimigo.
    :param ataque: Valor de ataque do inimigo.
    :param defesa: Valor de defesa do inimigo.
    :param recompensa_xp: Quantidade de XP concedida ao herói ao derrotar o inimigo.
    :param recompensa_ouro: Quantidade de ouro concedida ao herói ao derrotar o inimigo.
    :param drops: Lista de objetos Item que podem ser dropados ao derrotar o inimigo.
"""
    __PORCENTAGEM_DANO = 0.3
    def __init__(self, nome, hp, ataque, defesa, recompensa_xp, recompensa_ouro, drops):
        super().__init__(nome, hp, ataque, defesa, chance_critico = 0.30, dano_critico = 1.5)
        self.__recompensa_xp = int(recompensa_xp)
        self.__recompensa_ouro = int(recompensa_ouro)
        self.__drops = drops


    @property
    def recompensa_xp(self) -> int: return self.__recompensa_xp


    @property
    def recompensa_ouro(self) -> int: return self.__recompensa_ouro


    @property
    def drops(self) -> list[Item]: return self.__drops


    def calcular_dano_minimo(self) -> int: return int(self.ataque * self.__PORCENTAGEM_DANO)
