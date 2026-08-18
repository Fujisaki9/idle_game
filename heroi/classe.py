from entidade.base import Entidade
from entidade.equipamento import Equipamento


class Heroi(Entidade):
    """
    Representa o personagem principal do jogo.
    Herda os atributos base da classe Entidade e adiciona sistema de progressão, equipamentos e recursos.

    :param nome_personagem: Nome do herói.

    :ivar nivel_personagem: Nível atual do herói (inicia em 1).
    :ivar xp: Pontos de experiência acumulados.
    :ivar ouro: Quantidade de moedas de ouro que o herói possui.
    :ivar xp_bonus_heroi: Bônus adicional aplicado aos ganhos de experiência.
    :ivar ouro_bonus_heroi: Bônus adicional aplicado aos ganhos de ouro.
    :ivar arma: O equipamento do tipo arma atualmente equipado.
    :ivar armadura: O equipamento do tipo armadura atualmente equipado.
    :ivar acessorio: O equipamento do tipo acessório atualmente equipado.
    """

    __MULTIPLICADOR_XP = 40
    __EXPOENTE_XP = 1.2

    def __init__(self, nome_personagem: str):

        super().__init__(nome_personagem, hp=150, ataque=18, defesa=6, chance_critico=0.30, dano_critico=1.5)
        self.__nivel_personagem = 1
        self.__xp = 0
        self.__ouro = 0
        self.__xp_bonus_heroi = 0
        self.__ouro_bonus_heroi = 0
        self.__arma = Equipamento("Espada", [3, 6, 10, 15, 25, 40])
        self.__armadura = Equipamento("Armadura", [2, 4, 7, 11, 16, 22])
        self.__acessorio = Equipamento("Acessório", [20, 40, 70, 110, 160, 220])

    @property
    def nivel_personagem(self) -> int: return self.__nivel_personagem

    @nivel_personagem.setter
    def nivel_personagem(self, valor: int): self.__nivel_personagem = valor

    @property
    def xp(self) -> int: return self.__xp

    @xp.setter
    def xp(self, valor: int): self.__xp = valor

    @property
    def ouro(self) -> int: return self.__ouro

    @ouro.setter
    def ouro(self, valor: int): self.__ouro = valor

    @property
    def xp_bonus_heroi(self) -> float: return self.__xp_bonus_heroi

    @xp_bonus_heroi.setter
    def xp_bonus_heroi(self, valor: float): self.__xp_bonus_heroi = float(valor)

    @property
    def ouro_bonus_heroi(self) -> float: return self.__ouro_bonus_heroi

    @ouro_bonus_heroi.setter
    def ouro_bonus_heroi(self, valor: float): self.__ouro_bonus_heroi = float(valor)

    @property
    def arma(self) -> Equipamento: return self.__arma

    @property
    def armadura(self) -> Equipamento: return self.__armadura

    @property
    def acessorio(self) -> Equipamento: return self.__acessorio

    def aumentar_nivel(self, valor: int): self.__nivel_personagem += valor

    def calcular_xp_nivel(self) -> int:
        return round((self.__nivel_personagem ** self.__EXPOENTE_XP) * self.__MULTIPLICADOR_XP)

    def adicionar_xp(self, valor: int): self.__xp += round(valor)

    def diminuir_xp(self, valor: int): self.__xp = max(0, self.__xp - round(valor))

    def adicionar_xp_bonus(self, valor: float): self.__xp_bonus_heroi += float(valor)

    def adicionar_ouro(self, valor: int): self.__ouro += round(valor)

    def diminuir_ouro(self, valor: int): self.__ouro = max(0, self.__ouro - round(valor))

    def adicionar_ouro_bonus(self, valor: float): self.__ouro_bonus_heroi += float(valor)

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

    def aplicar_recompensas(self, valor: int):
        if valor.ataque_bonus != 0:
            self.adicionar_ataque(self.ataque * valor.ataque_bonus)
        if valor.defesa_bonus != 0:
            self.adicionar_defesa(self.defesa * valor.defesa_bonus)
        if valor.hp_max_bonus != 0:
            self.adicionar_hp_max(self.hp_max * valor.hp_max_bonus)
            self.curar_hp_total()
        if valor.chance_critico_bonus != 0:
            self.adicionar_chance_critico(self.chance_critico * valor.chance_critico_bonus)
        if valor.dano_critico_bonus != 0:
            self.adicionar_dano_critico(self.dano_critico * valor.dano_critico_bonus)
        if valor.xp_bonus != 0:
            self.adicionar_xp_bonus(valor.xp_bonus)
        if valor.ouro_bonus != 0:
            self.adicionar_ouro_bonus(valor.ouro_bonus)