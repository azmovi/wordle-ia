def criar_conjunto(nome_arquivo: str) -> set[str]:
    """
    Criar um conjunto de palavras a partir de um arquivo de texto com todas as
    palavras possíveis para se jogar ou sortidas pelo próprio wordle.

    Parameters:
        nome_arquivo: o nome do arquivo txt com as palavras por linha.

    Returns:
        Um cojunto de strings com todas as palavras presentes no arquivo.

    Examples:
        criar_conjunto('palavras_validas.txt')
        {...}
    """
    conjunto = set()
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            conjunto.add(linha[0:5])
    return conjunto
