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


def formatar_porcentagem(valor):
    return f"{valor * 100:.2f} %"