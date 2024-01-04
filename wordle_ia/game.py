from random import choice

from banco_de_palavras import CONJUNTO_DE_PALAVRAS, LISTA_DE_PALAVRAS
from rich import box
from rich.console import Console
from rich.table import Table

console = Console()


def cria_o_dict_palavra_sortida(palavra: str) -> dict[str, int]:
    dict_palavra_sortida = {}

    for letra in palavra:
        if letra not in dict_palavra_sortida:
            dict_palavra_sortida[letra] = 1
        else:
            dict_palavra_sortida[letra] += 1

    return dict_palavra_sortida


PALAVRA_SORTIDA = choice(LISTA_DE_PALAVRAS)
DICT_PALAVRA_SORTIDA = cria_o_dict_palavra_sortida(PALAVRA_SORTIDA)


def palavra_valida(palavra: str) -> bool:
    if len(palavra) == 5 and palavra in CONJUNTO_DE_PALAVRAS:
        return True
    return False


def preprocess(
    palavra: str, palavra_sortida: str, dict_palavra_sortida: dict[str, int]
) -> list[str]:
    """Faz o pré-processamento da palavra"""

    lista_de_letras = [''] * 5
    palavra_lista = list(palavra)

    for i in range(5):
        letra = palavra[i]
        if letra in dict_palavra_sortida and letra == palavra_sortida[i]:
            lista_de_letras[i] = '[bold green]' + letra.upper() + '[/bold green]'
            dict_palavra_sortida[letra] -= 1
            if dict_palavra_sortida[letra] == 0:
                del dict_palavra_sortida[letra]

            palavra_lista[i] = '-'

    for i in range(5):
        letra = palavra_lista[i]
        if (
            letra.isalpha()
            and letra in dict_palavra_sortida
            and dict_palavra_sortida[letra] > 0
        ):
            lista_de_letras[i] = '[bold yellow]' + letra.upper() + '[/bold yellow]'
            dict_palavra_sortida[letra] -= 1
            palavra_lista[i] = '-'

    for i in range(5):
        if palavra_lista[i].isalpha():
            lista_de_letras[i] = '[bold]' + palavra_lista[i].upper() + '[/bold]'

    return lista_de_letras


def init_tabela() -> list[str]:
    """
    Cria uma lista que vai servir de tabela.
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
    return tabela


def __main__():
    tabela = init_tabela()
    console.print(tabela)

    for i in range(6):
        tentativa = ''  # Gambiarra
        while palavra_valida(tentativa) is False:
            tentativa = input('Informe a palavra: ')
            print(palavra_valida(tentativa))


if __name__ == '__main__':
    __main__()
