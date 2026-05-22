class Equipamento:
    """
    Representa os equipamentos do herói (Arma, Armadura e Acessório).
    Contém o sistema de progressão de nível e raridade dos equipamentos.
    :param nome: Nome do equipamento.
    :param bonus_1: Bônus de atributo por nivel (01 - 10).
    :param bonus_2: Bônus de atributo por nivel (11 - 20).
    :param bonus_3: Bônus de atributo por nivel (21 - 30).
    :param bonus_4: Bônus de atributo por nivel (31 - 40).
    :param bonus_5: Bônus de atributo por nivel (41 - 50).
    :param bonus_6: Bônus de atributo por nivel (51 - 60).
    :param raridade: Raridade do equipamento. Padrão: comum.
    :param nivel_max: Nível máximo do equipamento. Padrão: 30.
    """
    def __init__(self, nome, bonus_1, bonus_2, bonus_3, bonus_4, bonus_5, bonus_6, raridade ="comum", nivel_max = 30):
        self.nome = nome
        self.nivel = 1
        self.nivel_max = nivel_max
        self.bonus_1 = bonus_1
        self.bonus_2 = bonus_2
        self.bonus_3 = bonus_3
        self.bonus_4 = bonus_4
        self.bonus_5 = bonus_5
        self.bonus_6 = bonus_6
        self.raridade = raridade


    def calcular_custo_upgrade(self) -> int:
        """
        Calcula o custo de upgrade do equipamento baseado no nível atual.
        :return: Valor do upgrade.
        """
        return 30 * self.nivel


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
            (10, self.bonus_1),
            (20, self.bonus_2),
            (30, self.bonus_3),
            (40, self.bonus_4),
            (50, self.bonus_5),
            (60, self.bonus_6)
        ]
        total = 0
        nivel_anterior = 0
        for limite, bonus in faixas:
            if self.nivel <= limite:
                total += (self.nivel - nivel_anterior) * bonus
                break
            else:
                total += (limite - nivel_anterior) * bonus
            nivel_anterior = limite
        return total