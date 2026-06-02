from time import sleep
import json, os

from rich import print as rprint

from inventory.models import Inventario
from utils.console import limpar_console


def carregar_dados():
    """
    Inicializa o arquivo .json e carrega todos os dados salvos, caso houver.
    :return: Dicionário com os dados salvos ou dicionário vazio caso não exista save.
    """
    if os.path.exists("save.json"):
        with open("save.json", "r", encoding = "utf-8") as arquivo:
            return json.load(arquivo)
    return {}


def salvar_dados(dados):
    """
    Salva todos os dados coletados no jogo dentro do arquivo .json.
    :param dados: Dicionário contendo todos os dados coletados.
    :return: None
    """
    with open("save.json", "w", encoding = "utf-8") as arquivo:
        json.dump(dados, arquivo, indent = 4, ensure_ascii = False)


def salvar_jogo(heroi, zona, inventario, indice_zona, codex):
    """
    Coleta os dados atuais do jogo e os salva no arquivo .json.
    :param heroi: Objeto heroi -> classe Heroi.
    :param zona: Lista de objetos da classe Zona.
    :param inventario: Dicionário que contém os objetos da classe Inventário.
    :param indice_zona: Índice da zona atual na lista de zonas.
    :param codex: Lista de objetos da classe Codex.
    :return: None
    """
    dados = {
        "heroi": {
            "nome": heroi.nome,
            "nivel": heroi.nivel,
            "xp": heroi.xp,
            "xp_bonus": heroi.xp_bonus,
            "ouro": heroi.ouro,
            "ouro_bonus": heroi.ouro_bonus,
            "hp": heroi.hp,
            "hp_max": heroi.hp_max,
            "ataque": heroi.ataque,
            "defesa": heroi.defesa,
            "chance_critico": heroi.chance_critico,
            "dano_critico": heroi.dano_critico
        },
        "equipamentos": {
            "arma": {
                "nome": heroi.arma.nome_equip,
                "nivel": heroi.arma.nivel_equip,
                "nivel_max": heroi.arma.nivel_max,
                "raridade": heroi.arma.raridade
            },
            "armadura": {
                "nome": heroi.armadura.nome_equip,
                "nivel": heroi.armadura.nivel_equip,
                "nivel_max": heroi.armadura.nivel_max,
                "raridade": heroi.armadura.raridade
            },
            "acessorio": {
                "nome": heroi.acessorio.nome_equip,
                "nivel": heroi.acessorio.nivel_equip,
                "nivel_max": heroi.acessorio.nivel_max,
                "raridade": heroi.acessorio.raridade
            }
        },
        "inventario" : {
            nome: {
                "quantidade": inventario[nome].quantidade_item,
                "preco_unitario": inventario[nome].preco_unitario,
                "preco_total": inventario[nome].preco_total
            }
            for nome in inventario
        },
        "zonas": {
            zona[indice].nome_zona: zona[indice].zona_concluida
            for indice in range(len(zona))
        },
        "codex": {
            colecao.nome_colecao: {
                "conclusao": colecao.conclusao,
                "requisitos": {
                    requisito.nome_material: {
                        "quantidade": requisito.quantidade,
                        "obtido": requisito.obtido
                    }
                for requisito in colecao.requisitos
                }
            }
            for colecao in codex
        },
        "indice_zona": indice_zona
    }
    salvar_dados(dados)


