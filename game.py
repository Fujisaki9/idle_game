from rich.console import Console
from rich.table import Table
from rich.align import Align
from rich import print as rprint
from time import sleep
import services, utils, save, recipes


def acessar_proxima_zona(indice_zona, zona, heroi) -> tuple:
    """
    Verifica os requisitos e acessa a próxima zona.
    :param indice_zona: Índice da zona atual na lista de zonas.
    :param zona: Lista de objetos da classe Zona.
    :param heroi: Objeto heroi -> classe Heroi.
    :return: Tupla contendo o novo indice_zona e zona_atual.
    """
    zona_atual = zona[indice_zona]
    if indice_zona + 1 < len(zona):
        if zona[indice_zona + 1].nivel_minimo <= heroi.nivel:
            indice_zona += 1
            zona_atual = zona[indice_zona]
            rprint("[bold #FF8C00]Acessando a próxima zona![/]")
            sleep(1)
            rprint(f"[bold #FF8C00][Zona {indice_zona + 1}] {zona_atual.nome_zona}[/]")
            sleep(1)
        else:
            rprint(f"[bold red]Você não tem nível suficiente para acessar a próxima zona[/]")
            sleep(1)
            rprint(f"[bold red][Zona {indice_zona + 2}] {zona[indice_zona + 1].nome_zona} | "
                   f"Nível mínimo: {zona[indice_zona + 1].nivel_minimo}.[/]")
            sleep(1)
            rprint("[bold red]Repetindo a zona atual.[/]")
            sleep(1)
    else:
        rprint("[bold green]Você completou todas as zonas![/]")
        sleep(1)
    return indice_zona, zona_atual


def mostrar_atributos(heroi):
    """
    Exibe todos os atributos do herói.
    :param heroi: Objeto heroi -> classe Heroi.
    :return: None
    """
    console = Console()
    utils.mostrar_menu_principal()
    utils.mostrar_atributos_heroi(heroi)
    console.input("[bold #FF8C00]Pressione ENTER para voltar ao menu principal.[/]")
    utils.limpar_console()


def aprimorar_equipamentos(heroi):
    """
    Utiliza o ouro coletado nos combates para aprimorar o nível dos equipamentos do herói.
    :param heroi: Objeto heroi -> classe Heroi.
    :return: None
    """
    equipamentos_dict = {1: heroi.arma, 2: heroi.armadura, 3: heroi.acessorio}
    while True:
        utils.limpar_console()
        utils.mostrar_menu_principal()
        utils.mostrar_menu_equip()
        opcao_equip = utils.validar_integer("Escolha uma opção: ")
        if opcao_equip in (1, 2, 3):
            rprint(f"[bold #FF8C00]Equipamento: {equipamentos_dict[opcao_equip].nome} |"
                   f" Nível atual: {equipamentos_dict[opcao_equip].nivel}[/]")
            sleep(1)
            services.aprimorar_equipamento(heroi, equipamentos_dict[opcao_equip])
        elif opcao_equip == 4:
            utils.limpar_console()
            break
        else:
            rprint("[bold red]Comando inválido![/]")
        sleep(1)


def forjar_equipamentos(heroi, inventario):
    """
    Utiliza os materiais coletados nos combates para criar equipamentos avançados.
    :param heroi: Objeto heroi -> classe Heroi.
    :param inventario: Dicionário que contém os objetos da classe Inventário.
    :return: None
    """
    console = Console()
    equipamentos_dict = {1: heroi.arma, 2: heroi.armadura, 3: heroi.acessorio}
    equipamentos_raridade = {"comum": 30, "epico": 40, "unico": 50, "lendario": 60}
    raridade_por_escolha = {1: "epico", 2: "unico", 3: "lendario"}
    nomes_equipamentos = {
        1: {1: "Lâmina Sombria", 2: "Lâmina do Caos Vulcânico", 3: "Lâmina do Fim"},
        2: {1: "Armadura das Sombras", 2: "Armadura do Dragão", 3: "Armadura do Caos"},
        3: {1: "Amuleto Sombrio", 2: "Amuleto Abissal", 3: "Amuleto do Caos Eterno"}
    }

    indice_item, recipe_item, indice_raridade = mostrar_itens_forja(heroi, inventario)
    if indice_raridade is None:
        pass
    else:
        for item in recipe_item:
            nome_item = utils.formatar_strings(item["nome"])
            if nome_item in inventario:
                if inventario[nome_item].quantidade_item >= item["quantidade"]:
                    item["obtido"] = True
                    rprint(f"[bold green][{inventario[nome_item].quantidade_item}/{item['quantidade']}] {nome_item} "
                           f"| Zona: {utils.formatar_strings(item['zona'])}[/]")
                else:
                    rprint(f"[bold red][{inventario[nome_item].quantidade_item}/{item['quantidade']}] {nome_item} "
                           f"| Zona: {utils.formatar_strings(item['zona'])}[/]")
            else:
                rprint(f"[bold red]Você não possui {nome_item} | Zona: {utils.formatar_strings(item['zona'])}[/]")

        if all(i["obtido"] for i in recipe_item):
            for item in recipe_item:
                nome_item = utils.formatar_strings(item["nome"])
                inventario[nome_item].quantidade_item -= item["quantidade"]
                if inventario[nome_item].quantidade_item <= 0:
                    del inventario[nome_item]
            item_completo = equipamentos_dict[indice_item]
            item_completo.raridade = raridade_por_escolha[indice_raridade]
            item_completo.nivel_max = equipamentos_raridade[item_completo.raridade]
            item_completo.nome = nomes_equipamentos[indice_item][indice_raridade]
            rprint(f"[bold cyan]Materiais prontos para a forja![/]")
            sleep(1.5)
            rprint(f"[bold cyan]:hammer: Forjando o item...[/]")
            sleep(1.5)
            rprint(f"[bold green]:sparkles:  O item {item_completo.nome.upper()} foi forjado com sucesso![/]")
            sleep(1)
            console.input("[bold #FF8C00]Pressione ENTER para voltar ao menu principal.[/]")
        else:
            rprint("[bold #FF8C00]Materiais insuficientes para craftar![/]")
            console.input("[bold #FF8C00]Pressione ENTER para voltar ao menu principal.[/]")

    rprint("[bold #FF8C00]Saindo da Forja...[/]")
    sleep(1)
    utils.limpar_console()


