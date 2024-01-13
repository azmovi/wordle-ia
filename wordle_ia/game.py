from rich import box
from rich.console import Console
from rich.table import Table

from wordle_ia.banco_de_palavras import CONJUNTO_TODAS_PALAVRAS

console = Console()

LISTA_DE_TENTATIVAS = []


def cria_o_dict_palavra_sortida(palavra: str) -> dict[str, int]:
    """
    Cria um dicionario com a quantidade de cada letra presente da palavra
    sortida

    Parameters:
        palavra: Uma string que representa a palavra sortida.
    Returns:
        Um dicionario onde as chaves são as letras e os itens a quantidade de
        vezes que essa letra aparece.
    Examples:
        >>> cria_o_dict_palavra_sortida('palavra')
        {'p': 1, 'a': 3, 'l': 1, 'v': 1, 'r': 1}
    """
    dict_palavra_sortida = {}

    for letra in palavra:
        if letra not in dict_palavra_sortida:
            dict_palavra_sortida[letra] = 1
        else:
            dict_palavra_sortida[letra] += 1

    return dict_palavra_sortida


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
    if len(palavra) == 5 and palavra in CONJUNTO_TODAS_PALAVRAS:
        return True
    return False


def cria_lista_letra(
    palavra: str, palavra_sortida: str
) -> tuple[list[str], bool]:
    """
    Faz o pré-processamento da palavra para conseguir colocar na tabela
    Parameters:
        palavra: a string escolhida pelo usuário
    Returns:
        Uma tupla com dois valores, o primeiro sendo uma lista com as letras
        formatadas e um booleano representando se a palavra teste foi correta
        ou não
    Example:
        >>> cria_lista_letra('white', 'white')
        (['[bold green]W[/bold green]', ...], True)
        >>> cria_lista_letra('piece', 'white')
        (['[bold]P[/bold]', ...], False)
    """

    lista_de_letras = [''] * 5
    palavra_lista = list(palavra)
    dict_palavra_sortida = cria_o_dict_palavra_sortida(palavra_sortida)

    for i in range(5):
        letra = palavra[i]
        if letra in dict_palavra_sortida and letra == palavra_sortida[i]:
            lista_de_letras[i] = (
                '[bold green]' + letra.upper() + '[/bold green]'
            )
            dict_palavra_sortida[letra] -= 1
            if dict_palavra_sortida[letra] == 0:
                del dict_palavra_sortida[letra]

            # Veriricar se acertou a palavra
            if len(dict_palavra_sortida) == 0:
                return lista_de_letras, True

            palavra_lista[i] = '-'

    for i in range(5):
        letra = palavra_lista[i]
        if (
            letra.isalpha()
            and letra in dict_palavra_sortida
            and dict_palavra_sortida[letra] > 0
        ):
            lista_de_letras[i] = (
                '[bold yellow]' + letra.upper() + '[/bold yellow]'
            )
            dict_palavra_sortida[letra] -= 1
            palavra_lista[i] = '-'

    for i in range(5):
        if palavra_lista[i].isalpha():
            lista_de_letras[i] = (
                '[bold]' + palavra_lista[i].upper() + '[/bold]'
            )

    return lista_de_letras, False


def init_table() -> None:
    """
    Cria a tabela inicial vazia.
    Examples:
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


def imprime_tentativa(tentativa: str, palavra_sortida: str) -> bool:
    """
    Usa o rich para imprimir a palavra tentativa do usuário além de mostrar se
    a palavra testada é a correta ou não
    Parameters:
        tentativa: a palavra tentativa do usuário.
        palavra_sortida: a palavra a ser acertada pelo usuário.
    Returns:
        Um booleano que representa se a palavra teste é a correta.
    Examples:
    """
    lista_de_letras, certo = cria_lista_letra(tentativa, palavra_sortida)
    certo, LISTA_DE_TENTATIVAS.append(lista_de_letras)
    tabela = create_table()

    for letras in LISTA_DE_TENTATIVAS:
        tabela.add_row(*letras)

    for _ in range(6 - len(LISTA_DE_TENTATIVAS)):
        tabela.add_row(' ', ' ', ' ', ' ', ' ')

    console.print(tabela)
    return certo


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
