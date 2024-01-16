import os
from random import choice

from rich.console import Console
from typer import Typer

from wordle_ia.banco_de_palavras import CONJUNTO_PALAVRAS_SORTIDAS
from wordle_ia.game import imprime_tentativa, init_table, palavra_valida
from wordle_ia.ia import tentativa_ia, test_tentativa

app = Typer()
console = Console()


@app.command()
def normal():
    init_table()
    palavra_sortida = choice(list(CONJUNTO_PALAVRAS_SORTIDAS))
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
        certo = imprime_tentativa(tentativa, palavra_sortida)
    if certo:
        console.print(msg1)
    else:
        console.print(msg2)
        console.print('[bold] A palavra correta é [/bold]', palavra_sortida)


@app.command()
def computer():
    init_table()
    palavra_sortida = choice(list(CONJUNTO_PALAVRAS_SORTIDAS))
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
