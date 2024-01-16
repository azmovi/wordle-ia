from collections import Counter

import numpy as np
import pandas as pd

from wordle_ia.banco_palavras_validas import CONJUNTO_PALAVRAS_VALIDAS

BANCO_REDUZIDO = CONJUNTO_PALAVRAS_VALIDAS


def create_df(banco_palavra: list[str]):
    array = np.array([list(w) for w in banco_palavra])
    df = pd.DataFrame(data=array, columns=[f'letter_{i+1}' for i in range(5)])
    df['word'] = banco_palavra
    return df


def frequencia_letra(df):
    contador = Counter()
    for i in range(5):
        contador[i + 1] = Counter(df[f'letter_{i+1}'])
    return contador


def tentativa_ia():
    return


def test_tentativa():
    return
