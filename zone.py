from random import choice
import copy

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
        self.nome_zona = nome_zona
        self.nivel_minimo = nivel_minimo
        self.lista_inimigos = lista_inimigos
        self.boss = boss
        self.zona_concluida = zona_concluida


    def gerar_inimigo(self):
        """
        Sorteia um inimigo aleatório dentro de uma lista de inimigos da zona.
        Cada zona possui 10 fases, sendo 9 fases com inimigos aleatórios e a fase 10 reservada para o boss final.
        :return: Cópia de um objeto Inimigo sorteado aleatoriamente da lista.
        """
        inimigo = choice(self.lista_inimigos)
        return copy.deepcopy(inimigo)
