from shared.requirement import RequisitoMateriais


class Recipe(RequisitoMateriais):

    def __init__(self, nome_material, quantidade, zona_obtencao, obtido: bool = False):
        super().__init__(nome_material, quantidade, zona_obtencao, obtido)
