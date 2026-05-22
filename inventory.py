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
        self.nome_item = nome_item
        self.quantidade_item = quantidade_item
        self.preco_unitario = preco_unitario
        self.preco_total = preco_total


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
        self.nome = nome
        self.quantidade_drop = quantidade_drop
        self.chance_drop = chance_drop
        self.valor_item = valor_item

