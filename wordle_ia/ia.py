# from wordle_ia.game import analise_palavra_teste

# Filtro_verde -> Filtro_Amarelo -> Filtro_Cinza
# Evitar a ocorre de uma duplicada sendo verde ou amarela


def indices_tipo(lista_pos: list[int], tipo: int) -> list[int]:
    return [i for i, v in enumerate(lista_pos) if v == tipo]


def filtro_verde(
    palavra_teste: str, lista_pos: list[int], banco_de_palavras: set[str]
) -> tuple[set[str], set[str]]:
    novo_banco_de_palavras = set()
    tipo = 2
    lista_indices = indices_tipo(lista_pos, tipo)

    for palavra in banco_de_palavras:
        if all(
            palavra_teste[indice] == palavra[indice]
            for indice in lista_indices
        ):
            novo_banco_de_palavras.add(palavra)

    visitados = {palavra_teste[indice] for indice in lista_indices}

    return novo_banco_de_palavras, visitados


def filtro_cinza(
    palavra_teste: str,
    lista_pos: list[int],
    banco_de_palavras: set[str],
    visitados: set[str],
) -> set[str]:

    tipo = 0
    novo_banco_de_palavras = set()
    lista_indices = indices_tipo(lista_pos, tipo)

    for indice in lista_indices:
        letra = palavra_teste[indice]
        if letra not in visitados:
            visitados.add(letra)
            for palavra in banco_de_palavras:
                if letra not in palavra:
                    novo_banco_de_palavras.add(palavra)

    return novo_banco_de_palavras, visitados


def filtro_amarelo(
    palavra_teste: str,
    lista_pos: list[int],
    banco_de_palavras: set[str],
    visitados: set[str],
) -> tuple[set[str], set[str]]:

    tipo = 1
    novo_banco_de_palavras = set()
    lista_indices = indices_tipo(lista_pos, tipo)

    for indice in lista_indices:
        letra = palavra_teste[indice]
        if letra not in visitados:
            visitados.add(letra)
            for palavra in banco_de_palavras:
                if letra in palavra:
                    novo_banco_de_palavras.add(palavra)

    return novo_banco_de_palavras, visitados