def mostrar_itens_forja(heroi, inventario) -> tuple:
    """
    Exibe o menu de equipamentos e seus respectivos recipes.
    :param heroi: Objeto heroi -> classe Heroi
    :param inventario: Dicionário que contém os objetos da classe Inventário.
    :return: Tupla contendo o indice do equipamento, o dicionário do recipe e o índice da raridade escolhida.
    """
    console = Console()
    equipamentos_heroi = {1: heroi.arma, 2: heroi.armadura, 3: heroi.acessorio}
    raridade_necessaria = {1: "comum", 2: "epico", 3: "unico"}
    raridade_ordem = {"comum": 0, "epico": 1, "unico": 2, "lendario": 3}
    indice = None
    dicionario = None


    menus = {
        1:{
            "titulo": "ARMAS - RECIPES",
            "opcoes": [
                "[bold yellow][1] Lâmina Sombria (Épico)[/]",
                "[bold magenta][2] Lâmina do Caos Vulcânico (Único)[/]",
                "[bold red][3] Lâmina do Fim (Lendário)[/]",
                "[bold][4] Voltar[/]"
            ]
        },
        2:{
            "titulo": "ARMADURAS - RECIPES",
            "opcoes": [
                "[bold yellow][1] Armadura das Sombras (Épico)[/]",
                "[bold magenta][2] Armadura do Dragão (Único)[/]",
                "[bold red][3] Armadura do Caos (Lendário)[/]",
                "[bold][4] Voltar[/]"
            ]
        },
        3:{
            "titulo": "ACESSÓRIOS - RECIPES",
            "opcoes": [
                "[bold yellow][1] Amuleto Sombrio (Épico)[/]",
                "[bold magenta][2] Amuleto Abissal (Único)[/]",
                "[bold red][3] Amuleto do Caos Eterno (Lendário)[/]",
                "[bold][4] Voltar[/]"
            ]
        }
    }

    while True:
        utils.limpar_console()
        utils.mostrar_menu_principal()
        menu = Table(style = 'yellow', width = 40)
        menu.add_column("RECIPES", justify='center')
        menu.add_row(Align.left("[bold][1] Armas[/]"))
        menu.add_row(Align.left("[bold][2] Armaduras[/]"))
        menu.add_row(Align.left("[bold][3] Acessórios[/]"))
        menu.add_row(Align.left("[bold][4] Sair da Forja[/]"))
        console.print(menu)

        indice = utils.validar_integer("Escolha uma opção: ")

        if indice == 4:
            sleep(0.5)
            break
        elif indice not in menus:
            rprint("[bold red]Insira um comando válido![/]")
            continue

        submenu_info = menus[indice]
        submenu = Table(style = 'yellow', width = 50)
        submenu.add_column(submenu_info["titulo"], justify = 'center')
        for opcao in submenu_info["opcoes"]:
            submenu.add_row(Align.left(opcao))

        while True:
            utils.limpar_console()
            utils.mostrar_menu_principal()
            console.print(submenu)
            escolha = utils.validar_integer("Escolha um Recipe: ")

            if escolha in (1, 2, 3):
                recipe = recipes.mostrar_recipes(indice)
                dicionario = recipe[escolha]
                equipamento_atual = equipamentos_heroi[indice]
                raridade_exigida = raridade_necessaria[escolha]

                menu_recipes = Table(style = 'yellow', width = 80)
                menu_recipes.add_column("ITENS", justify = 'center')
                menu_recipes.add_column("MATERIAIS", justify = 'center')
                menu_recipes.add_column("ZONA", justify = 'center')
                for material in recipe[escolha]:
                    nome_formatado = utils.formatar_strings(material["nome"])
                    quantidade_atual = inventario.get(nome_formatado, None)
                    contador = f"{quantidade_atual.quantidade_item}/{material["quantidade"]}" \
                               if quantidade_atual else f"0/{material["quantidade"]}"

                    menu_recipes.add_row(Align.left(nome_formatado),
                                         contador,
                                         Align.left(utils.formatar_strings(material["zona"])))

                console.print(menu_recipes)

                craft = utils.validar_pergunta("Deseja craftar esse item? [S/N]: ")
                if craft == 'S':
                    if raridade_ordem[equipamento_atual.raridade] > raridade_ordem[raridade_exigida]:
                        rprint("[bold red]Você já possui este item ou uma versão superior![/]")
                        sleep(1.5)
                    elif equipamento_atual.raridade == raridade_exigida:
                        return indice, dicionario, escolha
                    else:
                        rprint(f"[bold red]Você precisa ter o item de raridade anterior para craftar este![/]")
                        sleep(1.5)
            elif escolha == 4:
                break
            else:
                rprint("[bold red]Insira um comando válido![/]")
                sleep(1)

    return indice, dicionario, None


