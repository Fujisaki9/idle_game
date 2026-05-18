from rich.console import Console, Group
from rich.progress import ProgressBar
from rich.live import Live
from inventory import Inventario
from rich import print as rprint
from random import randint, random
from time import sleep
import utils


def gerar_barras(heroi, inimigo, log):
    """
    Cria uma interface visual, exibindo barras de vida durante o combate.
    :param heroi: Objeto heroi -> classe Heroi.
    :param inimigo: Objeto inimigo -> classe Inimigo.
    :param log: Histórico de combate coletado.
    :return: Objeto Group do rich contendo as barras de HP e o log de combate.
    """
    texto_log = ''.join(log)
    barra_heroi = ProgressBar(total=heroi.hp_max, completed=max(0, heroi.hp), width=20)
    barra_inimigo = ProgressBar(total=inimigo.hp_max, completed=max(0, inimigo.hp), width=20)

    conteudo = Group(f"{heroi.nome:<20} :heart: {max(0, heroi.hp)}/{heroi.hp_max}", barra_heroi,
                     f"\n{inimigo.nome:<20} :heart: {max(0, inimigo.hp)}/{inimigo.hp_max}", barra_inimigo,
                     f"\nNível: {heroi.nivel} | Ouro: {heroi.ouro}",
                     f"Exp atual: {heroi.xp} | Exp necessária: {int((heroi.nivel ** 1.2) * 100)}"
                     "",
                     "",
                     texto_log
                     )

    return conteudo


def mostrar_hp(heroi, inimigo, log):
    """
    Inicializa o painel de exibição em tempo real do combate.
    :param heroi: Objeto heroi -> classe Heroi.
    :param inimigo: Objeto inimigo -> classe Inimigo.
    :param log: Histórico de combate coletado.
    :return: Objeto Live do rich que atualiza a interface do combate em tempo real.
    """
    console = Console()
    return Live(gerar_barras(heroi, inimigo, log), console = console, refresh_per_second = 4)


def iniciar_combate(heroi, inimigo) -> bool:
    """
    Executa a dinâmica de combate turno a turno entre herói e inimigo.
    :param heroi: Objeto heroi -> classe Heroi.
    :param inimigo: Objeto inimigo -> classe Inimigo.
    :return: True (vitória), False (derrota).
    """
    turno = 1
    log_combate = list()
    rprint(f"[bold]Iniciando o combate contra {inimigo.nome}[/]")
    print()
    with mostrar_hp(heroi, inimigo, log_combate) as live:
        while heroi.verificar_vida() and inimigo.verificar_vida():
            dano_heroi = max(1, randint(int(heroi.ataque * 0.9), int(heroi.ataque * 1.1)) - inimigo.defesa)
            dano_minimo = inimigo.ataque * 0.30
            dano_inimigo = max(int(dano_minimo), randint(int(inimigo.ataque * 0.9), int(inimigo.ataque * 1.1))  - heroi.defesa)
            inimigo.hp -= dano_heroi
            log_combate.append(f"[bold][Turno {turno}]: {heroi.nome} causou {dano_heroi} de dano em {inimigo.nome}.\n")
            live.update(gerar_barras(heroi, inimigo, log_combate))
            sleep(0.5)
            turno += 1
            if inimigo.verificar_vida():
                heroi.hp -= dano_inimigo
                log_combate.append(f"[bold][Turno {turno}]: Você sofreu {dano_inimigo} de dano de {inimigo.nome}.\n")
                turno += 1
                live.update(gerar_barras(heroi, inimigo, log_combate))
                sleep(0.5)
        if heroi.verificar_vida():
            log_combate.append(f"[bold green]O inimigo {inimigo.nome} foi derrotado![/].\n")
            live.update(gerar_barras(heroi, inimigo, log_combate))
            sleep(0.5)
            heroi.hp = min(heroi.hp_max, heroi.hp + heroi.hp_max * 0.30)
        else:
            log_combate.append(f"[bold red]Você foi morto por {inimigo.nome}[/].\n")
            live.update(gerar_barras(heroi, inimigo, log_combate))
            sleep(0.5)
    return heroi.verificar_vida()


def processar_recompensas(heroi, inimigo, inventario) -> bool:
    """
    Inicia o combate, processa as recompensas e retorna um valor booleano.
    :param heroi: Objeto heroi -> classe Heroi.
    :param inimigo: Objeto inimigo -> classe Inimigo.
    :param inventario: Dicionário com os objetos da classe Inventario.
    :return: True se o herói venceu o combate, False se o herói morreu.
    """
    combate = iniciar_combate(heroi, inimigo)
    if combate:
        dropar_itens(inimigo, inventario)
        heroi.xp += inimigo.recompensa_xp
        heroi.ouro += inimigo.recompensa_ouro
        rprint(f"[bold #FF8C00]+ {inimigo.recompensa_xp} XP[/]")
        rprint(f"[bold yellow]+ {inimigo.recompensa_ouro} Ouro[/]")
        sleep(0.5)
        xp_necessaria = int((heroi.nivel ** 1.2) * 40)
        while heroi.xp >= xp_necessaria:
            heroi.xp -= xp_necessaria
            heroi.aumentar_atributos()
            xp_necessaria = int((heroi.nivel ** 1.2) * 40)
    return combate


