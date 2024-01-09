from typer import Typer 

from wordle_ia.game import init_game

app = Typer()

@app.command()
def exec():
    init_game()
    return

