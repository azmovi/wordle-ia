import os
from random import choice

from rich.console import Console
from typer import Typer

from wordle_ia.banco_palavras import criar_conjunto
from wordle_ia.filtros import executa_filtros
from wordle_ia.game import (
    analise_palavra_teste,
    imprime_tentativa,
    init_table,
    palavra_valida,
)
from wordle_ia.score import melhor_palavra

app = Typer()
console = Console()

CONJUNTO_PALAVRAS_VALIDAS = criar_conjunto('wordle_ia/palavras_validas.txt')
CONJUNTO_PALAVRAS_POSSIVEIS = criar_conjunto(
    'wordle_ia/palavras_possiveis.txt'
)

MSG1 = ':party_popper: [bold green] PARABENS! [/bold green] :party_popper:'
MSG2 = ':tired_face: [bold red] VOCÊ PERDEU [/bold red] :tired_face:'
MSG3 = '[bold]Aperte ENTER para testar a próxima palavra...[/bold]'

PALAVRA_SORTIDA = choice(list(CONJUNTO_PALAVRAS_VALIDAS))


def final(certo: bool, palavra_sortida: str) -> None:
    if certo:
        console.print(MSG1)
    else:
        console.print(MSG2)
        console.print('[bold] A palavra correta é ', palavra_sortida)


@app.command()
def normal():
    os.system('cls' if os.name == 'nt' else 'clear')
    init_table()
    certo = False
    qtd_tentativas = 0
    while not certo and qtd_tentativas < 6:
        tentativa = ''  # Gambiarra
        while palavra_valida(tentativa) is False:
            tentativa = input('Informe a palavra: ')

        qtd_tentativas += 1
        os.system('cls' if os.name == 'nt' else 'clear')
        lista_posicoes = analise_palavra_teste(tentativa, PALAVRA_SORTIDA)
        imprime_tentativa(tentativa, lista_posicoes)
        certo = sum(lista_posicoes) == 10

    final(certo, PALAVRA_SORTIDA)


@app.command()
def ia():
    os.system('cls' if os.name == 'nt' else 'clear')
    tentativa = 'salet'
    certo = False
    qtd_tentativas = 0
    banco_de_palavras = CONJUNTO_PALAVRAS_POSSIVEIS
    lista_posicoes = []
    score = 3.5
    while not certo and qtd_tentativas < 6:
        if qtd_tentativas > 0:
            banco_de_palavras = executa_filtros(
                tentativa, lista_posicoes, banco_de_palavras
            )
            tentativa, score = melhor_palavra(banco_de_palavras)
            score = round(score, 2)
        lista_posicoes = analise_palavra_teste(tentativa, PALAVRA_SORTIDA)
        imprime_tentativa(tentativa, lista_posicoes)
        console.print(f'A palavra {tentativa}, teve um score de {score}')
        certo = sum(lista_posicoes) == 10
        qtd_tentativas += 1

        if not certo:
            console.print(MSG3)
            input()
            if qtd_tentativas < 6:
                os.system('cls' if os.name == 'nt' else 'clear')
    final(certo, PALAVRA_SORTIDA)
