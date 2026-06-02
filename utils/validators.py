from rich import print as rprint
from rich.console import Console


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