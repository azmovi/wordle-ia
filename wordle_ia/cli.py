import os
from random import choice

from rich.console import Console
from typer import Typer

from wordle_ia.banco_de_palavras import CONJUNTO_PALAVRAS_SORTIDAS
from wordle_ia.game import imprime_tentativa, init_table, palavra_valida

app = Typer()
console = Console()


@app.command()
def init_game():
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
