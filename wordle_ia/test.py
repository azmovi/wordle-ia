from banco_palavras_possiveis import CONJUNTO_PALAVRAS_POSSIVEIS


def indices_tipo(lista_pos: list[int], tipo: int) -> list[int]:
    return [i for i, v in enumerate(lista_pos) if v == tipo]


def palavra_com_duplicata(palavra_teste: str) -> tuple[list[str], bool]:
    letras_vistas = set()
    letras_duplicadas = []

    for letra in palavra_teste:
        if letra in letras_vistas and letra not in letras_duplicadas:
            letras_duplicadas.append(letra)
        else:
            letras_vistas.add(letra)

    return len(letras_duplicadas) != 0, letras_duplicadas


def remove_palavras_com_cinza(
    palavra_teste: str,
    lista_pos: list[int],
    banco_de_palavras: set[str],
    visitados: set[str],
) -> set[str]:

    tipo = 0
    conjunto_rejeitado = set()
    novo_visitados = visitados.copy()
    lista_indices = indices_tipo(lista_pos, tipo)

    for indice in lista_indices:
        letra = palavra_teste[indice]
        if letra not in novo_visitados:
            novo_visitados.add(letra)
            for palavra in banco_de_palavras:
                if letra in palavra:
                    conjunto_rejeitado.add(palavra)

    return banco_de_palavras - conjunto_rejeitado, novo_visitados


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
    novo_banco_de_palavras = set()
    novo_visitados = visitados.copy()
    lista_indices = indices_tipo(lista_pos, tipo)

    for indice in lista_indices:
        letra = palavra_teste[indice]
        if letra not in novo_visitados:
            novo_visitados.add(letra)
            for palavra in banco_de_palavras:
                if letra in palavra:
                    novo_banco_de_palavras.add(palavra)

    return novo_banco_de_palavras, novo_visitados


palavra_test = 'speed'
lista_pos = [0, 1, 2, 1, 0]  # crepe

visitados = set()
banco_de_palavras = CONJUNTO_PALAVRAS_POSSIVEIS

novo_banco, novo_visitados = escolhe_palavras_com_verde(
    palavra_test, lista_pos, banco_de_palavras
)
print(novo_banco, novo_visitados)

novo_banco, novo_visitados = remove_palavras_com_cinza(
        palavra_test, lista_pos, novo_banco, novo_visitados
)
print(novo_banco, novo_visitados)

print(escolhe_palavras_com_amarelo(
    palavra_test, lista_pos, novo_banco, novo_visitados
))
