# from banco_palavras_validas import CONJUNTO_PALAVRAS_VALIDAS

correta = 'float'
test = 'slate'


def retorna_lista_pos_correta(
    palavra_correta: str, palavra_test: str
) -> list[int]:
    correta = list(palavra_correta)
    test = list(palavra_test)
    posicao_correta = [0] * 5

    for i in range(5):
        if correta[i] == test[i]:
            posicao_correta[i] = 2
            test[i] = 1
            correta[i] = 0

    for i in range(5):
        if test[i] in correta:
            indice = correta.index(test[i])
            posicao_correta[i] = 1
            test[i] = 1
            correta[indice] = 0

    for i in range(5):
        t = test[i]
        if t != 0 and t != 1:
            posicao_correta[i] = 0

    return posicao_correta


print(retorna_lista_pos_correta('crepe', 'speed'))
