from wordle_ia.game import palavra_valida


def test_palavra_deve_funcionar_com_maiusculas():
    palavra = 'WHITE'

    result = palavra_valida(palavra)
    assert result