def processar_morte(heroi, zona, indice_zona) -> tuple:
    """
    Realoca o heroi na zona anterior e reseta as fases.
    Se não for possível realocar, apenas reseta as fases.
    :param heroi: Objeto heroi -> class Heroi.
    :param zona: Lista de objetos da classe Zona.
    :param indice_zona: Índice da zona atual na lista de zonas.
    :return: Tupla contendo o novo indice_zona e zona_atual.
    """
    heroi.hp = heroi.hp_max
    if indice_zona > 1:
        indice_zona -= 1
    return indice_zona, zona[indice_zona]


def aprimorar_equipamento(heroi, equipamento):
    """
    Utiliza o ouro coletado em combate para aprimorar os equipamentos desejados.
    :param heroi: Objeto heroi -> classe Heroi
    :param equipamento: Objeto equipamento (criado na classe Heroi) -> classe Equipamento
    :return: None
    """
    custo = equipamento.calcular_custo_upgrade()
    bonus = 0

    if equipamento.nivel < equipamento.nivel_max:
        if heroi.ouro >= custo:
            heroi.ouro -= custo
            equipamento.nivel += 1

            rprint(f"[bold green]{equipamento.nome} aprimorado(a) para o Nível {equipamento.nivel}![/]")
            rprint(f"[bold cyan]Custo: {custo} de ouro | Ouro: {heroi.ouro}[/]")

            if equipamento.nivel <= 10:
                bonus += equipamento.bonus_1
            elif equipamento.nivel <= 20:
                bonus += equipamento.bonus_2
            elif equipamento.nivel <= 30:
                bonus += equipamento.bonus_3
            elif equipamento.nivel <= 40:
                bonus += equipamento.bonus_4
            elif equipamento.nivel <= 50:
                bonus += equipamento.bonus_5
            else:
                bonus += equipamento.bonus_6

            if equipamento == heroi.arma:
                heroi.ataque += bonus
            elif equipamento == heroi.armadura:
                heroi.defesa += bonus
            else:
                heroi.hp_max += bonus
        else:
            rprint(f"[bold red]Recursos insuficientes, falta {custo - heroi.ouro} de ouro![/]")
    else:
        rprint(f"[bold red]{equipamento.nome} está no nível máximo. Vá à Forja e faça o upgrade![/]")


def dropar_itens(inimigo, inventario):
    """
    Sorteia e adiciona os itens dropados pelo inimigo ao inventário do herói.
    :param inimigo: Objeto inimigo -> classe Inimigo.
    :param inventario: Dicionário que contém os objetos da classe Inventário.
    :return: None
    """
    for item in inimigo.drops:
        if random() <= item.chance_drop:
            rprint(f"[bold #FF8C00]Drop: {item.nome} x1.[/]")
            if item.nome in inventario:
                inventario[item.nome].quantidade_item += 1
                inventario[item.nome].preco_total += item.valor_item
            else:
                inventario[item.nome] = Inventario(item.nome, 1, item.valor_item, item.valor_item)
    sleep(0.5)


def vender_itens_inventario(heroi, inventario):
    """
    Permite que o usuário venda os materiais coletados em combate.
    :param heroi: Objeto heroi -> classe Heroi.
    :param inventario: Dicionário que contèm os objetos da classe Inventário.
    :return: None
    """
    while True:
        utils.limpar_console()
        utils.mostrar_menu_principal()
        utils.mostrar_itens_inventario(inventario)
        indice = utils.validar_integer("Digite o índice do item que deseja vender: ")
        if indice <= len(inventario):
            item = list(inventario.keys())[indice - 1]
            rprint(f"[bold cyan]Item: {inventario[item].nome_item} | Quantidade: {inventario[item].quantidade_item} | "
                   f"Preço: {inventario[item].preco_total}[/]")
            quantidade = utils.validar_integer("Quantas unidades deseja vender?: ")
            if quantidade <= inventario[item].quantidade_item:
                calcular_preco = quantidade * inventario[item].preco_unitario
                rprint(f"[bold cyan]Item: {inventario[item].nome_item} | Quantidade: {quantidade} | "
                       f"Preço: {calcular_preco}[/]")
                pergunta = utils.validar_pergunta("Confirmar venda? [S/N]: ")
                if pergunta == 'S':
                    heroi.ouro += calcular_preco
                    inventario[item].quantidade_item -= quantidade
                    inventario[item].preco_total -= calcular_preco
                    if inventario[item].quantidade_item == 0:
                        del inventario[item]
                    rprint(f"[bold green]Item vendido com sucesso | Ouro Atual: {heroi.ouro}[/]")
                    sleep(1.5)
                    break
                elif pergunta == 'N':
                    break
            else:
                rprint("[bold red]Quantidade insuficiente de materiais![/]")
                sleep(1)
        elif indice == len(inventario) + 1:
            break
        else:
            rprint("[bold red]Insira um comando válido![/]")
            sleep(1)