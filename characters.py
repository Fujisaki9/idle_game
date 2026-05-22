from base import Entidade
from equipment import Equipamento

class Heroi(Entidade):
    """
    Representa o personagem principal do jogo.
    Herda os atributos base da classe Entidade e adiciona sistema de progressão, equipamentos e recursos.
    :param nome: Nome do herói definido pelo jogador.
    """
    def __init__(self, nome):
        super().__init__(nome, hp = 150, ataque = 18, defesa = 6, chance_critico = 0.30, dano_critico = 1.5)
        self.nivel = 1
        self.xp = 0
        self.ouro = 0
        self.xp_bonus = 0
        self.ouro_bonus = 0
        self.arma = Equipamento("Espada", 3, 6, 10, 15, 25, 40)
        self.armadura = Equipamento("Armadura", 2, 4, 7, 11, 16,
                                    22)
        self.acessorio = Equipamento("Acessório", 20, 40, 70,
                                     110, 160, 220)


    def aumentar_atributos(self):
        """
        Efetua a adição de atributos toda vez que o herói sobe de nível.
        Ganhos de atributo por nível:
        |Ataque = +3
        |Defesa = +1
        |HP = + 20
        |HP Máx = +20|
        :return: None
        """
        self.nivel += 1
        self.hp += 20
        self.hp_max += 20
        self.ataque += 3
        self.defesa += 1


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
    def __init__(self, nome, hp, ataque, defesa, recompensa_xp, recompensa_ouro, drops):
        super().__init__(nome, hp, ataque, defesa, chance_critico = 0.30, dano_critico = 1.5)
        self.recompensa_xp = recompensa_xp
        self.recompensa_ouro = recompensa_ouro
        self.drops = drops

