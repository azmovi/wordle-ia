from collections import Counter

import numpy as np

from wordle_ia.banco_palavras_validas import CONJUNTO_PALAVRAS_VALIDAS
from wordle_ia.game import analise_palavra_teste


palavra_teste = 'speed'
palavra_correta = 'steal'

# Reduzir meu espaço de busca
lista_pos = analise_palavra_teste(palavra_teste, palavra_correta)
print(lista_pos)

def remove_palavras_com_cinza(
        palavra_teste: str, lista_pos: list[int], banco_de_palavras: set[str]
) -> set[str]:

    conjunto_rejeitado = set()
    for i in range(5):
        letra = palavra_teste[i]
        tipo = lista_pos[i]
        if tipo == 0:
            for palavra in banco_de_palavras:
                if letra in palavra and palavra_teste[indice1] != palavra[indice1] and :
                    conjunto_rejeitado.add(palavra)
    return banco_de_palavras - conjunto_rejeitado

def escolhe_palavras_com_verde(
        palavra_test: str, lista_pos: list[int], banco_de_palavras: set[str]
):
    novo_banco_de_palavras = set()
    for i in range(5):
        letra = palavra_test[i]
        tipo = lista_pos[i]
        if tipo == 2:
            for palavra in banco_de_palavras:
                if palavra[i] == letra:
                    novo_banco_de_palavras.add(palavra)

    return novo_banco_de_palavras


novo_conjunto = escolhe_palavras_com_verde('speed', [1, 0, 2, 0, 0], {'aback', 'newts', 'while', 'with', 'steal', 'bleart'})
    
#conjunto_novo = remove_palavras_com_cinza(palavra_teste, lista_pos, {'steal'})
print(novo_conjunto)
