from base.superclasse import Entidade
from base.item import Item


class Inimigo(Entidade):
    """
    Representa os inimigos encontrados nas zonas do jogo.
    Herda os atributos base da classe Entidade e adiciona recompensas de XP, ouro e sistema de drops.
    :param recompensa_xp: Quantidade de XP concedida ao herói ao derrotar o inimigo.
    :param recompensa_ouro: Quantidade de ouro concedida ao herói ao derrotar o inimigo.
    :param drops: Lista de objetos Item que podem ser dropados ao derrotar o inimigo.
    """

    __PORCENTAGEM_DANO = 0.3

    def __init__(self, nome_personagem: str,
                 hp: int,
                 ataque: int,
                 defesa: int,
                 recompensa_xp: int,
                 recompensa_ouro: int,
                 drops: list[Item]):

        super().__init__(nome_personagem, hp, ataque, defesa, chance_critico=0.30, dano_critico=1.5)
        self.__recompensa_xp = recompensa_xp
        self.__recompensa_ouro = recompensa_ouro
        self.__drops = drops

    @property
    def recompensa_xp(self) -> int: return self.__recompensa_xp

    @property
    def recompensa_ouro(self) -> int: return self.__recompensa_ouro

    @property
    def drops(self) -> list[Item]: return self.__drops

    def calcular_dano_minimo(self) -> int: return round(self.ataque * self.__PORCENTAGEM_DANO)