def carregar_jogo(heroi, zonas, inventario, codex):
    """
    Carrega os dados armazenados no arquivo .json para dentro do jogo.
    :param heroi: Objeto heroi -> classe Heroi.
    :param zonas: Lista de objetos da classe Zona.
    :param inventario: Dicionário que contém os objetos da classe Inventário.
    :param codex: Lista de objetos da classe Codex.
    :return: Tupla contendo um booleano (True se save existe, False se novo jogo) e o índice da zona atual.
    """
    dados = carregar_dados()
    if not dados:
        return False, 0    # Novo jogo.

    heroi.nome = dados["heroi"]["nome"]
    heroi.nivel = dados["heroi"]["nivel"]
    heroi.xp = dados["heroi"]["xp"]
    heroi.xp_bonus = dados["heroi"]["xp_bonus"]
    heroi.ouro = dados["heroi"]["ouro"]
    heroi.ouro_bonus = dados["heroi"]["ouro_bonus"]
    heroi.hp = dados["heroi"]["hp"]
    heroi.hp_max = dados["heroi"]["hp_max"]
    heroi.ataque = dados["heroi"]["ataque"]
    heroi.defesa = dados["heroi"]["defesa"]
    heroi.chance_critico = dados["heroi"]["chance_critico"]
    heroi.dano_critico = dados["heroi"]["dano_critico"]

    heroi.arma.nome_equip = dados["equipamentos"]["arma"]["nome"]
    heroi.arma.nivel_equip = dados["equipamentos"]["arma"]["nivel"]
    heroi.arma.nivel_max = dados["equipamentos"]["arma"]["nivel_max"]
    heroi.arma.raridade = dados["equipamentos"]["arma"]["raridade"]

    heroi.armadura.nome_equip = dados["equipamentos"]["armadura"]["nome"]
    heroi.armadura.nivel_equip = dados["equipamentos"]["armadura"]["nivel"]
    heroi.armadura.nivel_max = dados["equipamentos"]["armadura"]["nivel_max"]
    heroi.armadura.raridade = dados["equipamentos"]["armadura"]["raridade"]

    heroi.acessorio.nome_equip = dados["equipamentos"]["acessorio"]["nome"]
    heroi.acessorio.nivel_equip = dados["equipamentos"]["acessorio"]["nivel"]
    heroi.acessorio.nivel_max = dados["equipamentos"]["acessorio"]["nivel_max"]
    heroi.acessorio.raridade = dados["equipamentos"]["acessorio"]["raridade"]

    for nome, valores in dados["inventario"].items():
        inventario[nome] = Inventario(nome, valores["quantidade"], valores["preco_unitario"], valores["preco_total"])

    for zona in zonas:
        if zona.nome_zona in dados["zonas"]:
            zona.zona_concluida = dados["zonas"][zona.nome_zona]

    for colecao in codex:
        if colecao.nome_colecao in dados["codex"]:
            dados_colecao = dados["codex"][colecao.nome_colecao]
            colecao.conclusao = dados_colecao["conclusao"]
            for requisito in colecao.requisitos:
                if requisito.nome_material in dados_colecao["requisitos"]:
                    requisito.quantidade = dados_colecao["requisitos"][requisito.nome_material]["quantidade"]
                    requisito.obtido = dados_colecao["requisitos"][requisito.nome_material]["obtido"]


    return True, dados["indice_zona"]


def continuar_jogo(heroi, zona, inventario, indice_zona, codex):
    """
    Salva os dados em um arquivo .json e reinicia a zona.
    :param heroi: Objeto heroi -> classe Heroi.
    :param zona: Lista de objetos da classe Zona.
    :param inventario: Dicionário que contém os objetos da classe Inventário.
    :param indice_zona: Índice da zona atual na lista de zonas.
    :param codex: Lista de objetos da classe Codex.
    :return: None
    """
    salvar_jogo(heroi, zona, inventario, indice_zona, codex)
    rprint(f"[bold #FF8C00]Zona atual: {zona[indice_zona].nome_zona}[/]")
    sleep(1)
    limpar_console()


def encerrar_jogo(heroi, zona, inventario, indice_zona, codex):
    """
    Salva os dados em um arquivo .json e finaliza o jogo.
    :param heroi: Objeto heroi -> classe Heroi.
    :param zona: Lista de objetos da classe Zona.
    :param inventario: Dicionário que contém os objetos da classe Inventário.
    :param indice_zona: Índice da zona atual na lista de zonas.
    :param codex: Lista de objetos da classe Codex.
    :return: None
    """
    limpar_console()
    salvar_jogo(heroi, zona, inventario, indice_zona, codex)
    rprint("[bold blue]Salvando os dados...[/]")
    sleep(1)
    rprint("[bold blue]Encerrando o jogo...[/]")
    sleep(1)
    rprint("[bold blue]Jogo encerrado![/]")


def verificar_save():
    pass