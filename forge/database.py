from copy import deepcopy

from forge.models import Recipe


def criar_recipes_forja(indice) -> dict:
    """
    Cria os objetos da classe Recipe.
    :param indice: Índice do equipamento (1 = Arma, 2 = Armadura, 3 = Acessório).
    :return: Dicionário com o título e os recipes do equipamento escolhido, contendo as chaves 'titulo', 'nome',
    'raridade', 'indice_raridade', 'raridade_necessaria', 'nivel_maximo' e 'materiais'.
   """
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
                Recipe("pele_de_goblin", 15, "[1]_floresta_sombria"),
                Recipe("garra_de_lobo", 9, "[1]_floresta_sombria"),
                Recipe("essencia_do_troll", 3, "[2]_caverna_do_eco"),
                Recipe("osso_de_esqueleto", 15, "[2]_caverna_do_eco"),
                Recipe("essencia_do_golem", 3, "[2]_caverna_do_eco"),
                Recipe("essencia_da_morte", 3, "[3]_ruinas_amaldicoadas")
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
                Recipe("cristal_de_fogo", 15, "[4]_montanha_de_fogo"),
                Recipe("pele_de_ogro_vulcanico", 9, "[4]_montanha_de_fogo"),
                Recipe("coracao_de_lava", 3, "[4]_montanha_de_fogo"),
                Recipe("escama_de_wyvern", 15, "[5]_torre_do_dragao"),
                Recipe("garra_de_wyvern", 9, "[5]_torre_do_dragao"),
                Recipe("coracao_de_dragao", 3, "[5]_torre_do_dragao")
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
                Recipe("essencia_do_espectro", 15, "[7]_floresta_amaldicoada"),
                Recipe("coroa_do_rei_espectro", 3, "[7]_floresta_amaldicoada"),
                Recipe("cristal_do_trovao", 15, "[8]_templo_do_trovao"),
                Recipe("essencia_do_trovao_primordial", 3, "[8]_templo_do_trovao"),
                Recipe("alma_sombria", 15, "[9]_portao_do_caos"),
                Recipe("essencia_do_caos_primordial", 3, "[9]_portao_do_caos")
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
                Recipe("pele_de_lobo", 15, "[1]_floresta_sombria"),
                Recipe("dente_de_goblin", 9, "[1]_floresta_sombria"),
                Recipe("pedra_do_troll", 6, "[1]_floresta_sombria"),
                Recipe("caveira_de_esqueleto", 9, "[2]_caverna_do_eco"),
                Recipe("nucleo_do_golem", 3, "[2]_caverna_do_eco"),
                Recipe("alma_do_necromante", 3, "[3]_ruinas_amaldicoadas")
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
                Recipe("cinza_elemental", 15, "[4]_montanha_de_fogo"),
                Recipe("dente_de_ogro", 9, "[4]_montanha_de_fogo"),
                Recipe("escama_de_hidra", 6, "[4]_montanha_de_fogo"),
                Recipe("fragmento_de_armadura_negra", 15, "[5]_torre_do_dragao"),
                Recipe("escama_de_wyvern", 9, "[5]_torre_do_dragao"),
                Recipe("escama_do_dragao_anciao", 6, "[5]_torre_do_dragao")
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
                Recipe("casca_sombria", 15, "[7]_floresta_amaldicoada"),
                Recipe("alma_do_rei", 3, "[7]_floresta_amaldicoada"),
                Recipe("nucleo_eletrico", 15, "[8]_templo_do_trovao"),
                Recipe("alma_do_tita", 3, "[8]_templo_do_trovao"),
                Recipe("fragmento_sombrio", 15, "[9]_portao_do_caos"),
                Recipe("alma_do_lorde_do_caos", 3, "[9]_portao_do_caos")
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
                Recipe("dente_de_goblin", 9, "[1]_floresta_sombria"),
                Recipe("coracao_do_troll", 3, "[1]_floresta_sombria"),
                Recipe("asa_de_morcego", 15, "[2]_caverna_do_eco"),
                Recipe("sangue_de_morcego", 9, "[2]_caverna_do_eco"),
                Recipe("grimorio_sombrio", 3, "[3]_ruinas_amaldicoadas"),
                Recipe("osso_amaldicoado", 9, "[3]_ruinas_amaldicoadas")
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
                Recipe("veneno_de_hidra", 6, "[4]_montanha_de_fogo"),
                Recipe("alma_do_cavaleiro", 9, "[5]_torre_do_dragao"),
                Recipe("escama_de_serpente", 15, "[6]_abismo_aquatico"),
                Recipe("veneno_de_serpente", 9, "[6]_abismo_aquatico"),
                Recipe("olho_do_kraken", 3, "[6]_abismo_aquatico"),
                Recipe("essencia_abissal", 3, "[6]_abismo_aquatico")
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
                Recipe("seiva_sombria", 9, "[7]_floresta_amaldicoada"),
                Recipe("essencia_real_espectral", 3, "[7]_floresta_amaldicoada"),
                Recipe("fragmento_do_trovao", 15, "[8]_templo_do_trovao"),
                Recipe("essencia_do_trovao", 9, "[8]_templo_do_trovao"),
                Recipe("alma_sombria", 9, "[9]_portao_do_caos"),
                Recipe("coroa_do_caos", 3, "[9]_portao_do_caos")
                ]
                }
            }
        }

    return deepcopy(dicionario_recipes[indice])