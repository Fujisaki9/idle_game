from utils import formatar_strings

class RequisitoMateriais:
    """
    Define um requisito de material para coleções do Codex e recipes da Forja, armazenando o nome, quantidade necessária
    e estado de conclusão.
    :param nome_material: Nome do material exigido.
    :param quantidade: Quantidade necessária do material.
    :param obtido: Indica se o requisito foi concluído. Padrão: False.
    """
    def __init__(self, nome_material, quantidade, obtido = False):
        self.nome_material = nome_material
        self.quantidade = quantidade
        self.obtido = obtido


    def __str__(self):
        return f"{formatar_strings(self.nome_material)} [{self.quantidade}] "


class Codex:
    """
    Representa uma coleção do Codex, composta por requisitos de materiais e uma recompensa permanente.
    Ao depositar todos os materiais exigidos, a coleção é concluída e os bônus são aplicados definitivamente no herói.
    :param nome_colecao: Nome identificador da coleção.
    :param requisitos: Lista de objetos RequisitoMateriais com os materiais exigidos.
    :param recompensa_colecao: Objeto Recompensa com os bônus permanentes concedidos ao concluir.
    :param conclusao: Indica se a coleção foi concluída. Padrão: False.
    """
    def __init__(self, nome_colecao, requisitos, recompensa_colecao, conclusao = False):
        self.nome_colecao = nome_colecao
        self.requisitos = requisitos
        self.recompensa_colecao = recompensa_colecao
        self.conclusao = conclusao


class Recompensa:
    """
    Representa os bônus permanentes concedidos ao herói ao concluir requisitos específicos.
    Atributos não utilizados permanecem em 0 e são ignorados na aplicação.
    :param ataque: Bônus percentual de ataque. Padrão: 0.
    :param defesa: Bônus percentual de defesa. Padrão: 0.
    :param hp_max: Bônus percentual de HP máximo. Padrão: 0.
    :param chance_critico: Bônus percentual de chance de crítico. Padrão: 0.
    :param dano_critico: Bônus percentual de dano crítico. Padrão: 0.
    :param xp_bonus: Bônus adicional de XP ganho. Padrão: 0.
    :param ouro_bonus: Bônus adicional de ouro ganho. Padrão: 0.
    """
    def __init__(self, ataque = 0, defesa = 0, hp_max = 0, chance_critico = 0, dano_critico = 0, xp_bonus = 0, ouro_bonus = 0):
        self.ataque = ataque
        self.defesa = defesa
        self.hp_max = hp_max
        self.chance_critico = chance_critico
        self.dano_critico = dano_critico
        self.xp_bonus = xp_bonus
        self.ouro_bonus = ouro_bonus


    def __str__(self):
        resultado = list()
        for k, v in self.__dict__.items():
            if v != 0:
                atributo = v * 100
                resultado.append(f"+{atributo:.0f}% {formatar_strings(k)}")
        return "\n".join(resultado)
