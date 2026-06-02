import os
from time import sleep

from rich import print as rprint

from codex.database import criar_codex
from codex.services import acessar_codex
from combat.services import preparar_combate
from forge.services import forjar_equipamentos
from hero.models import Heroi
from hero.services import aprimorar_equipamentos
from hero.ui import mostrar_atributos
from inventory.services import abrir_inventario
from save.services import carregar_jogo, continuar_jogo, encerrar_jogo, salvar_jogo
from utils.console import limpar_console
from utils.ui import mostrar_menu_principal
from utils.validators import validar_integer
from zone.database import criar_zonas
from zone.services import acessar_proxima_zona, escolher_zona, repetir_zona, selecionar_zona
from zone.ui import mostrar_menu_zona


def main():
    if os.path.exists("save.json"):
        heroi = Heroi(nome="")
        rprint("Carregando o jogo...")
        sleep(1)
    else:
        heroi = Heroi(nome=input("Insira o nome do seu personagem: ").strip())

    # Cria um dicionario que armazena objetos da Classe Inventario e Classe Item
    inventario = dict()

    # Cria o objeto codex -> Classe Codex
    codex = criar_codex()

    # Cria o objeto zona -> Classe Zona e Classe Inimigo.
    zona = criar_zonas()
    fase = 0

    # Carrega os dados salvos no arquivo .json
    carregado, indice_zona = carregar_jogo(heroi, zona, inventario, codex)
    zona_atual = zona[indice_zona]

    acessar_menu_principal = False
    jogo_encerrado = False

    while True:
        fase += 1
        rprint(f"[bold #FF8C00][Zona {indice_zona + 1}] {zona_atual.nome_zona} -> Fase {fase}[/]")

        preparar_combate(fase, zona, zona_atual, indice_zona, heroi, inventario)

        if fase == 10:
            zona_atual.zona_concluida = True
            fase = 0
            salvar_jogo(heroi, zona, inventario, indice_zona, codex)
            rprint(f"[bold #FF8C00]Zona [{indice_zona + 1}] {zona_atual.nome_zona} concluída![/]")
            sleep(1)
            while True:
                mostrar_menu_zona()
                opcao = validar_integer("Escolha uma opção: ")
                match opcao:
                    case 1:
                        indice_zona, zona_atual = acessar_proxima_zona(indice_zona, zona, heroi)
                        break
                    case 2:
                        indice_zona, zona_atual = selecionar_zona(zona, indice_zona, heroi)
                        rprint(f"[bold #FF8C00]Zona atual: [{indice_zona + 1}] {zona_atual.nome_zona}.[/]")
                        sleep(0.5)
                        repetir_zona(zona, zona_atual, indice_zona, heroi, inventario)
                        salvar_jogo(heroi, zona, inventario, indice_zona, codex)
                        continue
                    case 3:
                        acessar_menu_principal = True
                        break
                    case _:
                        rprint("[bold red]Digite uma opção válida![/]")
            limpar_console()

        # Abre o menu principal.
        if acessar_menu_principal:
            while True:
                mostrar_menu_principal()
                rprint(f"[bold #FF8C00]Zona atual: [{indice_zona + 1}] {zona_atual.nome_zona}.[/]")
                menu_principal = validar_integer("Escolha uma opção: ")
                limpar_console()
                match menu_principal:

                    case 1: # Mostra atributos do heroi.
                        mostrar_atributos(heroi)

                    case 2: # Aprimora equipamentos.
                        aprimorar_equipamentos(heroi)

                    case 3: # Cria equipamentos avançados.
                        forjar_equipamentos(heroi, inventario)

                    case 4: # Abre o inventário.
                        abrir_inventario(inventario, heroi)

                    case 5: # Abre o codex e salva as alterações no arquivo .json.
                        acessar_codex(codex, inventario, heroi)
                        salvar_jogo(heroi, zona, inventario, indice_zona, codex)

                    case 6: # Mostra a lista de zonas, o status de conclusão e salva os dados no arquivo .json.
                        indice_zona, zona_atual = escolher_zona(indice_zona, zona, heroi, inventario, codex)

                    case 7: # Salva os dados no arquivo .json e reinicia a zona.
                        continuar_jogo(heroi, zona, inventario, indice_zona, codex)
                        break

                    case 8: # Salva os dados no arquivo .json e encerra o jogo.
                        encerrar_jogo(heroi, zona, inventario, indice_zona, codex)
                        jogo_encerrado = True
                        break

                    case _:
                        rprint("[bold red]ERRO: Algo aconteceu![/]")


        acessar_menu_principal = False
        if jogo_encerrado:
            break

if __name__ == "__main__":
    main()