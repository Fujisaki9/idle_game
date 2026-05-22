import copy

def mostrar_recipes(escolha: int) -> dict:
    """
    Contém os recipes dos equipamentos criados na forja e retorna o recipe selecionado.
    :param escolha: Índice do tipo de equipamento (1 = Arma, 2 = Armadura, 3 = Acessório).
    :return: Retorna uma cópia do dicionário de recipes do equipamento selecionado.
    """
    dicionario_recipes = {
        # Recipes de Armas
        1: {
            # Lâmina Sombria (Épica)
            1: [
                {"nome": "pele_de_goblin", "quantidade": 15, "obtido": False, "zona": "[1]_floresta_sombria"},
                {"nome": "garra_de_lobo", "quantidade": 9, "obtido": False, "zona": "[1]_floresta_sombria"},
                {"nome": "essencia_do_troll", "quantidade":  3, "obtido": False, "zona": "[2]_caverna_do_eco"},
                {"nome": "osso_de_esqueleto", "quantidade":  15, "obtido": False, "zona": "[2]_caverna_do_eco"},
                {"nome": "essencia_do_golem", "quantidade":  3, "obtido": False, "zona": "[2]_caverna_do_eco"},
                {"nome": "essencia_da_morte", "quantidade":  3, "obtido": False, "zona": "[3]_ruinas_amaldicoadas"}
            ],
            # Lâmina do Caos Vulcânico (Única)
            2: [
                {"nome": "cristal_de_fogo", "quantidade": 15, "obtido": False, "zona": "[4]_montanha_de_fogo"},
                {"nome": "pele_de_ogro_vulcanico", "quantidade": 9, "obtido": False, "zona": "[4]_montanha_de_fogo"},
                {"nome": "coracao_de_lava", "quantidade": 3, "obtido": False, "zona": "[4]_montanha_de_fogo"},
                {"nome": "escama_de_wyvern", "quantidade": 15, "obtido": False, "zona": "[5]_torre_do_dragao"},
                {"nome": "garra_de_wyvern", "quantidade": 9, "obtido": False, "zona": "[5]_torre_do_dragao"},
                {"nome": "coracao_de_dragao", "quantidade": 3, "obtido": False, "zona": "[5]_torre_do_dragao"}
            ],
            # Lâmina do Fim (Lendária)
            3: [
                {"nome": "essencia_do_espectro", "quantidade": 15, "obtido": False, "zona": "[7]_floresta_amaldicoada"},
                {"nome": "coroa_do_rei_espectro", "quantidade": 3, "obtido": False, "zona": "[7]_floresta_amaldicoada"},
                {"nome": "cristal_do_trovao", "quantidade": 15, "obtido": False, "zona": "[8]_templo_do_trovao"},
                {"nome": "essencia_do_trovao_primordial", "quantidade": 3, "obtido": False, "zona": "[8]_templo_do_trovao"},
                {"nome": "alma_sombria", "quantidade": 15, "obtido": False, "zona": "[9]_portao_do_caos"},
                {"nome": "essencia_do_caos_primordial", "quantidade": 3, "obtido": False, "zona": "[9]_portao_do_caos"}
            ]
        },
        # Recipes de Armaduras
        2: {
            # Armadura das Sombras (Épica)
            1: [
                {"nome": "pele_de_lobo", "quantidade": 15, "obtido": False, "zona": "[1]_floresta_sombria"},
                {"nome": "dente_de_goblin", "quantidade": 9, "obtido": False, "zona": "[1]_floresta_sombria"},
                {"nome": "pedra_do_troll", "quantidade": 6, "obtido": False, "zona": "[1]_floresta_sombria"},
                {"nome": "caveira_de_esqueleto", "quantidade": 9, "obtido": False, "zona": "[2]_caverna_do_eco"},
                {"nome": "nucleo_do_golem", "quantidade": 3, "obtido": False, "zona": "[2]_caverna_do_eco"},
                {"nome": "alma_do_necromante", "quantidade": 3, "obtido": False, "zona": "[3]_ruinas_amaldicoadas"}
            ],
            # Armadura do Dragão (Única)
            2: [
                {"nome": "cinza_elemental", "quantidade": 15, "obtido": False, "zona": "[4]_montanha_de_fogo"},
                {"nome": "dente_de_ogro", "quantidade": 9, "obtido": False, "zona": "[4]_montanha_de_fogo"},
                {"nome": "escama_de_hidra", "quantidade": 6, "obtido": False, "zona": "[4]_montanha_de_fogo"},
                {"nome": "fragmento_de_armadura_negra", "quantidade": 15, "obtido": False, "zona": "[5]_torre_do_dragao"},
                {"nome": "escama_de_wyvern", "quantidade": 9, "obtido": False, "zona": "[5]_torre_do_dragao"},
                {"nome": "escama_do_dragao_anciao", "quantidade": 6, "obtido": False, "zona": "[5]_torre_do_dragao"}
            ],
            # Armadura do Caos (Lendária)
            3: [
                {"nome": "casca_sombria", "quantidade": 15, "obtido": False, "zona": "[7]_floresta_amaldicoada"},
                {"nome": "alma_do_rei", "quantidade": 3, "obtido": False, "zona": "[7]_floresta_amaldicoada"},
                {"nome": "nucleo_eletrico", "quantidade": 15, "obtido": False, "zona": "[8]_templo_do_trovao"},
                {"nome": "alma_do_tita", "quantidade": 3, "obtido": False, "zona": "[8]_templo_do_trovao"},
                {"nome": "fragmento_sombrio", "quantidade": 15, "obtido": False, "zona": "[9]_portao_do_caos"},
                {"nome": "alma_do_lorde_do_caos", "quantidade": 3, "obtido": False, "zona": "[9]_portao_do_caos"}
            ]
        },
        # Recipes de Acessórios
        3: {
            # Amuleto Sombrio (Épico)
            1: [
                {"nome": "dente_de_goblin", "quantidade": 9, "obtido": False, "zona": "[1]_floresta_sombria"},
                {"nome": "coracao_do_troll", "quantidade": 3, "obtido": False, "zona": "[1]_floresta_sombria"},
                {"nome": "asa_de_morcego", "quantidade": 15, "obtido": False, "zona": "[2]_caverna_do_eco"},
                {"nome": "sangue_de_morcego", "quantidade": 9, "obtido": False, "zona": "[2]_caverna_do_eco"},
                {"nome": "grimorio_sombrio", "quantidade": 3, "obtido": False, "zona": "[3]_ruinas_amaldicoadas"},
                {"nome": "osso_amaldicoado", "quantidade": 9, "obtido": False, "zona": "[3]_ruinas_amaldicoadas"}
            ],
            # Amuleto Abissal (Único)
            2: [
                {"nome": "veneno_de_hidra", "quantidade": 6, "obtido": False, "zona": "[4]_montanha_de_fogo"},
                {"nome": "alma_do_cavaleiro", "quantidade": 9, "obtido": False, "zona": "[5]_torre_do_dragao"},
                {"nome": "escama_de_serpente", "quantidade": 15, "obtido": False, "zona": "[6]_abismo_aquatico"},
                {"nome": "veneno_de_serpente", "quantidade": 9, "obtido": False, "zona": "[6]_abismo_aquatico"},
                {"nome": "olho_do_kraken", "quantidade": 3, "obtido": False, "zona": "[6]_abismo_aquatico"},
                {"nome": "essencia_abissal", "quantidade": 3, "obtido": False, "zona": "[6]_abismo_aquatico"}
            ],
            # Amuleto do Caos Eterno (Lendário)
            3: [
                {"nome": "seiva_sombria", "quantidade": 9, "obtido": False, "zona": "[7]_floresta_amaldicoada"},
                {"nome": "essencia_real_espectral", "quantidade": 3, "obtido": False, "zona": "[7]_floresta_amaldicoada"},
                {"nome": "fragmento_do_trovao", "quantidade": 15, "obtido": False, "zona": "[8]_templo_do_trovao"},
                {"nome": "essencia_do_trovao", "quantidade": 9, "obtido": False, "zona": "[8]_templo_do_trovao"},
                {"nome": "alma_sombria", "quantidade": 9, "obtido": False, "zona": "[9]_portao_do_caos"},
                {"nome": "coroa_do_caos", "quantidade": 3, "obtido": False, "zona": "[9]_portao_do_caos"}
            ]
        }
    }

    return copy.deepcopy(dicionario_recipes[escolha])