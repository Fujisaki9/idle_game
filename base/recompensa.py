class Recompensa:
    """
    Representa os bônus permanentes concedidos ao herói ao concluir requisitos específicos.
    Atributos não utilizados permanecem em 0 e são ignorados na aplicação.
    :param ataque_bonus: Bônus percentual de ataque. Padrão: 0.
    :param defesa_bonus: Bônus percentual de defesa. Padrão: 0.
    :param hp_max_bonus: Bônus percentual de HP máximo. Padrão: 0.
    :param chance_critico_bonus: Bônus percentual de chance de crítico. Padrão: 0.
    :param dano_critico_bonus: Bônus percentual de dano crítico. Padrão: 0.
    :param xp_bonus: Bônus adicional de XP ganho. Padrão: 0.
    :param ouro_bonus: Bônus adicional de ouro ganho. Padrão: 0.
    """
    def __init__(self, ataque_bonus: int = 0,
                 defesa_bonus: int = 0,
                 hp_max_bonus: int = 0,
                 chance_critico_bonus: float = 0,
                 dano_critico_bonus: float = 0,
                 xp_bonus: float = 0,
                 ouro_bonus: float = 0):

        self.__ataque_bonus = ataque_bonus
        self.__defesa_bonus = defesa_bonus
        self.__hp_max_bonus = hp_max_bonus
        self.__chance_critico_bonus = chance_critico_bonus
        self.__dano_critico_bonus = dano_critico_bonus
        self.__xp_bonus = xp_bonus
        self.__ouro_bonus = ouro_bonus

    @property
    def ataque_bonus(self) -> int: return self.__ataque_bonus

    @property
    def defesa_bonus(self) -> int: return self.__defesa_bonus

    @property
    def hp_max_bonus(self) -> int: return self.__hp_max_bonus

    @property
    def chance_critico_bonus(self) -> float: return self.__chance_critico_bonus

    @property
    def dano_critico_bonus(self) -> float: return self.__dano_critico_bonus

    @property
    def xp_bonus(self) -> float: return self.__xp_bonus

    @property
    def ouro_bonus(self) -> float: return self.__ouro_bonus
