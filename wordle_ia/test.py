from banco_palavras_possiveis import CONJUNTO_PALAVRAS_POSSIVEIS


def indices_tipo(lista_pos: list[int], tipo: int) -> list[int]:
    return [i for i, v in enumerate(lista_pos) if v == tipo]


def remove_palavras_com_cinza(
    palavra_teste: str,
    lista_pos: list[int],
    banco_de_palavras: set[str],
    visitados: set[str],
) -> set[str]:

    tipo = 0
    lista_indices = indices_tipo(lista_pos, tipo)
    novo_banco_de_palavras = set()

    for indice in lista_indices:
        letra = palavra_teste[indice]
        if letra not in novo_visitados:
            visitados.add(letra)
            for palavra in banco_de_palavras:
                if letra not in palavra:
                    novo_banco_de_palavras.add(palavra)

    return novo_banco_de_palavras, visitados


def escolhe_palavras_com_verde(
    palavra_teste: str, lista_pos: list[int], banco_de_palavras: set[str]
):
    tipo = 2
    novo_banco_de_palavras = set()
    lista_indices = indices_tipo(lista_pos, tipo)

    for palavra in banco_de_palavras:
        if all(
            palavra_teste[indice] == palavra[indice]
            for indice in lista_indices
        ):
            novo_banco_de_palavras.add(palavra)

    visitados = {palavra_teste[indice] for indice in lista_indices}

    return novo_banco_de_palavras, visitados


def escolhe_palavras_com_amarelo(
    palavra_teste: str,
    lista_pos: list[int],
    banco_de_palavras: set[str],
    visitados: set[str],
) -> tuple[set[str], set[str]]:

    tipo = 1
    lista_indices = indices_tipo(lista_pos, tipo)
    novo_banco_de_palavras = set()

    for indice in lista_indices:
        letra = palavra_teste[indice]
        if letra not in novo_visitados:
            visitados.add(letra)
            for palavra in banco_de_palavras:
                if letra in palavra:
                    novo_banco_de_palavras.add(palavra)

    return novo_banco_de_palavras, visitados


palavra_test = 'speed'
lista_pos = [0, 1, 2, 1, 0]  # crepe

visitados = set()
banco_de_palavras = CONJUNTO_PALAVRAS_POSSIVEIS

novo_banco, novo_visitados = escolhe_palavras_com_verde(
    palavra_test, lista_pos, banco_de_palavras
)

print(novo_banco, novo_visitados)


novo_banco, novo_visitados = escolhe_palavras_com_amarelo(
    palavra_test, lista_pos, novo_banco, novo_visitados
)

print(novo_banco, novo_visitados)

print(remove_palavras_com_cinza(
        palavra_test, lista_pos, novo_banco, novo_visitados
))
