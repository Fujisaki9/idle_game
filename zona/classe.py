from copy import deepcopy
from random import choice

from entidade.inimigo import Inimigo


class Zona:
    """
    Representa uma zona do jogo contendo inimigos e um boss.
    Controla o acesso às zonas através do nível mínimo exigido e o status de conclusão de cada zona.
    :param nome_zona: Nome identificador da zona.
    :param nivel_minimo: Nível mínimo exigido para acessar a zona.
    :param lista_inimigos: Lista de objetos Inimigo presentes na zona.
    :param boss: Objeto Inimigo que representa o boss da zona.
    :param zona_concluida: Indica se o boss da zona foi derrotado. Padrão: False.
    """
    def __init__(self, nome_zona: str,
                 nivel_minimo: int,
                 lista_inimigos: list[Inimigo],
                 boss: Inimigo,
                 zona_concluida: bool = False):

        self.__nome_zona = nome_zona
        self.__nivel_minimo = nivel_minimo
        self.__lista_inimigos = lista_inimigos
        self.__boss = boss
        self.__zona_concluida = zona_concluida

    @property
    def nome_zona(self) -> str: return self.__nome_zona

    @nome_zona.setter
    def nome_zona(self, valor): self.__nome_zona = str(valor)

    @property
    def nivel_minimo(self) -> int: return self.__nivel_minimo

    @property
    def lista_inimigos(self) -> list[Inimigo]: return self.__lista_inimigos

    @property
    def boss(self) -> Inimigo: return self.__boss

    @property
    def zona_concluida(self) -> bool: return self.__zona_concluida

    @zona_concluida.setter
    def zona_concluida(self, valor): self.__zona_concluida = bool(valor)

    def concluir_zona(self): self.__zona_concluida = True

    def gerar_inimigo(self) -> Inimigo:
        inimigo = choice(self.__lista_inimigos)
        return deepcopy(inimigo)
