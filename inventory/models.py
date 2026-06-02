class Inventario:
    """
    Representa um item armazenado no inventário do herói.
    Controla a quantidade e o valor total dos materiais coletados em combate.
    :param nome_item: Nome do item armazenado.
    :param quantidade_item: Quantidade atual do item no inventário.
    :param preco_unitario: Preço de venda unitário do item.
    :param preco_total: Valor total calculado com base na quantidade.
    """
    def __init__(self, nome_item, quantidade_item, preco_unitario, preco_total):
        self.__nome_item = str(nome_item)
        self.__quantidade_item = int(quantidade_item)
        self.__preco_unitario = int(preco_unitario)
        self.__preco_total = int(preco_total)


    @property
    def nome_item(self) -> str: return self.__nome_item


    @nome_item.setter
    def nome_item(self, nome_item_novo): self.__nome_item = str(nome_item_novo)


    @property
    def quantidade_item(self) -> int: return self.__quantidade_item


    @quantidade_item.setter
    def quantidade_item(self, quantidade_item_nova): self.__quantidade_item = int(quantidade_item_nova)


    @property
    def preco_unitario(self) -> int: return self.__preco_unitario


    @preco_unitario.setter
    def preco_unitario(self, preco_unitario_novo): self.__preco_unitario = int(preco_unitario_novo)


    @property
    def preco_total(self) -> int: return self.__preco_total


    @preco_total.setter
    def preco_total(self, preco_total_novo): self.__preco_total = int(preco_total_novo)


    def subtrair_quantidade(self, valor): self.__quantidade_item = max(0, self.__quantidade_item - int(valor))


    def adicionar_quantidade(self): self.__quantidade_item += 1


    def adicionar_preco_total(self, valor): self.__preco_total += int(valor)


    def subtrair_preco_total(self, valor): self.__preco_total = max(0, self.__preco_total - int(valor))


    def calcular_preco(self, quantidade) -> int: return int(self.__preco_unitario * quantidade)
