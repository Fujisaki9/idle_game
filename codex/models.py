from shared.reward import Recompensa
from shared.requirement import RequisitoMateriais


class Codex:
    """
    Representa uma coleção do Codex, composta por requisitos de materiais e uma recompensa permanente.
    Ao depositar todos os materiais exigidos, a coleção é concluída e os bônus são aplicados definitivamente no herói.
    :param nome_colecao: Nome identificador da coleção.
    :param requisitos: Lista de objetos RequisitoMateriais com os materiais exigidos.
    :param recompensa_colecao: Objeto Recompensa com os bônus permanentes concedidos ao concluir.
    :param conclusao: Indica se a coleção foi concluída. Padrão: False.
    """
    def __init__(self, nome_colecao, requisitos: list, recompensa_colecao, conclusao: bool = False):
        self.__nome_colecao = str(nome_colecao)
        self.__requisitos = list(requisitos)
        self.__recompensa_colecao = recompensa_colecao
        self.__conclusao = bool(conclusao)


    @property
    def nome_colecao(self) -> str: return self.__nome_colecao


    @nome_colecao.setter
    def nome_colecao(self, nome_colecao_novo): self.__nome_colecao = str(nome_colecao_novo)


    @property
    def requisitos(self) -> list[RequisitoMateriais]: return self.__requisitos


    @property
    def recompensa_colecao(self) -> Recompensa: return self.__recompensa_colecao


    @property
    def conclusao(self) -> bool: return self.__conclusao


    @conclusao.setter
    def conclusao(self, conclusao_nova): self.__conclusao = bool(conclusao_nova)


    def concluir(self):
        """Define a coleção como concluída após os requisitos terem sido completados."""
        self.__conclusao = True