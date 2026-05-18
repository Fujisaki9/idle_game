from rich.table import Table
from rich.console import Console
from rich.align import Align
from rich import print as rprint
import os


def validar_integer(pergunta) -> int:
    """
    Valida o input do usuário garantindo que seja um número inteiro positivo.
    :param pergunta: Mensagem exibida ao usuário para solicitar o input.
    :return: Número inteiro positivo inserido pelo usuário.
    """
    console = Console()
    while True:
        try:
            valor = int(console.input(f"[bold #FF8C00]{pergunta}[/]"))
            if valor <= 0:
                rprint("[bold red]Insira um comando válido![/]")
            else:
                return valor
        except ValueError:
            rprint("[bold red]ERRO: Comando inválido![/]")


def validar_pergunta(string) -> str:
    """
    Valida o input do usuário aceitando apenas 'S' ou 'N' como resposta.
    :param string: Mensagem exibida ao usuário para solicitar o input.
    :return: 'S' ou 'N' em maiúsculo conforme a escolha do usuário.
    """
    console = Console()
    while True:
        resposta = console.input(f"[bold #FF8C00]{string}[/]").strip().upper()
        if resposta in ('S', 'N'):
            return resposta
        else:
            rprint("[bold red]ERRO: Digite um comando válido![/]")


def limpar_console():
    """
    Limpa o console de acordo com o sistema operacional.
    :return: None
    """
    if os.name == 'nt':
        comando = 'cls'
    else:
        comando = 'clear'
    os.system(comando)


def formatar_strings(string) -> str:
    """
    Formata strings com underline para o padrão de título, mantendo preposições e artigos em minúsculo.
    :param string: String com underline a ser formatada (ex: pele_de_goblin).
    :return: String formatada no padrão de título (ex: Pele de Goblin).
    """
    lista = ['De', 'Do', 'Da', 'Dos', 'Das', 'No', 'Na', 'O', 'A', 'Os', 'As', 'E']
    final = list()
    palavra = string.title().split('_')
    for indice, valor in enumerate(palavra):
        if valor in lista:
            final.append(valor.lower())
        else:
            final.append(valor)
    string_formatada = ' '.join(final)
    return string_formatada


def mostrar_menu_zona():
    """
    Exibe o menu de opções com todas as opções disponíveis para o jogador.
    :return: None
    """
    console = Console()
    table = Table(style = 'yellow', width = 40)
    table.add_column("MENU", justify = 'center')
    table.add_row(Align.left("[1] Acessar a próxima zona"))
    table.add_row(Align.left("[2] Repetir a zona atual"))
    table.add_row(Align.left("[3] Acessar o menu principal"))
    console.print(table)


def mostrar_menu_principal():
    """
    Exibe o menu principal com todas as opções disponíveis para o jogador.
    :return: None
    """
    table = Table(style = 'yellow', width = 30)
    table.add_column("MENU DE OPÇÕES", justify = 'center')
    table.add_row(Align.left("[1] Mostrar Atributos"))
    table.add_row(Align.left("[2] Aprimorar Equipamentos"))
    table.add_row(Align.left("[3] Forja"))
    table.add_row(Align.left("[4] Abrir Inventário"))
    table.add_row(Align.left("[5] Escolher zona"))
    table.add_row(Align.left("[6] Continuar"))
    table.add_row(Align.left("[7] Sair do jogo"))
    console = Console()
    console.print(table)


def mostrar_menu_equip():
    """
    Exibe o menu de aprimoramento dos equipamentos do herói.
    :return: None
    """
    console = Console()
    table = Table(style = 'yellow')
    table.add_column("EQUIPAMENTOS", justify = 'center')
    table.add_row(Align.left("[1] Aprimorar Arma"))
    table.add_row(Align.left("[2] Aprimorar Armadura"))
    table.add_row(Align.left("[3] Aprimorar Acessório"))
    table.add_row(Align.left("[4] Voltar para o Menu"))
    console.print(table)


