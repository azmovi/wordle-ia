# from banco_palavras_validas import CONJUNTO_PALAVRAS_VALIDAS

correta = 'float'
test = 'slate'


def retorna_lista_pos_correta(
    palavra_correta: str, palavra_test: str
) -> list[int]:
    lista_palavra_correta = list(palavra_correta)
    lista_palavra_test = list(palavra_test)
    lista_posicao_correta = [0] * 5

    for idx, (c, t) in enumerate(
        zip(lista_palavra_correta, lista_palavra_test)
    ):
        if c == t:
            lista_posicao_correta[idx] = 2
            lista_palavra_test[idx] = 1
            lista_palavra_correta[idx] = 0

    for idx, t in enumerate(lista_palavra_test):
        if t in lista_palavra_correta:
            indice = lista_palavra_correta.index(t)
            lista_posicao_correta[idx] = 1
            lista_palavra_test[idx] = 1
            lista_palavra_correta[indice] = 0

    for idx, t in enumerate(lista_palavra_test):
        if t != 0 and t != 1:
            lista_posicao_correta[idx] = 0

    return lista_posicao_correta


print(retorna_lista_pos_correta('crepe', 'speed'))
