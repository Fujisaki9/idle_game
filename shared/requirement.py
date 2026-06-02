class RequisitoMateriais:
    """
    Define um requisito de material para coleções do Codex e recipes da Forja, armazenando o nome, quantidade necessária
    e estado de conclusão.
    :param nome_material: Nome do material exigido.
    :param quantidade: Quantidade necessária do material.
    :param obtido: Indica se o requisito foi concluído. Padrão: False.
    """
    def __init__(self, nome_material, quantidade, zona_obtencao, obtido: bool = False):
        self.__nome_material = str(nome_material)
        self.__quantidade = int(quantidade)
        self.__zona_obtencao = str(zona_obtencao)
        self.__obtido = bool(obtido)


    @property
    def nome_material(self) -> str: return self.__nome_material


    @nome_material.setter
    def nome_material(self, nome_material_novo): self.nome_material = str(nome_material_novo)


    @property
    def quantidade(self) -> int: return self.__quantidade


    @quantidade.setter
    def quantidade(self, quantidade_nova): self.__quantidade = int(quantidade_nova)


    @property
    def zona_obtencao(self) -> str: return self.__zona_obtencao


    @property
    def obtido(self) -> bool: return self.__obtido


    @obtido.setter
    def obtido(self, obtido_novo): self.__obtido = bool(obtido_novo)


    def obter(self):
        """Define o material como obtido após a quantidade necessária ser inserida."""
        self.__obtido = True


    def subtrair_materiais(self, quantidade): self.__quantidade = max(0, self.__quantidade - int(quantidade))