from type.testing import CliRunner
from wordle_ia.cli import app

runner = CliRunner()

def game_retorna_0():
    result = runner.invoke(app)
    assert result.exit_code == 0
