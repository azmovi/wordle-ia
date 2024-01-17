from rich import box
from rich.console import Console
from rich.table import Table

from wordle_ia.banco_palavras_possiveis import CONJUNTO_PALAVRAS_POSSIVEIS

console = Console()

LISTA_DE_TENTATIVAS = []


def palavra_valida(palavra: str) -> bool:
    """
    Verifica se a palavra a ser testada é valida.

    Parameters:
        palavra: Uma string que representa a palavra testada do usuário.
    Returns:
        Um booleano que verifica se a palavra testada é possível ou não.
    Examples:
        >>> palavra_valida('white')
        True
        >>> palavra_valida('antonio')
        False
    """

    palavra = palavra.lower()
    if len(palavra) == 5 and palavra in CONJUNTO_PALAVRAS_POSSIVEIS:
        return True
    return False


def analise_palavra_teste(palavra_teste: str, palavra_correta) -> list[int]:
    """
    Analisa o posicionamento de cada letra da palavra teste baseado no
    posicionamento das letras da palavra correta
    Parameters:
        palavra_teste: Uma string com a tentativa do usuário
        palavra_correta: Uma string que foi previamente definida de forma
        aleatório no banco de palavras
    Returns:
        Uma lista de inteiros de 5 posições, onde cada espaço representa o
        valor respectivo das letras da palavra teste, sendo esse valor igual a
        2 caso a letra está presente e na posição correta, 1 caso a letra
        exista porém na posição errada e 0 quando a letra não existe na palavra
        correta.
    Examples:
        >>> analise_palavra_teste('white', 'waist')
        [2, 0, 2, 1, 0]
    """

    correta = list(palavra_correta)
    teste = list(palavra_teste)
    posicao_correta = [0] * 5

    for i in range(5):
        if correta[i] == teste[i]:
            posicao_correta[i] = 2
            teste[i] = '1'
            correta[i] = '0'

    for i in range(5):
        if teste[i] in correta:
            indice = correta.index(teste[i])
            posicao_correta[i] = 1
            teste[i] = '1'
            correta[indice] = '0'

    for i in range(5):
        t = teste[i]
        if t != '0' and t != '1':
            posicao_correta[i] = 0

    return posicao_correta


def letra_verde(char: str) -> str:
    """
    Formata um char para ser escrito em letra maiúscula e em VERDE com o rich
    Parameters:
        char: uma letra do alfabeto
    Returns:
        Uma string com esse char formatado
    Examples:
        >>> letra_verde('a')
        '[bold green]A[/bold green]'
    """
    return '[bold green]' + char.upper() + '[/bold green]'


def letra_amarela(char: str) -> str:
    """
    Formata um char para ser escrito em letra maiúscula e em AMARELO com o rich
    Parameters:
        char: uma letra do alfabeto
    Returns:
        Uma string com esse char formatado
    Examples:
        >>> letra_amarela('a')
        '[bold yellow]A[/bold yellow]'
    """
    return '[bold yellow]' + char.upper() + '[/bold yellow]'


def letra_cinza(char: str) -> str:
    """
    Formata um char para ser escrito em letra maiúscula e em NEGRITO com o rich
    Parameters:
        char: uma letra do alfabeto
    Returns:
        Uma string com esse char formatado
    Examples:
        >>> letra_cinza('a')
        '[bold]A[/bold]'
    """
    return '[bold]' + char.upper() + '[/bold]'


def verifica_posicoes(
    palavra_teste: str, lista_posicoes: list[int]
) -> list[str]:
    """
    Formata a string baseado nas posições que as letras estão dispostas
    comparado com a palavra correta
    Parameters:
        palavra_teste: A string que foi a tentativa do usuário
        lista_posicoes: Um vetor de inteiro informando se a letra está na
        posição correta (2), se a letra existe porém não está na posição
        correta (1) e se a letra não existe (0).
    Returns:
        uma lista de strings que podem ser corretamente formatadas para a
        biblioteca rich
    Examples:
        >>> pos = analise_palavra_teste('white', 'waist')
        >>> verifica_posicoes('white', pos)
        ['[bold green]W[/bold green]', ... '[bold]E[/bold]']
    """
    lista_teste = list(palavra_teste)
    for i in range(5):
        if lista_posicoes[i] == 2:
            lista_teste[i] = letra_verde(lista_teste[i])
        elif lista_posicoes[i] == 1:
            lista_teste[i] = letra_amarela(lista_teste[i])
        else:
            lista_teste[i] = letra_cinza(lista_teste[i])

    return lista_teste


def init_table() -> None:
    """
    Cria a tabela inicial vazia.
    """
    tabela = Table(
        title='[bold]Wordle[/bold]',
        show_header=False,
        show_lines=True,
        box=box.SQUARE,
        title_justify='center',
    )
    for i in range(6):
        tabela.add_row(' ', ' ', ' ', ' ', ' ')

    console.print(tabela)
    return


def imprime_tentativa(tentativa: str, lista_de_posicoes: list[int]) -> None:
    """
    Usa o rich para imprimir a palavra tentativa do usuário além de mostrar se
    a palavra testada é a correta ou não
    Parameters:
        tentativa: a palavra tentativa do usuário.
        lista_de_posicoes: uma lista de inteiro definido as posições das letras
    """
    lista_de_mensagem = verifica_posicoes(tentativa, lista_de_posicoes)
    LISTA_DE_TENTATIVAS.append(lista_de_mensagem)
    tabela = create_table()

    for letras in LISTA_DE_TENTATIVAS:
        tabela.add_row(*letras)

    for _ in range(6 - len(LISTA_DE_TENTATIVAS)):
        tabela.add_row(' ', ' ', ' ', ' ', ' ')

    console.print(tabela)
    return


def create_table() -> Table:
    """
    Cria uma tabela com o setup especifico e vazia
    Returns:
        Uma tabela do rich com o setup do wordle
    Examples:
        >>> create_table()
        <...>
    """
    tabela = Table(
        title='[bold]Wordle[/bold]',
        show_header=False,
        show_lines=True,
        box=box.SQUARE,
        title_justify='center',
    )
    return tabela
