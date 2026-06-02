from shared.base import Entidade
from shared.equipment import Equipamento


class Heroi(Entidade):
    """
    Representa o personagem principal do jogo.
    Herda os atributos base da classe Entidade e adiciona sistema de progressão, equipamentos e recursos.
    :param nome: Nome do herói definido pelo jogador.
    """
    __MULTIPLICADOR_XP = 40
    __EXPOENTE_XP = 1.2
    def __init__(self, nome):
        super().__init__(nome, hp = 150, ataque = 18, defesa = 6, chance_critico = 0.30, dano_critico = 1.5)
        self.__nivel = 1
        self.__xp = 0
        self.__ouro = 0
        self.__xp_bonus = 0
        self.__ouro_bonus = 0
        self.__arma = Equipamento("Espada", 3, 6, 10, 15, 25,
                                  40)
        self.__armadura = Equipamento("Armadura", 2, 4, 7, 11, 16,
                                    22)
        self.__acessorio = Equipamento("Acessório", 20, 40, 70,
                                     110, 160, 220)


    @property
    def nivel(self) -> int: return self.__nivel


    @nivel.setter
    def nivel(self, nivel_novo): self.__nivel = int(nivel_novo)


    @property
    def xp(self) -> int: return self.__xp


    @xp.setter
    def xp(self, xp_nova): self.__xp = int(xp_nova)


    @property
    def ouro(self) -> int: return self.__ouro


    @ouro.setter
    def ouro(self, ouro_novo): self.__ouro = int(ouro_novo)


    @property
    def xp_bonus(self) -> float: return self.__xp_bonus


    @xp_bonus.setter
    def xp_bonus(self, xp_bonus_novo): self.__xp_bonus = float(xp_bonus_novo)


    @property
    def ouro_bonus(self) -> float: return self.__ouro_bonus


    @ouro_bonus.setter
    def ouro_bonus(self, ouro_bonus_novo): self.__ouro_bonus = float(ouro_bonus_novo)

    @property
    def arma(self) -> Equipamento: return self.__arma


    @property
    def armadura(self) -> Equipamento: return self.__armadura


    @property
    def acessorio(self) -> Equipamento: return self.__acessorio


    def aumentar_nivel(self, valor): self.__nivel += int(valor)


    def calcular_xp_nivel(self) -> int:
        """
        Calcular a quantidade de experiência necessária para subir de nível.
        :return: Quantidade de XP necessária.
        """
        return int((self.__nivel ** self.__EXPOENTE_XP) * self.__MULTIPLICADOR_XP)


    def adicionar_xp(self, valor): self.__xp += int(valor)


    def diminuir_xp(self, valor): self.__xp = max(0, self.__xp - int(valor))


    def adicionar_xp_bonus(self, valor): self.__xp_bonus += valor


    def adicionar_ouro(self, valor): self.__ouro += int(valor)


    def diminuir_ouro(self, valor): self.__ouro = max(0, self.__ouro - int(valor))


    def adicionar_ouro_bonus(self, valor): self.__ouro_bonus += valor


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
        self.aumentar_nivel(1)
        self.adicionar_hp_max(20)
        self.adicionar_ataque(3)
        self.adicionar_defesa(1)


    def aplicar_recompensas(self, recompensa):
        """
        Aplica os bônus percentuais da recompensa nos atributos do personagem, calculando o ganho com base no valor
        atual de cada atributo.
        :param recompensa: Objeto Recompensa com os bônus percentuais a serem aplicados nos atributos do herói.
        :return: None.
        """
        if recompensa.ataque != 0:
            self.adicionar_ataque(self.ataque * recompensa.ataque)
        if recompensa.defesa != 0:
            self.adicionar_defesa(self.defesa * recompensa.defesa)
        if recompensa.hp_max != 0:
            self.adicionar_hp_max(self.hp_max * recompensa.hp_max)
            self.encher_hp()
        if recompensa.chance_critico != 0:
            self.adicionar_chance_critico(self.chance_critico * recompensa.chance_critico)
        if recompensa.dano_critico != 0:
            self.adicionar_dano_critico(self.dano_critico *  recompensa.dano_critico)
        if recompensa.xp_bonus != 0:
            self.adicionar_xp_bonus(recompensa.xp_bonus)
        if recompensa.ouro_bonus != 0:
            self.adicionar_ouro_bonus(recompensa.ouro_bonus)