import os
from random import choice

from rich.console import Console
from typer import Typer

from wordle_ia.banco_de_palavras import CONJUNTO_DE_PALAVRAS
from wordle_ia.game import imprime_tentativa, init_table, palavra_valida

app = Typer()
console = Console()


@app.command()
def init_game():
    init_table()
    palavra_sortida = choice(list(CONJUNTO_DE_PALAVRAS))
    certo = False
    print(palavra_sortida)
    msg1 = ':party_popper: [bold green] PARABENS! [/bold green] :party_popper:'
    msg2 = ':tired_face: [bold red] VOCÊ PERDEU [/bold red] :tired_face:'
    qtd_tentativas = 0
    while qtd_tentativas < 6 and not certo:
        tentativa = ''  # Gambiarra
        while palavra_valida(tentativa) is False:
            tentativa = input('Informe a palavra: ')

        qtd_tentativas += 1
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print(qtd_tentativas)
        certo = imprime_tentativa(tentativa, palavra_sortida)
    if certo:
        console.print(msg1)
    else:
        console.print(msg2)
        console.print('[bold] A palavra correta é [/bold]', palavra_sortida)
