from zone import Zona
from crafting import Codex, RequisitoMateriais, Recompensa
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
    essencia_demonio = Item("Essencia Demoniaca", 1, 0.40, 150)
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


def criar_codex() -> list:
    """
    Cria os objetos da classe Codex com seus requisitos e recompensas.
    :return: Lista de objetos da classe Codex.
    """
    instinto_1 = RequisitoMateriais("pele_de_lobo", 20)
    instinto_2 = RequisitoMateriais("garra_de_lobo", 15)
    instinto_3 = RequisitoMateriais("pele_de_goblin", 20)

    sangue_1 = RequisitoMateriais("sangue_de_morcego", 25)
    sangue_2 = RequisitoMateriais("asa_de_morcego", 20)
    sangue_3 = RequisitoMateriais("caveira_de_esqueleto", 15)

    muralha_1 = RequisitoMateriais("pedra_do_troll", 12)
    muralha_2 = RequisitoMateriais("osso_de_esqueleto", 30)
    muralha_3 = RequisitoMateriais("nucleo_do_golem", 8)

    presas_1 = RequisitoMateriais("dente_de_goblin", 25)
    presas_2 = RequisitoMateriais("garra_de_lobo", 20)
    presas_3 = RequisitoMateriais("fragmento_de_pedra_magica", 10)

    essencia_1 = RequisitoMateriais("ectoplasma", 30)
    essencia_2 = RequisitoMateriais("essencia_fantasmagorica", 20)
    essencia_3 = RequisitoMateriais("osso_amaldicoado", 20)

    chama_1 = RequisitoMateriais("cristal_de_fogo", 25)
    chama_2 = RequisitoMateriais("cinza_elemental", 20)
    chama_3 = RequisitoMateriais("coracao_do_troll", 8)

    pele_1 = RequisitoMateriais("pele_de_ogro_vulcanico", 20)
    pele_2 = RequisitoMateriais("escama_de_hidra", 10)
    pele_3 = RequisitoMateriais("fragmento_de_pedra_magica", 12)

    arte_1 = RequisitoMateriais("grimorio_sombrio", 6)
    arte_2 = RequisitoMateriais("alma_do_necromante", 5)
    arte_3 = RequisitoMateriais("carne_putrefata", 30)

    garras_1 = RequisitoMateriais("garra_de_wyvern", 15)
    garras_2 = RequisitoMateriais("dente_de_ogro", 20)
    garras_3 = RequisitoMateriais("escama_de_wyvern", 20)

    veneno_1 = RequisitoMateriais("veneno_de_hidra", 12)
    veneno_2 = RequisitoMateriais("veneno_de_serpente", 20)
    veneno_3 = RequisitoMateriais("ectoplasma", 25)

    alma_1 = RequisitoMateriais("alma_do_cavaleiro", 10)
    alma_2 = RequisitoMateriais("fragmento_de_armadura_negra", 25)
    alma_3 = RequisitoMateriais("nucleo_de_golem", 8)

    tita_1 = RequisitoMateriais("coracao_de_lava", 5)
    tita_2 = RequisitoMateriais("escama_de_hidra", 15)
    tita_3 = RequisitoMateriais("cristal_de_fogo", 30)
    tita_4 = RequisitoMateriais("cinza_elemental", 25)

    coracao_1 = RequisitoMateriais("coracao_de_dragao", 5)
    coracao_2 = RequisitoMateriais("escama_do_dragao_anciao", 12)
    coracao_3 = RequisitoMateriais("dente_do_dragao_anciao", 10)

    veu_1 = RequisitoMateriais("essencia_do_espectro", 20)
    veu_2 = RequisitoMateriais("fragmento_espectral", 20)
    veu_3 = RequisitoMateriais("alma_do_necromante", 8)
    veu_4 = RequisitoMateriais("essencia_da_morte", 5)

    senhor_1 = RequisitoMateriais("essencia_abissal", 8)
    senhor_2 = RequisitoMateriais("olho_do_kraken", 6)
    senhor_3 = RequisitoMateriais("tentaculo_do_kraken", 10)
    senhor_4 = RequisitoMateriais("escama_de_serpente", 30)

    rei_1 = RequisitoMateriais("coroa_do_rei_espectro", 3)
    rei_2 = RequisitoMateriais("alma_do_rei", 5)
    rei_3 = RequisitoMateriais("essencia_real_espectral", 3)
    rei_4 = RequisitoMateriais("seiva_sombria", 20)

    trovao_1 = RequisitoMateriais("essencia_do_trovao_primordial", 5)
    trovao_2 = RequisitoMateriais("cristal_do_trovao", 15)
    trovao_3 = RequisitoMateriais("fragmento_do_trovao", 20)
    trovao_4 = RequisitoMateriais("nucleo_eletrico", 15)

    legado_1 = RequisitoMateriais("alma_do_tita", 4)
    legado_2 = RequisitoMateriais("fragmento_do_martelo_do_tita", 6)
    legado_3 = RequisitoMateriais("essencia_do_trovao_primordial", 3)
    legado_4 = RequisitoMateriais("cristal_do_trovao", 20)

    frag_1 = RequisitoMateriais("cristal_do_caos", 20)
    frag_2 = RequisitoMateriais("essencia_demoniaca", 15)
    frag_3 = RequisitoMateriais("fragmento_sombrio", 20)
    frag_4 = RequisitoMateriais("alma_sombria", 20)

    caos_1 = RequisitoMateriais("essencia_do_caos_primordial", 3)
    caos_2 = RequisitoMateriais("coroa_do_caos", 3)
    caos_3 = RequisitoMateriais("alma_do_lorde_do_caos", 4)
    caos_4 = RequisitoMateriais("coroa_do_rei_espectro", 2)
    caos_5 = RequisitoMateriais("coracao_de_dragao", 3)

    return [
        Codex("instinto_selvagem", [instinto_1, instinto_2, instinto_3],
              Recompensa(xp_bonus = 0.05)),
        Codex("sangue_das_cavernas", [sangue_1, sangue_2, sangue_3],
              Recompensa(ouro_bonus = 0.05)),
        Codex("muralha_bruta", [muralha_1, muralha_2, muralha_3],
              Recompensa(defesa = 0.08)),
        Codex("presas_da_floresta", [presas_1, presas_2, presas_3],
              Recompensa(ataque = 0.05)),
        Codex("essencia_sombria", [essencia_1, essencia_2, essencia_3],
              Recompensa(ataque = 0.08)),
        Codex("chama_interior", [chama_1, chama_2, chama_3],
              Recompensa(ataque = 0.10)),
        Codex("pele_vulcanica", [pele_1, pele_2, pele_3],
              Recompensa(hp_max = 0.10)),
        Codex("arte_da_necromancia", [arte_1, arte_2, arte_3],
              Recompensa(xp_bonus = 0.08, ouro_bonus = 0.05)),
        Codex("garras_do_predador", [garras_1, garras_2, garras_3],
              Recompensa(chance_critico = 0.08)),
        Codex("veneno_eterno", [veneno_1, veneno_2, veneno_3],
              Recompensa(ataque = 0.10, chance_critico = 0.05)),
        Codex("alma_forjada", [alma_1, alma_2, alma_3],
              Recompensa(defesa = 0.12)),
        Codex("tita_de_lava", [tita_1, tita_2, tita_3, tita_4],
              Recompensa(ataque = 0.15, defesa = 0.05)),
        Codex("coracao_draconico", [coracao_1, coracao_2, coracao_3],
              Recompensa(ataque = 0.20, hp_max = 0.10)),
        Codex("veu_espectral", [veu_1, veu_2, veu_3, veu_4],
              Recompensa(defesa = 0.15, hp_max = 0.10)),
        Codex("senhor_do_abismo", [senhor_1, senhor_2, senhor_3, senhor_4],
              Recompensa(xp_bonus = 0.10, ouro_bonus = 0.20)),
        Codex("rei_das_sombras", [rei_1, rei_2, rei_3, rei_4],
              Recompensa(xp_bonus = 0.20, ouro_bonus = 0.10)),
        Codex("trovao_primordial", [trovao_1, trovao_2, trovao_3, trovao_4],
              Recompensa(chance_critico = 0.25, dano_critico = 0.15)),
        Codex("legado_do_tita", [legado_1, legado_2, legado_3, legado_4],
              Recompensa(ataque = 0.20, defesa = 0.15)),
        Codex("fragmento_do_caos", [frag_1, frag_2, frag_3, frag_4],
              Recompensa(ataque = 0.15, chance_critico = 0.10, dano_critico = 0.10)),
        Codex("caos_absoluto", [caos_1, caos_2, caos_3, caos_4, caos_5],
              Recompensa(ataque = 0.30, defesa = 0.10, hp_max = 0.15))
    ]