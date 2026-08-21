from time import sleep

from rich import print as rprint

from combate.servicos import preparar_combate
from jogo.servicos import executar_menu_principal, executar_menu_zona_concluida, inicializar_jogo
from persistencia.servicos import salvar_progresso_jogo
from utilitario.console import limpar_console


def main():
    heroi, inventario, codex, zonas, indice_zona, zona_atual = inicializar_jogo()
    fase = 0

    while True:
        fase += 1
        rprint(f"[bold #FF8C00][Zona {indice_zona + 1}] {zona_atual.nome_zona} -> Fase {fase}[/]")

        preparar_combate(fase, zonas, zona_atual, indice_zona, heroi, inventario)
        acessar_menu_principal = False

        if fase == 10:
            zona_atual.zona_concluida = True
            fase = 0
            salvar_progresso_jogo(heroi, zonas, inventario, indice_zona, codex)
            rprint(f"[bold #FF8C00]Zona [{indice_zona + 1}] {zona_atual.nome_zona} concluída![/]")
            sleep(1)

            indice_zona, zona_atual, acessar_menu_principal = executar_menu_zona_concluida(
                indice_zona, zonas, zona_atual, heroi, inventario
            )
            limpar_console()

        if acessar_menu_principal:
            indice_zona, zona_atual, _, jogo_encerrado = executar_menu_principal(
                indice_zona, zonas, zona_atual, heroi, inventario, codex
            )
            if jogo_encerrado:
                break


if __name__ == "__main__":
    main()