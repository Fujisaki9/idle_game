class Equipamento:
    """
    Representa os equipamentos do herói (Arma, Armadura e Acessório).
    Contém o sistema de progressão de nível e raridade dos equipamentos.
    :param nome_equip: Nome do equipamento.
    :param bonus_1: Bônus de atributo por nivel (01 - 10).
    :param bonus_2: Bônus de atributo por nivel (11 - 20).
    :param bonus_3: Bônus de atributo por nivel (21 - 30).
    :param bonus_4: Bônus de atributo por nivel (31 - 40).
    :param bonus_5: Bônus de atributo por nivel (41 - 50).
    :param bonus_6: Bônus de atributo por nivel (51 - 60).
    :param raridade: Raridade do equipamento. Padrão: comum.
    :param nivel_max: Nível máximo do equipamento. Padrão: 30.
    """
    __MULTIPLICADOR_OURO = 30
    def __init__(self, nome_equip, bonus_1, bonus_2, bonus_3, bonus_4, bonus_5, bonus_6, raridade = "comum", nivel_max = 30):
        self.__nome_equip = str(nome_equip)
        self.__nivel_equip = 1
        self.__nivel_max = int(nivel_max)
        self.__bonus_1 = int(bonus_1)
        self.__bonus_2 = int(bonus_2)
        self.__bonus_3 = int(bonus_3)
        self.__bonus_4 = int(bonus_4)
        self.__bonus_5 = int(bonus_5)
        self.__bonus_6 = int(bonus_6)
        self.__raridade = str(raridade)


    @property
    def nome_equip(self) -> str: return self.__nome_equip


    @nome_equip.setter
    def nome_equip(self, nome_equip_novo): self.__nome_equip = str(nome_equip_novo)


    @property
    def nivel_equip(self) -> int: return self.__nivel_equip


    @nivel_equip.setter
    def nivel_equip(self, nivel_equip_novo): self.__nivel_equip = int(nivel_equip_novo)


    @property
    def nivel_max(self) -> int: return self.__nivel_max


    @nivel_max.setter
    def nivel_max(self, nivel_max_novo): self.__nivel_max = int(nivel_max_novo)


    @property
    def raridade(self) -> str: return self.__raridade


    @raridade.setter
    def raridade(self, raridade_nova): self.__raridade = str(raridade_nova)


    def calcular_custo_upgrade(self) -> int:
        """
        Calcula o custo de upgrade do equipamento baseado no nível atual.
        :return: Valor do upgrade.
        """
        return self.__MULTIPLICADOR_OURO * self.__nivel_equip


    def aumentar_nivel_equip(self): self.__nivel_equip += 1


    def calcular_bonus_atual(self) -> int:
        """
        Calcula os ganhos de atributos baseado no nível do equipamento.
        A progressão de atributos segue faixas de níveis específicas para os três status principais:
        ataque(arma), defesa(armadura), vida(acessório).

        | Faixa de nível | Ataque | Defesa | Vida |

        | Nível 01 a 10  | +3     | +2     | +20  |
        | Nível 11 a 20  | +6     | +4     | +40  |
        | Nível 21 a 30  | +10    | +7     | +70  |
        | Nível 31 a 40  | +15    | +11    | +110 |
        | Nível 41 a 50  | +25    | +16    | +160 |
        | Nível 51 a 60  | +40    | +22    | +220 |

        :return: Valor total de atributo ganho.
        """

        faixas = [
            (10, self.__bonus_1),
            (20, self.__bonus_2),
            (30, self.__bonus_3),
            (40, self.__bonus_4),
            (50, self.__bonus_5),
            (60, self.__bonus_6)
        ]
        total = 0
        nivel_anterior = 0
        for limite, bonus in faixas:
            if self.__nivel_equip <= limite:
                total += (self.__nivel_equip - nivel_anterior) * bonus
                break
            else:
                total += (limite - nivel_anterior) * bonus
            nivel_anterior = limite
        return total