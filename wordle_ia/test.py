
def cria_o_dict_palavra_sortida(palavra: str) -> dict[str, int]:
    dict_palavra_sortida = {}

    for letra in palavra:
        if letra not in dict_palavra_sortida:
            dict_palavra_sortida[letra] = 1
        else:
            dict_palavra_sortida[letra] += 1

    return dict_palavra_sortida


palavra = 'valha'
palavra_sortida = 'praia'
DICT_PALAVRA_SORTIDA = cria_o_dict_palavra_sortida(palavra_sortida)

lista = preprocess(palavra, palavra_sortida, DICT_PALAVRA_SORTIDA)
print(lista)
