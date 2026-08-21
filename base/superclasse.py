from random import random, randint
from rich import print as rprint


class Entidade:
    """
    Classe base para todos os personagens do jogo.
    Todos os atributos são privados e acessados via getters e setters.
    :param nome_personagem: Nome do objeto.
    :param hp: HP inicial e máximo.
    :param ataque: Valor de ataque.
    :param defesa: Valor de defesa.
    :param chance_critico: Probabilidade de acerto crítico entre 0 e 1.
    :param dano_critico: Multiplicador de dano aplicado em acertos críticos.
    """

    __MULTIPLICADOR_CURA = 0.3

    def __init__(self, nome_personagem: str,
                 hp: int,
                 ataque: int,
                 defesa: int,
                 chance_critico: float,
                 dano_critico: float):

        self.__nome_personagem = nome_personagem
        self.__hp_max = hp
        self.__hp = hp
        self.__ataque = ataque
        self.__defesa = defesa
        self.__chance_critico = chance_critico
        self.__dano_critico = dano_critico

    @property
    def nome_personagem(self) -> str: return self.__nome_personagem

    @nome_personagem.setter
    def nome_personagem(self, valor: str):
        if len(valor) > 0:
            self.__nome_personagem = valor
        else:
            rprint("[bold red]ERRO: Digite um nome para seu personagem![/]")

    @property
    def hp_max(self) -> int: return self.__hp_max

    @hp_max.setter
    def hp_max(self, valor: int | float): self.__hp_max = round(valor)

    @property
    def hp(self) -> int: return self.__hp

    @hp.setter
    def hp(self, valor: int | float): self.__hp = round(valor)

    @property
    def ataque(self) -> int: return self.__ataque

    @ataque.setter
    def ataque(self, valor: int | float): self.__ataque = round(valor)

    @property
    def defesa(self) -> int: return self.__defesa

    @defesa.setter
    def defesa(self, valor: int | float): self.__defesa = round(valor)

    @property
    def chance_critico(self) -> float: return self.__chance_critico

    @chance_critico.setter
    def chance_critico(self, valor: float): self.__chance_critico = float(valor)

    @property
    def dano_critico(self) -> float: return self.__dano_critico

    @dano_critico.setter
    def dano_critico(self, valor: float): self.__dano_critico = float(valor)

    def adicionar_ataque(self, valor: int | float): self.__ataque += round(valor)

    def adicionar_defesa(self, valor: int | float): self.__defesa += round(valor)

    def adicionar_hp_max(self, valor: int | float):
        self.__hp_max += round(valor)
        self.__hp += round(valor)

    def curar_hp_total(self): self.__hp = self.__hp_max

    def subtrair_hp(self, valor: int | float): self.__hp = max(0, self.__hp - round(valor))

    def curar_hp(self):
        cura = round(self.__hp_max * self.__MULTIPLICADOR_CURA)
        self.__hp = min(self.__hp_max, self.__hp + cura)

    def adicionar_chance_critico(self, valor: float): self.__chance_critico += float(valor)

    def acertar_critico(self) -> bool:
        critico = random()

        if critico <= self.__chance_critico:
            return True
        return False

    def adicionar_dano_critico(self, valor: float): self.__dano_critico += float(valor)

    def calcular_dano_critico(self) -> int:
        dano_critico = self.__ataque * self.__dano_critico
        dano_minimo = round(dano_critico * 0.9)
        dano_maximo = round(dano_critico * 1.1)
        return randint(dano_minimo, dano_maximo)

    def calcular_dano_normal(self) -> int:
        dano_minimo = round(self.__ataque * 0.9)
        dano_maximo = round(self.__ataque * 1.1)
        return randint(dano_minimo, dano_maximo)

    def verificar_vida(self) -> bool:
        return self.__hp > 0
