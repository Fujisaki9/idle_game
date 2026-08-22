from rich import print as rprint
from rich.console import Console


def validar_inteiro(mensagem: str) -> int:
    console = Console()

    while True:
        try:
            valor = int(console.input(f"[bold #FF8C00]{mensagem}[/]"))
            if valor > 0:
                return valor
            rprint("[bold red]Insira um valor numérico maior que zero![/]")
        except ValueError:
            rprint("[bold red]ERRO: Insira um valor numérico![/]")


def validar_confirmacao(mensagem: str) -> str:
    console = Console()

    while True:
        resposta = console.input(f"[bold #FF8C00]{mensagem}[/]").strip().upper()
        if resposta in ('S', 'N'):
            return resposta
        else:
            rprint("[bold red]ERRO: Digite um comando válido![/]")