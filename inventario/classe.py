class Inventario:
    """Representa e gerencia um item armazenado no inventário do herói.

    Esta classe controla a quantidade disponível de um material coletado em combate,
    seu preço unitário e o valor total acumulado.

    :param nome_item_inventario: O nome descritivo do item.
    :param quantidade_item: A quantidade atual do item disponível no inventário.
    :param preco_unitario: O valor de uma única unidade do item.
    :param preco_total: O valor acumulado total correspondente a este item.
"""
    def __init__(self, nome_item_inventario: str,
                 quantidade_item: int,
                 preco_unitario: int,
                 preco_total: int):

        self.__nome_item_inventario = nome_item_inventario
        self.__quantidade_item = quantidade_item
        self.__preco_unitario = preco_unitario
        self.__preco_total = preco_total

    @property
    def nome_item_inventario(self) -> str: return self.__nome_item_inventario

    @property
    def quantidade_item(self) -> int: return self.__quantidade_item

    @property
    def preco_unitario(self) -> int: return self.__preco_unitario

    @property
    def preco_total(self) -> int: return self.__preco_total

    def subtrair_quantidade(self, valor): self.__quantidade_item = max(0, self.__quantidade_item - valor)

    def adicionar_quantidade(self): self.__quantidade_item += 1

    def adicionar_preco_total(self, valor): self.__preco_total += valor

    def subtrair_preco_total(self, valor): self.__preco_total = max(0, self.__preco_total - valor)

    def calcular_preco(self, valor) -> int: return self.__preco_unitario * valor
