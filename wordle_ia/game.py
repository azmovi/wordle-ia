from random import choice

from palavras import PALAVRAS
from tabulate import tabulate
from rich.console import Console


def preprocess():
    return


def tabela():
    console = Console()
    console.print("[bold]Wordle[/bold]", justify='center')
    conteudo = [['', '', '', '', ''], ['', '', '', '', ''],['', '', '', '', ''],['', '', '', '', ''],['', '', '', '', ''],]
    tabela = tabulate(conteudo, tablefmt="simple_grid")
    console.print(tabela, justify='center')

tabela()
