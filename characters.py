from base import Entidade
from equipment import Equipamento


class Heroi(Entidade):
    """
    Representa o personagem principal do jogo.
    Herda os atributos base da classe Entidade e adiciona sistema de progressão, equipamentos e recursos.
    """
    def __init__(self, nome):
        super().__init__(nome, hp = 150, ataque = 18, defesa = 6)
        self.nivel = 1
        self.xp = 0
        self.ouro = 0
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
    """
    def __init__(self, nome, hp, ataque, defesa, recompensa_xp, recompensa_ouro, drops):
        super().__init__(nome, hp, ataque, defesa)
        self.recompensa_xp = recompensa_xp
        self.recompensa_ouro = recompensa_ouro
        self.drops = drops

