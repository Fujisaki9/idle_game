from copy import deepcopy
from random import choice

from shared.enemy import Inimigo


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
    def __init__(self, nome_zona, nivel_minimo, lista_inimigos, boss, zona_concluida: bool = False):
        self.__nome_zona = str(nome_zona)
        self.__nivel_minimo = int(nivel_minimo)
        self.__lista_inimigos = lista_inimigos
        self.__boss = boss
        self.__zona_concluida = bool(zona_concluida)


    @property
    def nome_zona(self) -> str: return self.__nome_zona


    @nome_zona.setter
    def nome_zona(self, nome_zona_novo): self.__nome_zona = str(nome_zona_novo)


    @property
    def nivel_minimo(self) -> int: return self.__nivel_minimo


    @property
    def lista_inimigos(self) -> list[Inimigo]: return self.__lista_inimigos


    @property
    def boss(self) -> Inimigo: return self.__boss


    @property
    def zona_concluida(self) -> bool: return self.__zona_concluida


    @zona_concluida.setter
    def zona_concluida(self, zona_concluida_nova): self.__zona_concluida = bool(zona_concluida_nova)


    def concluir_zona(self):
        """Define a zona como concluída após o boss ser derrotado."""
        self.__zona_concluida = True


    def gerar_inimigo(self) -> Inimigo:
        """
        Sorteia um inimigo aleatório dentro de uma lista de inimigos da zona.
        Cada zona possui 10 fases, sendo 9 fases com inimigos aleatórios e a fase 10 reservada para o boss final.
        :return: Cópia de um objeto Inimigo sorteado aleatoriamente da lista.
        """
        inimigo = choice(self.__lista_inimigos)
        return deepcopy(inimigo)
