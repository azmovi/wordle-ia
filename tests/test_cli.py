from typer.testing import CliRunner

from wordle_ia.cli import app

runner = CliRunner()


def test_stdout_zero():
    result = runner.invoke(app)
    assert result.exit_code == 1
