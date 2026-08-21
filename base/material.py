class MaterialRequerido:
    """
    Define um requisito de material para coleções do Codex e recipes da Forja, armazenando o nome, quantidade necessária
    e estado de conclusão.
    :param nome_material: Nome do material exigido.
    :param quantidade_exigida: Quantidade necessária do material.
    :param material_obtido: Indica se o requisito foi concluído. Padrão: False.
    """
    def __init__(self, nome_material: str,
                 quantidade_exigida: int,
                 zona_obtencao: str,
                 material_obtido: bool = False):

        self.__nome_material = nome_material
        self.__quantidade_exigida = quantidade_exigida
        self.__zona_obtencao = zona_obtencao
        self.__material_obtido = material_obtido

    @property
    def nome_material(self) -> str: return self.__nome_material

    @nome_material.setter
    def nome_material(self, valor: str): self.__nome_material = valor

    @property
    def quantidade_exigida(self) -> int: return self.__quantidade_exigida

    @quantidade_exigida.setter
    def quantidade_exigida(self, valor: int): self.__quantidade_exigida = valor

    @property
    def zona_obtencao(self) -> str: return self.__zona_obtencao

    @property
    def material_obtido(self) -> bool: return self.__material_obtido

    @material_obtido.setter
    def material_obtido(self, valor: bool): self.__material_obtido = valor

    def coleta_concluida(self): self.__material_obtido = True

    def subtrair_materiais(self, valor: int): self.__quantidade_exigida = max(0, self.__quantidade_exigida - valor)