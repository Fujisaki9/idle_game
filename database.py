from zone import Zona
from characters import Inimigo
from inventory import Item


def criar_zonas() -> list:
    """
    Cria os objetos da classe Zona, da classe Inimigo, da classe Item.
    Configura todas as zonas do jogo, incluindo os inimigos, bosses e seus respectivos drops.
    :return: Lista de objetos da classe Zona ordenados por dificuldade crescente.
    """
    # Zona 1 -> Floresta Sombria (nível mínimo: 1)

    # Goblin/Lobo: Drops
    pele_goblin = Item("Pele de Goblin", 1, 0.60, 5)
    dente_goblin = Item("Dente de Goblin", 1, 0.40, 8)
    pele_lobo = Item("Pele de Lobo", 1, 0.60, 6)
    garra_lobo = Item("Garra de Lobo", 1, 0.40, 10)

    # Boss - Troll da Floresta: Drops
    pedra_troll = Item("Pedra do Troll", 1, 0.80, 40)
    coracao_troll = Item("Coracao do Troll", 1, 0.50, 70)
    essencia_troll = Item("Essencia do Troll", 1, 0.30, 120)

    goblin = Inimigo("Goblin", 30, 8, 2, 20, 10,
                     [pele_goblin, dente_goblin])
    lobo = Inimigo("Lobo Cinzento", 30, 8, 2, 20, 10,
                   [pele_lobo, garra_lobo])
    boss_floresta = Inimigo("Troll da Floresta", 120, 15, 5, 100, 60,
                            [pedra_troll, coracao_troll, essencia_troll])

    # Zona 2 -> Caverna do Eco (nível mínimo: 5)

    # Morcego/Esqueleto: Drops
    asa_morcego = Item("Asa de Morcego", 1, 0.60, 10)
    sangue_morcego = Item("Sangue de Morcego", 1, 0.40, 14)
    osso_esqueleto = Item("Osso de Esqueleto", 1, 0.60, 12)
    caveira_esqueleto = Item("Caveira de Esqueleto", 1, 0.40, 18)

    # Boss - Golem de Pedra: Drops
    nucleo_golem = Item("Nucleo do Golem", 1, 0.80, 80)
    fragmento_golem = Item("Fragmento de Pedra Magica", 1, 0.50, 120)
    essencia_golem = Item("Essencia do Golem", 1, 0.30, 200)

    morcego = Inimigo("Morcego Gigante", 55, 14, 4, 40, 15,
                      [asa_morcego, sangue_morcego])
    esqueleto = Inimigo("Esqueleto Guerreiro", 65, 16, 6, 50, 20,
                        [osso_esqueleto, caveira_esqueleto])
    boss_caverna = Inimigo("Golem de Pedra", 200, 25, 15, 180, 100,
                           [nucleo_golem, fragmento_golem, essencia_golem])

    # Zona 3 -> Ruínas Amaldiçoadas (nível mínimo: 10)

    # Fantasma/Zumbi: Drops
    ectoplasma = Item("Ectoplasma", 1, 0.60, 18)
    essencia_fantasma = Item("Essencia Fantasmagorica", 1, 0.40, 25)
    carne_zumbi = Item("Carne Putrefata", 1, 0.60, 16)
    osso_amaldicoado = Item("Osso Amaldicoado", 1, 0.40, 22)

    # Boss - Necromante: Drops
    grimorio = Item("Grimorio Sombrio", 1, 0.80, 150)
    alma_necromante = Item("Alma do Necromante", 1, 0.50, 220)
    essencia_morte = Item("Essencia da Morte", 1, 0.30, 350)

    fantasma = Inimigo("Fantasma", 80, 22, 8, 70, 30,
                       [ectoplasma, essencia_fantasma])
    zumbi = Inimigo("Zumbi Guerreiro", 95, 20, 10, 80, 35,
                    [carne_zumbi, osso_amaldicoado])
    boss_ruinas = Inimigo("Necromante", 280, 35, 12, 300, 180,
                          [grimorio, alma_necromante, essencia_morte])

    # Zona 4 -> Montanha de Fogo (nível mínimo: 18)

    # Elemental/Ogro: Drops
    cristal_fogo = Item("Cristal de Fogo", 1, 0.60, 28)
    cinza_elemental = Item("Cinza Elemental", 1, 0.40, 35)
    dente_ogro = Item("Dente de Ogro", 1, 0.60, 25)
    pele_ogro = Item("Pele de Ogro Vulcanico", 1, 0.40, 32)

    # Boss - Hidra de Lava: Drops
    escama_hidra = Item("Escama de Hidra", 1, 0.80, 200)
    veneno_hidra = Item("Veneno de Hidra", 1, 0.50, 300)
    coracao_hidra = Item("Coracao de Lava", 1, 0.30, 500)

    elemental = Inimigo("Elemental de Fogo", 120, 32, 14, 110, 55,
                        [cristal_fogo, cinza_elemental])
    ogro = Inimigo("Ogro Vulcanico", 140, 30, 18, 120, 60,
                   [dente_ogro, pele_ogro])
    boss_montanha = Inimigo("Hidra de Lava", 420, 48, 22, 500, 300,
                            [escama_hidra, veneno_hidra, coracao_hidra])

    # Zona 5 -> Torre do Dragão (nível mínimo: 28)

    # Cavaleiro Negro/Wyvern: Drops
    armadura_negra = Item("Fragmento de Armadura Negra", 1, 0.60, 40)
    alma_cavaleiro = Item("Alma do Cavaleiro", 1, 0.40, 55)
    escama_wyvern = Item("Escama de Wyvern", 1, 0.60, 45)
    garra_wyvern = Item("Garra de Wyvern", 1, 0.40, 60)

    # Boss - Dragão Ancião: Drops
    escama_dragao = Item("Escama do Dragao Anciao", 1, 0.80, 400)
    dente_dragao = Item("Dente do Dragao Anciao", 1, 0.50, 600)
    coracao_dragao = Item("Coracao de Dragao", 1, 0.30, 1000)
    cavaleiro = Inimigo("Cavaleiro Negro", 180, 42, 25, 160, 90,
                        [armadura_negra, alma_cavaleiro])
    wyvern = Inimigo("Wyvern", 200, 45, 20, 180, 100,
                     [escama_wyvern, garra_wyvern])
    boss_torre = Inimigo("Dragao Anciao", 800, 70, 35, 1000, 600,
                         [escama_dragao, dente_dragao, coracao_dragao])

    # Zona 6 -> Abismo Aquático (nível mínimo: 38)

    # Serpente/Tritão: Drops
    escama_serpente = Item("Escama de Serpente", 1, 0.60, 55)
    veneno_serpente = Item("Veneno de Serpente", 1, 0.40, 70)
    tridente_fragmento = Item("Fragmento de Tridente", 1, 0.60, 60)
    escama_tritao = Item("Escama de Tritao", 1, 0.40, 75)

    # Boss - Kraken: Drops
    tentaculo_kraken = Item("Tentaculo do Kraken", 1, 0.80, 600)
    olho_kraken = Item("Olho do Kraken", 1, 0.50, 900)
    essencia_kraken = Item("Essencia Abissal", 1, 0.30, 1400)

    serpente = Inimigo("Serpente Marinha", 260, 55, 28, 220, 120,
                            [escama_serpente, veneno_serpente])
    tritao = Inimigo("Tritao Guerreiro", 280, 58, 30, 240, 130,
                     [tridente_fragmento, escama_tritao] )
    boss_abismo = Inimigo("Kraken", 1100, 88, 45, 1400, 850,
                          [tentaculo_kraken, olho_kraken, essencia_kraken])

    # Zona 7 -> Floresta Amaldiçoada (nível mínimo: 50)

    # Árvore Sombria/Espectro: Drops
    casca_sombria = Item("Casca Sombria", 1, 0.60, 70)
    seiva_sombria = Item("Seiva Sombria", 1, 0.40, 90)
    essencia_espectro = Item("Essencia do Espectro", 1, 0.60, 75)
    fragmento_espectro = Item("Fragmento Espectral", 1, 0.40, 95)

    # Boss - Rei dos Espectros: Drops
    coroa_espectro = Item("Coroa do Rei Espectro", 1, 0.80, 800)
    alma_rei = Item("Alma do Rei", 1, 0.50, 1200)
    essencia_real = Item("Essencia Real Espectral", 1, 0.30, 1900)

    arvore = Inimigo("Arvore Sombria", 340, 68, 35, 300, 160,
                     [casca_sombria, seiva_sombria])
    espectro = Inimigo("Espectro Antigo", 360, 72, 33, 320, 170,
                       [essencia_espectro, fragmento_espectro])
    boss_floresta_2 = Inimigo("Rei dos Espectros", 1400, 105, 55, 1900, 1100,
                              [coroa_espectro, alma_rei, essencia_real])

    # Zona 8 -> Templo do Trovão (nível mínimo: 65)

    # Golem Elétrico/Guardião do Trovão: Drops
    nucleo_eletrico = Item("Nucleo Eletrico", 1, 0.60, 90)
    fragmento_trovao = Item("Fragmento do Trovao", 1, 0.40, 115)
    essencia_trovao = Item("Essencia do Trovao", 1, 0.60, 95)
    cristal_trovao = Item("Cristal do Trovao", 1, 0.40, 120)

    # Boss - Titã do Trovão: Drops
    martelo_tita = Item("Fragmento do Martelo do Tita", 1, 0.80, 1000)
    alma_tita = Item("Alma do Tita", 1, 0.50, 1500)
    essencia_tita = Item("Essencia do Trovao Primordial", 1, 0.30, 2500)

    golem_eletrico = Inimigo("Golem Eletrico", 440, 85, 42, 400, 210,
                             [nucleo_eletrico, fragmento_trovao])
    guardiao = Inimigo("Guardiao do Trovao", 460, 90, 45, 420, 220,
                       [essencia_trovao, cristal_trovao])
    boss_templo = Inimigo("Tita do Trovao", 1800, 130, 68, 2500, 1500,
                          [martelo_tita, alma_tita, essencia_tita])

    # Zona 9 -> Portal do Caos (nível mínimo: 80)

    # Demônio do Caos/Guardião Sombrio: Drops
    cristal_caos = Item("Cristal do Caos", 1, 0.60, 120)
    essencia_demonio = Item("Essencia Demoníaca", 1, 0.40, 150)
    fragmento_sombrio = Item("Fragmento Sombrio", 1, 0.60, 130)
    alma_sombria = Item("Alma Sombria", 1, 0.40, 160)

    # Boss - Lorde do Caos: Drops
    coroa_caos = Item("Coroa do Caos", 1, 0.80, 1500)
    alma_lorde = Item("Alma do Lorde do Caos", 1, 0.50, 2200)
    essencia_caos = Item("Essencia do Caos Primordial", 1, 0.30, 3200)

    demonios = Inimigo("Demonio do Caos", 560, 105, 52, 520, 280,
                       [cristal_caos, essencia_demonio])
    guardiao_sombrio = Inimigo("Guardiao Sombrio", 580, 110, 55, 540, 290,
                               [fragmento_sombrio, alma_sombria])
    boss_caos = Inimigo("Lorde do Caos", 2200, 160, 82, 3200, 2000,
                        [coroa_caos, alma_lorde, essencia_caos])

    return [
        Zona("Floresta Sombria", 1, [goblin, lobo], boss = boss_floresta),
        Zona("Caverna do Eco", 5, [morcego, esqueleto], boss = boss_caverna),
        Zona("Ruínas Amaldiçoadas", 10, [fantasma, zumbi], boss = boss_ruinas),
        Zona("Montanha de Fogo", 18, [elemental, ogro], boss = boss_montanha),
        Zona("Torre do Dragão", 28, [cavaleiro, wyvern], boss = boss_torre),
        Zona("Abismo Aquático", 38, [serpente, tritao], boss = boss_abismo),
        Zona("Floresta Amaldiçoada", 50, [arvore, espectro], boss = boss_floresta_2),
        Zona("Templo do Trovão", 65, [golem_eletrico, guardiao], boss = boss_templo),
        Zona("Portal do Caos", 80, [demonios, guardiao_sombrio], boss = boss_caos)
    ]