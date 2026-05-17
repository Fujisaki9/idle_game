class Inventario:
    """
    Representa um item armazenado no inventário do herói.
    Controla a quantidade e o valor total dos materiais coletados em combate.
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
    """
    def __init__(self, nome, quantidade_drop, chance_drop, valor_item):
        self.nome = nome
        self.quantidade_drop = quantidade_drop
        self.chance_drop = chance_drop
        self.valor_item = valor_item

