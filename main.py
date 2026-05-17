from characters import Heroi
from rich import print as rprint
import copy, utils, database, save, game, services


def main():
    # Cria o objeto heroi -> Classe Heroi.
    heroi = Heroi(nome = "Fujisaki")

    # Cria um dicionario que armazena objetos da Classe Inventario e Classe Item
    inventario = dict()

    # Cria o objeto zona -> Classe Zona e Classe Inimigo.
    zona = database.criar_zonas()
    fase = 0

    # Carrega os dados salvos no arquivo .json
    carregado, indice_zona = save.carregar_jogo(heroi, zona, inventario)
    zona_atual = zona[indice_zona]

    acessar_menu_principal = False
    encerrar_jogo = False

    while True:
        fase += 1
        rprint(f"[bold #FF8C00][Zona {indice_zona + 1}] {zona_atual.nome_zona} -> Fase {fase}[/]")

        # Inicia o combate contra monstros aleatórios da zona.
        if fase < 10:
            inimigo = zona_atual.gerar_inimigo()
            combate = services.processar_recompensas(heroi, inimigo, inventario)
            if not combate:
                indice_zona, zona_atual = services.processar_morte(heroi, zona, indice_zona)
                fase = 0
            utils.limpar_console()

        # Inicia o combate contra boss.
        else:
            inimigo = copy.deepcopy(zona_atual.boss)
            combate = services.processar_recompensas(heroi, inimigo, inventario)
            if not combate:
                indice_zona, zona_atual = services.processar_morte(heroi, zona, indice_zona)
                fase = 0
            else:

                # Abre o menu de opções após a conclusão da zona.
                utils.limpar_console()
                utils.mostrar_menu_zona()
                rprint(f"[bold #FF8C00]Zona [{indice_zona + 1}] {zona_atual.nome_zona} concluída![/]")
                while True:
                    opcao = utils.validar_integer("Escolha uma opção: ")
                    match opcao:
                        case 1:
                            indice_zona, zona_atual = game.acessar_proxima_zona(indice_zona, zona, heroi)
                            break
                        case 2:
                            break
                        case 3:
                            acessar_menu_principal = True
                            break
                        case _:
                            rprint("[bold red]Digite uma opção válida![/]")
            utils.limpar_console()

        # Reseta a zona, modifica o status de conclusão e salva os dados no arquivo .json.
        if fase == 10:
            zona_atual.zona_concluida = True
            save.salvar_jogo(heroi, zona, inventario, indice_zona)
            fase = 0

        # Abre o menu principal.
        if acessar_menu_principal:
            while True:
                utils.mostrar_menu_principal()
                rprint(f"[bold #FF8C00]Zona atual: [{indice_zona + 1}] {zona_atual.nome_zona}.[/]")
                menu_principal = utils.validar_integer("Escolha uma opção: ")
                utils.limpar_console()
                match menu_principal:

                    case 1: # Mostra atributos do heroi.
                        game.mostrar_atributos(heroi)

                    case 2: # Aprimora equipamentos.
                        game.aprimorar_equipamentos(heroi)

                    case 3: # Cria equipamentos avançados.
                        game.forjar_equipamentos(heroi, inventario)

                    case 4: # Abre o inventário.
                        game.mostrar_inventario(inventario, heroi)

                    case 5: # Mostra a lista de zonas, o status de conclusão e salva os dados no arquivo .json.
                        indice_zona, zona_atual = game.escolher_zona(indice_zona, zona, heroi, inventario)

                    case 6: # Salva os dados no arquivo .json e reinicia a zona.
                        game.continuar_jogo(heroi, zona, inventario, indice_zona)
                        break

                    case 7: # Salva os dados no arquivo .json e encerra o jogo.
                        game.encerrar_jogo(heroi, zona, inventario, indice_zona)
                        encerrar_jogo = True
                        break

                    case _:
                        rprint("[bold red]ERRO: Algo aconteceu![/]")


        acessar_menu_principal = False
        if encerrar_jogo:
            break

if __name__ == "__main__":
    main()