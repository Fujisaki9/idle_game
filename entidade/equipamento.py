class Equipamento:
    """
    Representa os equipamentos do herói (Arma, Armadura e Acessório).
    Contém o sistema de progressão de nível e raridade dos equipamentos.
    :param nome_equipamento: Nome do equipamento.
    :param bonus: Lista com os bônus de atributo por faixa de nível.
       bonus[0] -> nível 01-10
       bonus[1] -> nível 11-20
       bonus[2] -> nível 21-30
       bonus[3] -> nível 31-40
       bonus[4] -> nível 41-50
       bonus[5] -> nível 51-60
    :param raridade: Raridade do equipamento. Padrão: comum.
    :param nivel_maximo: Nível máximo do equipamento. Padrão: 30.
    """

    __MULTIPLICADOR_OURO = 30
    __QTD_FAIXAS_BONUS = 6

    def __init__(self, nome_equipamento: str,
                 bonus: list[int],
                 raridade: str = "comum",
                 nivel_maximo: int = 30):

        if len(bonus) != self.__QTD_FAIXAS_BONUS:
            raise ValueError(f"O limite máximo de bônus é {self.__QTD_FAIXAS_BONUS}. Quantidade atual: {len(bonus)}")

        self.__nome_equipamento = nome_equipamento
        self.__nivel_equipamento = 1
        self.__bonus = list(bonus)
        self.__raridade = raridade
        self.__nivel_maximo = nivel_maximo

    @property
    def nome_equipamento(self) -> str: return self.__nome_equipamento

    @nome_equipamento.setter
    def nome_equipamento(self, valor): self.__nome_equipamento = valor

    @property
    def nivel_equipamento(self) -> int: return self.__nivel_equipamento

    @nivel_equipamento.setter
    def nivel_equipamento(self, valor): self.__nivel_equipamento = valor

    @property
    def nivel_maximo(self) -> int: return self.__nivel_maximo

    @nivel_maximo.setter
    def nivel_maximo(self, valor): self.__nivel_maximo = valor

    @property
    def raridade(self) -> str: return self.__raridade

    @raridade.setter
    def raridade(self, valor): self.__raridade = valor

    def calcular_custo_upgrade(self) -> int:
        return self.__MULTIPLICADOR_OURO * self.__nivel_equipamento

    def aumentar_nivel_equip(self): self.__nivel_equipamento += 1

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

        faixas_bonus = [
            (10, self.__bonus[0]),
            (20, self.__bonus[1]),
            (30, self.__bonus[2]),
            (40, self.__bonus[3]),
            (50, self.__bonus[4]),
            (60, self.__bonus[5])
        ]
        bonus_total = 0
        nivel_anterior = 0

        for nivel_limite, faixa_bonus in faixas_bonus:

            if self.__nivel_equipamento <= nivel_limite:
                bonus_total += (self.__nivel_equipamento - nivel_anterior) * faixa_bonus
                break
            else:
                bonus_total += (nivel_limite - nivel_anterior) * faixa_bonus

            nivel_anterior = nivel_limite

        return bonus_total