from abc import ABC

class Entidade(ABC):
    """
    Classe base para todos os personagens do jogo.
    Define os atributos fundamentais de combate compartilhados entre o herói e os inimigos.
    :param nome: Nome do objeto.
    :param hp: HP inicial e máximo.
    :param ataque: Valor de ataque.
    :param defesa: Valor de defesa.
    :param chance_critico: Probabilidade de acerto crítico entre 0 e 1.
    :param dano_critico: Multiplicador de dano aplicado em acertos críticos.
    """
    def __init__(self, nome, hp, ataque, defesa, chance_critico, dano_critico):
        self.nome = nome
        self.hp_max = hp
        self.hp = hp
        self.ataque = ataque
        self.defesa = defesa
        self.chance_critico = chance_critico
        self.dano_critico = dano_critico


    def verificar_vida(self) -> bool:
        """
        Verifica se o herói/inimigo está vivo ou morto.
        :return: hp > 0 (True), hp <= 0 (False)
        """
        return self.hp > 0