def mostrar_atributos_heroi(heroi):
    """
    Exibe os equipamentos e todos os atributos do herói organizados em uma tabela.
    :param heroi: Objeto heroi -> classe Heroi
    :return: None
    """
    console = Console()
    table = Table(style = 'green')
    table.add_column("HEROI", justify = 'center')
    table.add_column("ATRIBUTOS", justify = 'center')
    table.add_row(Align.left("Nome do personagem"), Align.right(heroi.nome))
    table.add_row(Align.left("Level do personagem"), Align.right(str(heroi.nivel)))
    table.add_row(Align.left("Experiência atual"), Align.right(str(heroi.xp)))
    table.add_row(Align.left("Ouro obtido"), Align.right(str(heroi.ouro)))
    table.add_row(Align.left("Ataque total (ATK)"), Align.right(str(heroi.ataque)))
    table.add_row(Align.left("Defesa total (DEF)"), Align.right(str(heroi.defesa)))
    table.add_row(Align.left("HP total (HP)"), Align.right(str(heroi.hp_max)))
    table.add_row(Align.left("HP Atual"), Align.right(str(heroi.hp)))
    table.add_section()

    equipamentos_heroi = [heroi.arma, heroi.armadura, heroi.acessorio]
    atributos = ["ATK:", "DEF:", "HP:"]
    cores = {"epico": "bold yellow", "unico": "bold magenta", "lendario": "bold red"}

    for item, atributo in zip(equipamentos_heroi, atributos):   # Itera 2 listas ao mesmo tempo
        cor = cores.get(item.raridade, "")
        texto = f"{item.nome} ({item.raridade}) (Nv.{item.nivel})"
        if cor:
            nome_formatado = f"[{cor}]{texto}[/]"
        else:
            nome_formatado = texto
        table.add_row(Align.left(nome_formatado),
                      Align.left(f"{atributo:<5} {str(item.calcular_bonus_atual())}"))

    console.print(table)


def mostrar_tabela_zonas(zonas):
    """
    Exibe todas as zonas disponíveis e o status de conclusão.
    :param zonas: Lista de objetos da classe Zona.
    :return: None
    """
    console = Console()
    table = Table(style = 'yellow')
    table.add_column("ZONAS", justify = 'center')
    table.add_column("NV. MÍNIMO", justify = 'center')
    table.add_column("STATUS", justify = 'center')

    for indice, zona in enumerate(zonas, 1):
        if zona.zona_concluida:
            status = "[bold green]Completo[/]"
        else:
            status = "[bold red]Bloqueado[/]"
        table.add_row(Align.left(f"[{indice}] {zona.nome_zona}"), str(zona.nivel_minimo), status)
    table.add_row(Align.left(f"[bold red][{len(zonas) + 1}] Voltar[/]"), "-", "-")

    console.print(table)


def mostrar_inventario(inventario: dict):
    """
    Exibe em uma tabela os materiais coletados, a quantidade obtida e o valor total em ouro.
    :param inventario: Dicionário que contém os objetos da classe Inventário.
    :return: None
    """
    console = Console()
    table = Table(style = 'yellow', width = 90)
    table.add_column("ITENS", justify = 'center')
    table.add_column("QUANTIDADE", justify = 'center')
    table.add_column("PREÇO UNITÁRIO", justify = 'center')
    table.add_column("PREÇO TOTAL", justify='center')
    for item in inventario.values():
        table.add_row(Align.left(item.nome_item),
                      str(item.quantidade_item),
                      str(item.preco_unitario),
                      str(item.preco_total))

    console.print(table)


def mostrar_itens_inventario(inventario):
    """
    Exibe os materiais coletados e seus respectivos indices em uma tabela.
    :param inventario: Dicionário que contém os objetos da classe Inventário.
    :return: None
    """
    console = Console()
    table = Table(style = 'yellow', width = 90)
    table.add_column("ITENS", justify = 'center')
    table.add_column("QUANTIDADE", justify = 'center')
    table.add_column("PREÇO UNITÁRIO", justify='center')
    table.add_column("PREÇO TOTAL", justify = 'center')

    for indice, item in enumerate(inventario.values(), 1):
        table.add_row(Align.left(f"[{indice}] {item.nome_item}"),
                      str(item.quantidade_item),
                      str(item.preco_unitario),
                      str(item.preco_total))
    table.add_row(Align.left(f"[bold red][{len(inventario) + 1}] Voltar[/]"), "-", "-", "-")
    console.print(table)