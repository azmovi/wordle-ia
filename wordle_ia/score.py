from collections import Counter


def frequencia_letras_por_pos(
    banco_de_palavras: set[str],
) -> dict[int, dict[str, float]]:
    """
    Calcula a probabilidade da ocorrência das letras do alfabeto de acordo com
    a posição que ela se encontra na palavra.

    Parameters:
        banco_de_palavras: Um conjunto de palavras que serão a base do nosso
        cálculo de frequência

    Returns:
        Um dicionário que sua chave será a posição de análise e o valor um
        outro dicionário que terá como suave chave a letra que esta sendo
        analisada e sua chave será a probabilidade da ocorrência dessa letra.

    Examples:
        >>> banco_de_palavras = {'apple', 'white', 'crane', 'speed', 'pulse'}
        >>> frequencia_letras_por_pos(banco_de_palavras)
        {0: ...}
    """
    contador = dict()
    for i in range(5):
        contador[i] = Counter([palavra[i] for palavra in banco_de_palavras])

    frequencia = dict()
    total_por_pos = contador[0].total()

    for pos, dict_qtd_letras in contador.items():
        frequencia[pos] = {
            letra: qtd / total_por_pos
            for letra, qtd in dict_qtd_letras.items()
        }
    return frequencia


def melhor_palavra(banco_de_palavras: set[str]) -> tuple[str, float]:
    """
    Encontra a palavra que tem a maior probabilidade de aparecer baseado na
    frequência das letras em determinadas posições.

    Parameters:
        banco_de_palavras: Um conjunto de palavras com todas as possíveis
        palavras para serem escolhidas pela ia.

    Returns:
        Uma tupla que contém a palavra com a maior probabilidade de ocorrência
        e o valor aproximado da pontuação dessa palavra.

    Examples:
        >>> banco_de_palavras = {'apple', 'white', 'crane', 'speed', 'pulse'}
        >>> melhor_palavra(banco_de_palavras)
        ('apple', 1.6)
    """
    frequencias = frequencia_letras_por_pos(banco_de_palavras)
    maior_score = 0
    melhor_palavra = ''

    for palavra in banco_de_palavras:
        score = 0
        for i in range(5):
            score += frequencias[i][palavra[i]]

        if maior_score < score:
            maior_score = score
            melhor_palavra = palavra

    return melhor_palavra, round(maior_score, 2)
