def formatar_texto(texto: str) -> str:
    conectivos = ['De', 'Do', 'Da', 'Dos', 'Das', 'No', 'Na', 'O', 'A', 'Os', 'As', 'E']
    palavras_formatadas = []

    texto_splitado = texto.title().split('_')

    for indice_palavra, palavra in enumerate(texto_splitado):

        if palavra in conectivos:
            palavras_formatadas.append(palavra.lower())

        else:
            palavras_formatadas.append(palavra)

    nome_formatado = ' '.join(palavras_formatadas)
    return nome_formatado


def formatar_porcentagem(valor: float) -> str: return f"{valor * 100:.2f}%"