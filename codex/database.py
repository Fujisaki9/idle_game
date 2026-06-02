from codex.models import Codex
from shared.reward import Recompensa
from shared.requirement import RequisitoMateriais


def criar_codex() -> list[Codex]:
    """
    Cria os objetos da classe Codex com seus requisitos e recompensas.
    :return: Lista de objetos da classe Codex.
    """
    instinto_1 = RequisitoMateriais("pele_de_lobo", 20, "[1]_floresta_sombria")
    instinto_2 = RequisitoMateriais("garra_de_lobo", 15, "[1]_floresta_sombria")
    instinto_3 = RequisitoMateriais("pele_de_goblin", 20, "[1]_floresta_sombria")

    sangue_1 = RequisitoMateriais("sangue_de_morcego", 25, "[2]_caverna_do_eco")
    sangue_2 = RequisitoMateriais("asa_de_morcego", 20, "[2]_caverna_do_eco")
    sangue_3 = RequisitoMateriais("caveira_de_esqueleto", 15, "[2]_caverna_do_eco")

    muralha_1 = RequisitoMateriais("pedra_do_troll", 12, "[1]_floresta_sombria")
    muralha_2 = RequisitoMateriais("osso_de_esqueleto", 30, "[2]_caverna_do_eco")
    muralha_3 = RequisitoMateriais("nucleo_do_golem", 8, "[2]_caverna_do_eco")

    presas_1 = RequisitoMateriais("dente_de_goblin", 25, "[1]_floresta_sombria")
    presas_2 = RequisitoMateriais("garra_de_lobo", 20, "[1]_floresta_sombria")
    presas_3 = RequisitoMateriais("fragmento_de_pedra_magica", 10,
                                  "[2]_caverna_do_eco")

    essencia_1 = RequisitoMateriais("ectoplasma", 30, "[3]_ruinas_amaldicoadas")
    essencia_2 = RequisitoMateriais("essencia_fantasmagorica", 20,
                                    "[3]_ruinas_amaldicoadas")
    essencia_3 = RequisitoMateriais("osso_amaldicoado", 20, "[3]_ruinas_amaldicoadas")

    chama_1 = RequisitoMateriais("cristal_de_fogo", 25, "[4]_montanha_de_fogo")
    chama_2 = RequisitoMateriais("cinza_elemental", 20, "[4]_montanha_de_fogo")
    chama_3 = RequisitoMateriais("coracao_do_troll", 8, "[1]_floresta_sombria")

    pele_1 = RequisitoMateriais("pele_de_ogro_vulcanico", 20, "[4]_montanha_de_fogo")
    pele_2 = RequisitoMateriais("escama_de_hidra", 10, "[4]_montanha_de_fogo")
    pele_3 = RequisitoMateriais("fragmento_de_pedra_magica", 12, "[2]_caverna_do_eco")

    arte_1 = RequisitoMateriais("grimorio_sombrio", 6, "[3]_ruinas_amaldicoadas")
    arte_2 = RequisitoMateriais("alma_do_necromante", 5, "[3]_ruinas_amaldicoadas")
    arte_3 = RequisitoMateriais("carne_putrefata", 30, "[3]_ruinas_amaldicoadas")

    garras_1 = RequisitoMateriais("garra_de_wyvern", 15, "[5]_torre_do_dragao")
    garras_2 = RequisitoMateriais("dente_de_ogro", 20, "[4]_montanha_de_fogo")
    garras_3 = RequisitoMateriais("escama_de_wyvern", 20, "[5]_torre_do_dragao")

    veneno_1 = RequisitoMateriais("veneno_de_hidra", 12, "[4]_montanha_de_fogo")
    veneno_2 = RequisitoMateriais("veneno_de_serpente", 20, "[6]_abismo_aquatico")
    veneno_3 = RequisitoMateriais("ectoplasma", 25, "[3]_ruinas_amaldicoadas")

    alma_1 = RequisitoMateriais("alma_do_cavaleiro", 10, "[5]_torre_do_dragao")
    alma_2 = RequisitoMateriais("fragmento_de_armadura_negra", 25,
                                "[5]_torre_do_dragao")
    alma_3 = RequisitoMateriais("nucleo_de_golem", 8, "[2]_caverna_do_eco")

    tita_1 = RequisitoMateriais("coracao_de_lava", 5, "[4]_montanha_de_fogo")
    tita_2 = RequisitoMateriais("escama_de_hidra", 15, "[4]_montanha_de_fogo")
    tita_3 = RequisitoMateriais("cristal_de_fogo", 30, "[4]_montanha_de_fogo")
    tita_4 = RequisitoMateriais("cinza_elemental", 25, "[4]_montanha_de_fogo")

    coracao_1 = RequisitoMateriais("coracao_de_dragao", 5, "[5]_torre_do_dragao")
    coracao_2 = RequisitoMateriais("escama_do_dragao_anciao", 12,
                                   "[5]_torre_do_dragao")
    coracao_3 = RequisitoMateriais("dente_do_dragao_anciao", 10,
                                   "[5]_torre_do_dragao")

    veu_1 = RequisitoMateriais("essencia_do_espectro", 20, "[7]_floresta_amaldicoada")
    veu_2 = RequisitoMateriais("fragmento_espectral", 20, "[7]_floresta_amaldicoada")
    veu_3 = RequisitoMateriais("alma_do_necromante", 8, "[3]_ruinas_amaldicoadas")
    veu_4 = RequisitoMateriais("essencia_da_morte", 5, "[3]_ruinas_amaldicoadas")

    senhor_1 = RequisitoMateriais("essencia_abissal", 8, "[6]_abismo_aquatico")
    senhor_2 = RequisitoMateriais("olho_do_kraken", 6, "[6]_abismo_aquatico")
    senhor_3 = RequisitoMateriais("tentaculo_do_kraken", 10, "[6]_abismo_aquatico")
    senhor_4 = RequisitoMateriais("escama_de_serpente", 30, "[6]_abismo_aquatico")

    rei_1 = RequisitoMateriais("coroa_do_rei_espectro", 3, "[7]_floresta_amaldicoada")
    rei_2 = RequisitoMateriais("alma_do_rei", 5, "[7]_floresta_amaldicoada")
    rei_3 = RequisitoMateriais("essencia_real_espectral", 3,
                               "[7]_floresta_amaldicoada")
    rei_4 = RequisitoMateriais("seiva_sombria", 20, "[7]_floresta_amaldicoada")

    trovao_1 = RequisitoMateriais("essencia_do_trovao_primordial", 5,
                                  "[8]_templo_do_trovao")
    trovao_2 = RequisitoMateriais("cristal_do_trovao", 15, "[8]_templo_do_trovao")
    trovao_3 = RequisitoMateriais("fragmento_do_trovao", 20, "[8]_templo_do_trovao")
    trovao_4 = RequisitoMateriais("nucleo_eletrico", 15, "[8]_templo_do_trovao")

    legado_1 = RequisitoMateriais("alma_do_tita", 4, "[8]_templo_do_trovao")
    legado_2 = RequisitoMateriais("fragmento_do_martelo_do_tita", 6,
                                  "[8]_templo_do_trovao")
    legado_3 = RequisitoMateriais("essencia_do_trovao_primordial", 3,
                                  "[8]_templo_do_trovao")
    legado_4 = RequisitoMateriais("cristal_do_trovao", 20, "[8]_templo_do_trovao")

    frag_1 = RequisitoMateriais("cristal_do_caos", 20, "[9]_portao_do_caos")
    frag_2 = RequisitoMateriais("essencia_demoniaca", 15, "[9]_portao_do_caos")
    frag_3 = RequisitoMateriais("fragmento_sombrio", 20, "[9]_portao_do_caos")
    frag_4 = RequisitoMateriais("alma_sombria", 20, "[9]_portao_do_caos")

    caos_1 = RequisitoMateriais("essencia_do_caos_primordial", 3,
                                "[9]_portao_do_caos")
    caos_2 = RequisitoMateriais("coroa_do_caos", 3, "[9]_portao_do_caos")
    caos_3 = RequisitoMateriais("alma_do_lorde_do_caos", 4, "[9]_portao_do_caos")
    caos_4 = RequisitoMateriais("coroa_do_rei_espectro", 2,
                                "[7]_floresta_amaldicoada")
    caos_5 = RequisitoMateriais("coracao_de_dragao", 3, "[5]_torre_do_dragao")

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
