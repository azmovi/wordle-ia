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
    # jprint(palavra_sortida)
    while not certo:
        tentativa = ''  # Gambiarra
        while palavra_valida(tentativa) is False:
            tentativa = input('Informe a palavra: ')

        os.system('cls' if os.name == 'nt' else 'clear')
        certo = imprime_tentativa(tentativa, palavra_sortida)
    console.print(
        ':party_popper: [bold green] PARABENS! [/bold green] :party_popper:'
    )
