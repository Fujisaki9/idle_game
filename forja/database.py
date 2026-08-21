from copy import deepcopy

from base.material import MaterialRequerido


def escolher_recipe_forja(indice_escolhido: int) -> dict[int | str, Any]:
    dicionario_recipes = {
        # Recipes - Arma
        1: {
            "titulo": "ARMA - RECIPES",
            # Lâmina Sombria (Épica)
            1 : {
                "nome": "lamina_sombria",
                "raridade": "epico",
                "indice_raridade": 1,
                "raridade_necessaria": "comum",
                "nivel_maximo": 40,
                "materiais": [
                MaterialRequerido("pele_de_goblin", 15, "[1]_floresta_sombria"),
                MaterialRequerido("garra_de_lobo", 9, "[1]_floresta_sombria"),
                MaterialRequerido("essencia_do_troll", 3, "[2]_caverna_do_eco"),
                MaterialRequerido("osso_de_esqueleto", 15, "[2]_caverna_do_eco"),
                MaterialRequerido("essencia_do_golem", 3, "[2]_caverna_do_eco"),
                MaterialRequerido("essencia_da_morte", 3, "[3]_ruinas_amaldicoadas")
                ]
                },

            # Lâmina do Caos Vulcânico (Única)
            2 : {
                "nome": "lamina_do_caos_vulcanico",
                "raridade": "unico",
                "indice_raridade": 2,
                "raridade_necessaria": "epico",
                "nivel_maximo": 50,
                "materiais": [
                MaterialRequerido("cristal_de_fogo", 15, "[4]_montanha_de_fogo"),
                MaterialRequerido("pele_de_ogro_vulcanico", 9, "[4]_montanha_de_fogo"),
                MaterialRequerido("coracao_de_lava", 3, "[4]_montanha_de_fogo"),
                MaterialRequerido("escama_de_wyvern", 15, "[5]_torre_do_dragao"),
                MaterialRequerido("garra_de_wyvern", 9, "[5]_torre_do_dragao"),
                MaterialRequerido("coracao_de_dragao", 3, "[5]_torre_do_dragao")
                ]
                },

            # Lâmina do Fim (Lendária)
            3 : {
                "nome": "lamina_do_fim",
                "raridade": "lendario",
                "indice_raridade": 3,
                "raridade_necessaria": "unico",
                "nivel_maximo": 60,
                "materiais": [
                MaterialRequerido("essencia_do_espectro", 15, "[7]_floresta_amaldicoada"),
                MaterialRequerido("coroa_do_rei_espectro", 3, "[7]_floresta_amaldicoada"),
                MaterialRequerido("cristal_do_trovao", 15, "[8]_templo_do_trovao"),
                MaterialRequerido("essencia_do_trovao_primordial", 3, "[8]_templo_do_trovao"),
                MaterialRequerido("alma_sombria", 15, "[9]_portao_do_caos"),
                MaterialRequerido("essencia_do_caos_primordial", 3, "[9]_portao_do_caos")
                ]
                }
            },

        # Recipes - Armadura
        2: {
            "titulo": "ARMADURA - RECIPES",
            # Armadura das Sombras (Épica)
            1 : {
                "nome": "armadura_das_sombras",
                "raridade": "epico",
                "indice_raridade": 1,
                "raridade_necessaria": "comum",
                "nivel_maximo": 40,
                "materiais": [
                MaterialRequerido("pele_de_lobo", 15, "[1]_floresta_sombria"),
                MaterialRequerido("dente_de_goblin", 9, "[1]_floresta_sombria"),
                MaterialRequerido("pedra_do_troll", 6, "[1]_floresta_sombria"),
                MaterialRequerido("caveira_de_esqueleto", 9, "[2]_caverna_do_eco"),
                MaterialRequerido("nucleo_do_golem", 3, "[2]_caverna_do_eco"),
                MaterialRequerido("alma_do_necromante", 3, "[3]_ruinas_amaldicoadas")
                ]
                },

            # Armadura do Dragão (Única)
            2 : {
                "nome": "armadura_do_dragao",
                "raridade": "unico",
                "indice_raridade": 2,
                "raridade_necessaria": "epico",
                "nivel_maximo": 50,
                "materiais": [
                MaterialRequerido("cinza_elemental", 15, "[4]_montanha_de_fogo"),
                MaterialRequerido("dente_de_ogro", 9, "[4]_montanha_de_fogo"),
                MaterialRequerido("escama_de_hidra", 6, "[4]_montanha_de_fogo"),
                MaterialRequerido("fragmento_de_armadura_negra", 15, "[5]_torre_do_dragao"),
                MaterialRequerido("escama_de_wyvern", 9, "[5]_torre_do_dragao"),
                MaterialRequerido("escama_do_dragao_anciao", 6, "[5]_torre_do_dragao")
                ]
                },

            # Armadura do Caos (Lendária)
            3 : {
                "nome": "armadura_do_caos",
                "raridade": "lendario",
                "indice_raridade": 3,
                "raridade_necessaria": "unico",
                "nivel_maximo": 60,
                "materiais": [
                MaterialRequerido("casca_sombria", 15, "[7]_floresta_amaldicoada"),
                MaterialRequerido("alma_do_rei", 3, "[7]_floresta_amaldicoada"),
                MaterialRequerido("nucleo_eletrico", 15, "[8]_templo_do_trovao"),
                MaterialRequerido("alma_do_tita", 3, "[8]_templo_do_trovao"),
                MaterialRequerido("fragmento_sombrio", 15, "[9]_portao_do_caos"),
                MaterialRequerido("alma_do_lorde_do_caos", 3, "[9]_portao_do_caos")
                ]
                }
            },

        # Recipes - Acessório
        3 : {
            "titulo": "ACESSÓRIO - RECIPES",
            # Amuleto Sombrio (Épico)
            1 : {
                "nome": "amuleto_sombrio",
                "raridade": "epico",
                "indice_raridade": 1,
                "raridade_necessaria": "comum",
                "nivel_maximo": 40,
                "materiais": [
                MaterialRequerido("dente_de_goblin", 9, "[1]_floresta_sombria"),
                MaterialRequerido("coracao_do_troll", 3, "[1]_floresta_sombria"),
                MaterialRequerido("asa_de_morcego", 15, "[2]_caverna_do_eco"),
                MaterialRequerido("sangue_de_morcego", 9, "[2]_caverna_do_eco"),
                MaterialRequerido("grimorio_sombrio", 3, "[3]_ruinas_amaldicoadas"),
                MaterialRequerido("osso_amaldicoado", 9, "[3]_ruinas_amaldicoadas")
                ]
                },

            # Amuleto Abissal (Único)
            2 : {
                "nome": "amuleto_abissal",
                "raridade": "unico",
                "indice_raridade": 2,
                "raridade_necessaria": "epico",
                "nivel_maximo": 50,
                "materiais": [
                MaterialRequerido("veneno_de_hidra", 6, "[4]_montanha_de_fogo"),
                MaterialRequerido("alma_do_cavaleiro", 9, "[5]_torre_do_dragao"),
                MaterialRequerido("escama_de_serpente", 15, "[6]_abismo_aquatico"),
                MaterialRequerido("veneno_de_serpente", 9, "[6]_abismo_aquatico"),
                MaterialRequerido("olho_do_kraken", 3, "[6]_abismo_aquatico"),
                MaterialRequerido("essencia_abissal", 3, "[6]_abismo_aquatico")
                ]
                },

            # Amuleto do Caos Eterno (Lendário)
            3 : {
                "nome": "amuleto_do_caos_eterno",
                "raridade": "lendario",
                "indice_raridade": 3,
                "raridade_necessaria": "unico",
                "nivel_maximo": 60,
                "materiais": [
                MaterialRequerido("seiva_sombria", 9, "[7]_floresta_amaldicoada"),
                MaterialRequerido("essencia_real_espectral", 3, "[7]_floresta_amaldicoada"),
                MaterialRequerido("fragmento_do_trovao", 15, "[8]_templo_do_trovao"),
                MaterialRequerido("essencia_do_trovao", 9, "[8]_templo_do_trovao"),
                MaterialRequerido("alma_sombria", 9, "[9]_portao_do_caos"),
                MaterialRequerido("coroa_do_caos", 3, "[9]_portao_do_caos")
                ]
                }
            }
        }

    return deepcopy(dicionario_recipes[indice_escolhido])