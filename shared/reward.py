class Recompensa:
    """
    Representa os bônus permanentes concedidos ao herói ao concluir requisitos específicos.
    Atributos não utilizados permanecem em 0 e são ignorados na aplicação.
    :param ataque: Bônus percentual de ataque. Padrão: 0.
    :param defesa: Bônus percentual de defesa. Padrão: 0.
    :param hp_max: Bônus percentual de HP máximo. Padrão: 0.
    :param chance_critico: Bônus percentual de chance de crítico. Padrão: 0.
    :param dano_critico: Bônus percentual de dano crítico. Padrão: 0.
    :param xp_bonus: Bônus adicional de XP ganho. Padrão: 0.
    :param ouro_bonus: Bônus adicional de ouro ganho. Padrão: 0.
    """
    def __init__(self, ataque = 0, defesa = 0, hp_max = 0, chance_critico = 0, dano_critico = 0, xp_bonus = 0,
                 ouro_bonus = 0):
        self.__ataque = ataque
        self.__defesa = defesa
        self.__hp_max = hp_max
        self.__chance_critico = chance_critico
        self.__dano_critico = dano_critico
        self.__xp_bonus = xp_bonus
        self.__ouro_bonus = ouro_bonus


    @property
    def ataque(self) -> int: return self.__ataque


    @property
    def defesa(self) -> int: return self.__defesa


    @property
    def hp_max(self) -> int: return self.__hp_max


    @property
    def chance_critico(self) -> float: return self.__chance_critico


    @property
    def dano_critico(self) -> float: return self.__dano_critico


    @property
    def xp_bonus(self) -> float: return self.__xp_bonus


    @property
    def ouro_bonus(self) -> float: return self.__ouro_bonus
