from base.recompensa import Recompensa
from base.material import MaterialRequerido


class Codex:
    """
    Representa uma coleção do Codex, composta por requisitos de materiais e uma recompensa permanente.
    Ao depositar todos os materiais exigidos, a coleção é concluída e os bônus são aplicados definitivamente no herói.

    :param nome_colecao: Nome identificador da coleção.
    :param requisitos_colecao: Lista de objetos RequisitoMateriais com os materiais exigidos para a conclusão.
    :param recompensa_colecao: Objeto Recompensa com os bônus permanentes concedidos ao herói ao concluir.
    :param colecao_concluida: Indica se a coleção já foi concluída. Padrão: False.
    """
    def __init__(self, nome_colecao: str,
                 requisitos_colecao: list[MaterialRequerido],
                 recompensa_colecao: Recompensa,
                 colecao_concluida: bool = False):

        self.__nome_colecao = nome_colecao
        self.__requisitos_colecao = requisitos_colecao
        self.__recompensa_colecao = recompensa_colecao
        self.__colecao_concluida = colecao_concluida

    @property
    def nome_colecao(self) -> str:
        return self.__nome_colecao

    @property
    def requisitos_colecao(self) -> list[MaterialRequerido]:
        return self.__requisitos_colecao

    @property
    def recompensa_colecao(self) -> Recompensa:
        return self.__recompensa_colecao

    @property
    def colecao_concluida(self) -> bool:
        return self.__colecao_concluida

    @colecao_concluida.setter
    def colecao_concluida(self, valor: bool):
        self.__colecao_concluida = valor

    def concluir_colecao(self):
        self.__colecao_concluida = True