def mostrar_inventario(inventario, heroi):
    """
    Exibe o inventário do herói e oferece a opção de vender os itens coletados.
    :param inventario: Dicionário que contém os objetos da classe Inventário.
    :param heroi: Objeto heroi -> classe Heroi.
    :return: None
    """
    console = Console()
    while True:
        utils.limpar_console()
        utils.mostrar_menu_principal()
        utils.mostrar_inventario(inventario)
        rprint(f"[bold cyan]OURO ATUAL: {heroi.ouro}[/]")
        vender_item = utils.validar_pergunta("Deseja vender algum item? [S/N]: ")
        if vender_item == 'S':
            if not inventario:
                rprint("[bold red]Inventário vazio![/]")
                break
            else:
                services.vender_itens_inventario(heroi, inventario)
        else:
            break
    console.input("[bold #FF8C00]Pressione ENTER para voltar ao menu principal.[/]")
    utils.limpar_console()


def escolher_zona(indice_zona, zona, heroi, inventario) -> tuple:
    """
    Exibe as zonas disponíveis e permite ao jogador navegar entre as zonas já desbloqueadas.
    :param indice_zona: Índice da zona atual na lista de zonas.
    :param zona: Lista de objetos da classe Zona.
    :param heroi: Objeto heroi -> classe Heroi.
    :param inventario: Dicionário que contém os objetos da classe Inventário.
    :return: Tupla contendo o novo indice_zona e zona_atual após a escolha do jogador.
    """
    console = Console()
    zona_atual = zona[indice_zona]
    while True:
        utils.limpar_console()
        utils.mostrar_menu_principal()
        utils.mostrar_tabela_zonas(zona)
        escolha_zona = utils.validar_integer("Escolha uma zona: ")
        if escolha_zona <= len(zona):
            zona_escolhida = zona[escolha_zona - 1]
            if zona_escolhida.zona_concluida and heroi.nivel >= zona_escolhida.nivel_minimo:
                indice_zona = escolha_zona - 1
                zona_atual = zona[indice_zona]
                save.salvar_jogo(heroi, zona, inventario, indice_zona)
                rprint(f"[bold #FF8C00]Indo para a zona selecionada...[/]")
                sleep(1)
                rprint(f"[bold #FF8C00]Zona atual: [{escolha_zona}] {zona_atual.nome_zona}.[/]")
                sleep(1)
                break
            else:
                rprint("[bold red]Zona bloqueada![/]")
                sleep(1)
        elif escolha_zona == len(zona) + 1:
            break
        else:
            rprint("[bold red]Comando inválido![/]")
            sleep(1)
    console.input("[bold #FF8C00]Pressione ENTER para voltar ao menu principal.[/]")
    utils.limpar_console()
    return indice_zona, zona_atual

def continuar_jogo(heroi, zona, inventario, indice_zona):
    """
    Salva os dados em um arquivo .json e reinicia a zona.
    :param heroi: Objeto heroi -> classe Heroi.
    :param zona: Lista de objetos da classe Zona.
    :param inventario: Dicionário que contém os objetos da classe Inventário.
    :param indice_zona: Índice da zona atual na lista de zonas.
    :return: None
    """
    save.salvar_jogo(heroi, zona, inventario, indice_zona)
    rprint(f"[bold #FF8C00]Zona atual: {zona[indice_zona].nome_zona}[/]")
    sleep(1)
    utils.limpar_console()

def encerrar_jogo(heroi, zona, inventario, indice_zona):
    """
    Salva os dados em um arquivo .json e finaliza o jogo.
    :param heroi: Objeto heroi -> classe Heroi.
    :param zona: Lista de objetos da classe Zona.
    :param inventario: Dicionário que contém os objetos da classe Inventário.
    :param indice_zona: Índice da zona atual na lista de zonas.
    :return: None
    """
    utils.limpar_console()
    save.salvar_jogo(heroi, zona, inventario, indice_zona)
    rprint("[bold blue]Salvando os dados...[/]")
    sleep(1)
    rprint("[bold blue]Encerrando o jogo...[/]")
    sleep(1)
    rprint("[bold blue]Jogo encerrado![/]")