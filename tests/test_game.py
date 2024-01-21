from wordle_ia.game import imprime_tentativa, init_table, palavra_valida


def test_palavra_deve_funcionar_com_maiusculas():
    palavra = 'WHITE'

    result = palavra_valida(palavra)
    assert result


def test_output_tabela_vazia():
    resultado = init_table()

    assert resultado is None


def test_output_tabela_com_tentativa():
    palavra = 'speed'
    lista_pos = [2, 0, 2, 0, 0]  # steal
    resultado = imprime_tentativa(palavra, lista_pos)

    assert resultado is None
