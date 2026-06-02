class Item:
    """
    Representa os itens dropados pelos inimigos durante o combate.
    Define o nome, quantidade, chance de drop e preço de venda de cada material.
    :param nome: Nome do item.
    :param quantidade_drop: Quantidade dropada por combate.
    :param chance_drop: Probabilidade de drop entre 0 e 1.
    :param valor_item: Preço de venda unitário do item.
    """
    def __init__(self, nome, quantidade_drop, chance_drop, valor_item):
        self.__nome = str(nome)
        self.__quantidade_drop = int(quantidade_drop)
        self.__chance_drop = float(chance_drop)
        self.__valor_item = int(valor_item)


    @property
    def nome(self) -> str: return self.__nome


    @property
    def quantidade_drop(self) -> int: return self.__quantidade_drop


    @property
    def chance_drop(self) -> float: return self.__chance_drop


    @property
    def valor_item(self) -> int: return self.__valor_item