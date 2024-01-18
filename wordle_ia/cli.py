import os
from random import choice

from rich.console import Console
from typer import Typer

from wordle_ia.banco_palavras_validas import CONJUNTO_PALAVRAS_VALIDAS
from wordle_ia.game import (
    analise_palavra_teste,
    imprime_tentativa,
    init_table,
    palavra_valida,
)

app = Typer()
console = Console()


@app.command()
def normal():
    init_table()
    palavra_sortida = choice(list(CONJUNTO_PALAVRAS_VALIDAS))
    certo = False
    # print(palavra_sortida)
    msg1 = ':party_popper: [bold green] PARABENS! [/bold green] :party_popper:'
    msg2 = ':tired_face: [bold red] VOCÊ PERDEU [/bold red] :tired_face:'
    qtd_tentativas = 0
    while not certo and qtd_tentativas < 6:
        tentativa = ''  # Gambiarra
        while palavra_valida(tentativa) is False:
            tentativa = input('Informe a palavra: ')

        qtd_tentativas += 1
        os.system('cls' if os.name == 'nt' else 'clear')
        lista_posicoes = analise_palavra_teste(tentativa, palavra_sortida)
        imprime_tentativa(tentativa, lista_posicoes)
        certo = sum(lista_posicoes) == 10

    if certo:
        console.print(msg1)
    else:
        console.print(msg2)
        console.print('[bold] A palavra correta é [/bold]', palavra_sortida)


@app.command()
def computer():
    init_table()
    palavra_sortida = choice(list(CONJUNTO_PALAVRAS_VALIDAS))
    palavra_inicial = 'salet'
    certo = False
    # print(palavra_sortida)
    msg1 = ':party_popper: [bold green] PARABENS! [/bold green] :party_popper:'
    msg2 = ':tired_face: [bold red] VOCÊ PERDEU [/bold red] :tired_face:'
    qtd_tentativas = 0
    analise_palavra, banco_reduzido = test_tentativa(palavra_inicial)
    while not certo and qtd_tentativas < 6:
        tentativa = tentativa_ia(analise_palavra, banco_reduzido)
        os.system('cls' if os.name == 'nt' else 'clear')
        certo = imprime_tentativa(tentativa, palavra_sortida)
    if certo:
        console.print(msg1)
    else:
        console.print(msg2)
        console.print('[bold] A palavra correta é [/bold]', palavra_sortida)
