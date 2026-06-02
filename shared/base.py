from abc import ABC
from random import random, randint


class Entidade(ABC):
    """
    Classe base para todos os personagens do jogo.
    Todos os atributos são privados e acessados via getters e setters.
    :param nome: Nome do objeto.
    :param hp: HP inicial e máximo.
    :param ataque: Valor de ataque.
    :param defesa: Valor de defesa.
    :param chance_critico: Probabilidade de acerto crítico entre 0 e 1.
    :param dano_critico: Multiplicador de dano aplicado em acertos críticos.
    """
    def __init__(self, nome, hp, ataque, defesa, chance_critico, dano_critico):
        self.__nome = str(nome)
        self.__hp_max = int(hp)
        self.__hp = int(hp)
        self.__ataque = int(ataque)
        self.__defesa = int(defesa)
        self.__chance_critico = float(chance_critico)
        self.__dano_critico = float(dano_critico)


    @property
    def nome(self) -> str: return self.__nome


    @nome.setter
    def nome(self, valor):
        """
        Define o nome do personagem, validando se o valor não está vazio.
        :param valor: Nome do personagem definido pelo jogador.
        """
        if len(valor) > 0:
            self.__nome = valor
        else:
            print("ERRO: Você não digitou um nome para seu personagem!")


    @property
    def hp_max(self) -> int: return self.__hp_max


    @hp_max.setter
    def hp_max(self, hp_max_novo): self.__hp_max = int(hp_max_novo)


    @property
    def hp(self) -> int: return self.__hp


    @hp.setter
    def hp(self, hp_novo): self.__hp = int(hp_novo)


    @property
    def ataque(self) -> int: return self.__ataque


    @ataque.setter
    def ataque(self, ataque_novo): self.__ataque = int(ataque_novo)


    @property
    def defesa(self) -> int: return self.__defesa


    @defesa.setter
    def defesa(self, defesa_nova): self.__defesa = int(defesa_nova)


    @property
    def chance_critico(self) -> float: return self.__chance_critico


    @chance_critico.setter
    def chance_critico(self, chance_critico_nova): self.__chance_critico = float(chance_critico_nova)


    @property
    def dano_critico(self) -> float: return self.__dano_critico


    @dano_critico.setter
    def dano_critico(self, dano_critico_novo): self.__dano_critico = float(dano_critico_novo)


    def adicionar_ataque(self, valor): self.__ataque += int(valor)


    def adicionar_defesa(self, valor): self.__defesa += int(valor)


    def adicionar_hp_max(self, valor):
        self.__hp_max += int(valor)
        self.__hp += int(valor)


    def encher_hp(self): self.__hp = self.__hp_max


    def subtrair_hp(self, valor): self.__hp = max(0, self.__hp - int(valor))


    def curar_hp(self, percentual):
        """
        Define a quantidade de HP recuperada pelo usuário após o término do combate.
        :param percentual: Porcentagem de recuperação de HP entre 0 e 1. Ex: 0.3 (30%)
        :return: None
        """
        cura = int(self.__hp_max * percentual)
        self.__hp = min(self.__hp_max, self.__hp + cura)


    def adicionar_chance_critico(self, valor): self.__chance_critico += float(valor)


    def acertar_critico(self) -> bool:
        """
        Define se o ataque do objeto será crítico ou não.
        :return: True se for crítico ou False caso contrário.
        """
        critico = random()
        if critico <= self.__chance_critico:
            return True
        return False


    def adicionar_dano_critico(self, valor): self.__dano_critico += float(valor)


    def calcular_dano_critico(self) -> str:
        """
        Efetua o cálculo de dano crítico.
        :return: Dano crítico calculado com variação de ±10% sobre o ataque multiplicado pelo modificador de dano.
        crítico.
        """
        dano_critico = int(self.__ataque * self.__dano_critico)
        return randint(int(dano_critico * 0.9), int(dano_critico * 1.1))


    def calcular_dano_normal(self) -> int:
        """
        Efetua o cálculo de dano normal.
        :return: Dano calculado com variação de ±10% sobre o ataque multiplicado pelo modificador de dano.
        """
        return randint(int(self.__ataque * 0.9), int(self.__ataque * 1.1))


    def verificar_vida(self) -> bool:
        """
        Verifica se o herói/inimigo está vivo ou morto.
        :return: hp > 0 (True), hp <= 0 (False)
        """
        return self.__hp > 0
