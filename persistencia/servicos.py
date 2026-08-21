from time import sleep
import json, os

from rich import print as rprint

from codex.classe import Codex
from heroi.classe import Heroi
from inventario.classe import Inventario
from utilitario.console import limpar_console
from zona.classe import Zona


def carregar_dados():
    if os.path.exists("save.json"):
        with open("save.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return {}


def carregar_jogo(heroi: Heroi,
                  zonas: list[Zona],
                  inventario: dict[str, Inventario],
                  codex: list[Codex]) -> tuple[bool, int]:

    dados = carregar_dados()
    if not dados:
        return False, 0    # Novo jogo.

    heroi.nome_personagem = dados["heroi"]["nome"]
    heroi.nivel_personagem = dados["heroi"]["nivel_personagem"]
    heroi.xp = dados["heroi"]["xp"]
    heroi.xp_bonus_heroi = dados["heroi"]["xp_bonus_heroi"]
    heroi.ouro = dados["heroi"]["ouro"]
    heroi.ouro_bonus_heroi = dados["heroi"]["ouro_bonus_heroi"]
    heroi.hp = dados["heroi"]["hp"]
    heroi.hp_max = dados["heroi"]["hp_max"]
    heroi.ataque = dados["heroi"]["ataque"]
    heroi.defesa = dados["heroi"]["defesa"]
    heroi.chance_critico = dados["heroi"]["chance_critico"]
    heroi.dano_critico = dados["heroi"]["dano_critico"]

    heroi.arma.nome_equipamento = dados["equipamentos"]["arma"]["nome_equipamento"]
    heroi.arma.nivel_equipamento = dados["equipamentos"]["arma"]["nivel_equipamento"]
    heroi.arma.nivel_maximo = dados["equipamentos"]["arma"]["nivel_maximo"]
    heroi.arma.raridade = dados["equipamentos"]["arma"]["raridade"]

    heroi.armadura.nome_equipamento = dados["equipamentos"]["armadura"]["nome_equipamento"]
    heroi.armadura.nivel_equipamento = dados["equipamentos"]["armadura"]["nivel_equipamento"]
    heroi.armadura.nivel_maximo = dados["equipamentos"]["armadura"]["nivel_maximo"]
    heroi.armadura.raridade = dados["equipamentos"]["armadura"]["raridade"]

    heroi.acessorio.nome_equipamento = dados["equipamentos"]["acessorio"]["nome_equipamento"]
    heroi.acessorio.nivel_equipamento = dados["equipamentos"]["acessorio"]["nivel_equipamento"]
    heroi.acessorio.nivel_maximo = dados["equipamentos"]["acessorio"]["nivel_maximo"]
    heroi.acessorio.raridade = dados["equipamentos"]["acessorio"]["raridade"]

    for nome, valores in dados["inventario"].items():
        inventario[nome] = Inventario(nome, valores["quantidade_item"], valores["preco_unitario"], valores["preco_total"])

    for zona in zonas:
        if zona.nome_zona in dados["zonas"]:
            zona.zona_concluida = dados["zonas"][zona.nome_zona]

    for colecao in codex:
        if colecao.nome_colecao in dados["codex"]:
            dados_colecao = dados["codex"][colecao.nome_colecao]
            colecao.colecao_concluida = dados_colecao["colecao_concluida"]

            for requisito in colecao.requisitos_colecao:
                if requisito.nome_material in dados_colecao["requisitos"]:
                    requisito.quantidade_exigida = dados_colecao["requisitos"][requisito.nome_material]["quantidade_exigida"]
                    requisito.material_obtido = dados_colecao["requisitos"][requisito.nome_material]["material_obtido"]


    return True, dados["indice_zona"]


def salvar_progresso_jogo(heroi: Heroi,
                          zona: list[Zona],
                          inventario: dict[str, Inventario],
                          indice_zona: int,
                          codex: list[Codex]):

    dados = {
        "heroi": {
            "nome": heroi.nome_personagem,
            "nivel_personagem": heroi.nivel_personagem,
            "xp": heroi.xp,
            "xp_bonus_heroi": heroi.xp_bonus_heroi,
            "ouro": heroi.ouro,
            "ouro_bonus_heroi": heroi.ouro_bonus_heroi,
            "hp": heroi.hp,
            "hp_max": heroi.hp_max,
            "ataque": heroi.ataque,
            "defesa": heroi.defesa,
            "chance_critico": heroi.chance_critico,
            "dano_critico": heroi.dano_critico
        },
        "equipamentos": {
            "arma": {
                "nome_equipamento": heroi.arma.nome_equipamento,
                "nivel_equipamento": heroi.arma.nivel_equipamento,
                "nivel_maximo": heroi.arma.nivel_maximo,
                "raridade": heroi.arma.raridade
            },
            "armadura": {
                "nome_equipamento": heroi.armadura.nome_equipamento,
                "nivel_equipamento": heroi.armadura.nivel_equipamento,
                "nivel_maximo": heroi.armadura.nivel_maximo,
                "raridade": heroi.armadura.raridade
            },
            "acessorio": {
                "nome_equipamento": heroi.acessorio.nome_equipamento,
                "nivel_equipamento": heroi.acessorio.nivel_equipamento,
                "nivel_maximo": heroi.acessorio.nivel_maximo,
                "raridade": heroi.acessorio.raridade
            }
        },
        "inventario" : {
            nome: {
                "quantidade_item": inventario[nome].quantidade_item,
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
                "colecao_concluida": colecao.colecao_concluida,
                "requisitos": {
                    requisito.nome_material: {
                        "quantidade_exigida": requisito.quantidade_exigida,
                        "material_obtido": requisito.material_obtido
                    }
                for requisito in colecao.requisitos_colecao
                }
            }
            for colecao in codex
        },
        "indice_zona": indice_zona
    }
    salvar_dados(dados)


def salvar_dados(dados: dict):
    with open("save.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def continuar_jogo(heroi: Heroi,
                   zona: list[Zona],
                   inventario: dict[str, Inventario],
                   indice_zona: int,
                   codex: list[Codex]):

    salvar_progresso_jogo(heroi, zona, inventario, indice_zona, codex)

    rprint(f"[bold #FF8C00]Zona atual: {zona[indice_zona].nome_zona}[/]")
    sleep(1)
    limpar_console()


def encerrar_jogo(heroi: Heroi,
                  zona: list[Zona],
                  inventario: dict[str, Inventario],
                  indice_zona: int,
                  codex: list[Codex]):

    limpar_console()
    salvar_progresso_jogo(heroi, zona, inventario, indice_zona, codex)

    rprint("[bold blue]Salvando os dados...[/]")
    sleep(1)
    rprint("[bold blue]Encerrando o jogo...[/]")
    sleep(1)
    rprint("[bold blue]Jogo encerrado![/]")