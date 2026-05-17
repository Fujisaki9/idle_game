class Entidade:
    """
    Classe base para todos os personagens do jogo.
    Define os atributos fundamentais de combate compartilhados entre o herói e os inimigos.

    """
    def __init__(self, nome, hp, ataque, defesa):
        self.nome = nome
        self.hp_max = hp
        self.hp = hp
        self.ataque = ataque
        self.defesa = defesa


    def verificar_vida(self) -> bool:
        """
        Verifica se o herói/inimigo está vivo ou morto.
        :return: hp > 0 (True), hp <= 0 (False)
        """
        return self.hp > 0
