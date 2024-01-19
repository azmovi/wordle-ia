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
def ia():
    # Arrumar o filtro ou está excluindo de mais ou de menos
    # Arrumar para a ia nem sempre escolher a melhor palavra

    palavra_sortida = choice(list(CONJUNTO_PALAVRAS_VALIDAS))
    palavra_inicial = 'salet'
    certo = False
    msg1 = ':party_popper: [bold green] PARABENS! [/bold green] :party_popper:'
    msg2 = ':tired_face: [bold red] VOCÊ PERDEU [/bold red] :tired_face:'
    msg3 = '[bold]Aperte ENTER para testar a próxima palavra...[/bold]'
    qtd_tentativas = 0
    banco_de_palavras = CONJUNTO_PALAVRAS_POSSIVEIS
    lista_posicoes = []
    tentativa = palavra_inicial
    score = 3.5
    while not certo and qtd_tentativas < 6:
        if qtd_tentativas > 0:
            banco_de_palavras = executa_filtros(
                tentativa, lista_posicoes, banco_de_palavras
            )
            tentativa, score = melhor_palavra(banco_de_palavras)
            if len(tentativa) == 0:
                print('FUDEU')
                break

        lista_posicoes = analise_palavra_teste(tentativa, palavra_sortida)
        imprime_tentativa(tentativa, lista_posicoes)
        console.print(f'A palavra {tentativa}, teve um score de {score}')
        console.print(msg3)
        console.print(len(banco_de_palavras))
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
        qtd_tentativas += 1
        certo = sum(lista_posicoes) == 10

    if certo:
        console.print(msg1)
    else:
        console.print(msg2)
        console.print('[bold] A palavra correta é [/bold]', palavra_sortida)
