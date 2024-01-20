def indices_tipo(lista_pos: list[int], tipo: int) -> list[int]:
    """
    Cria uma lista de inteiros que representa as posições que um determinado
    número (tipo) aparece em uma lista.

    Parameters:
        lista_pos: a lista de inteiro baseado nos acertos(2), incertezas(1) e
        erros(0) do posicionamento das letras da palavra teste comparada com a
        palavra correta.

        tipo: O inteiro a ser analisado

    Returns:
        Uma lista de inteiros com os índices de ocorrência do tipo.

    Examples:
        >>> indices_tipo([2, 0, 1, 2, 0], 2)
        [0, 3]
    """
    return [i for i, v in enumerate(lista_pos) if v == tipo]


def filtro_verde(
    palavra_teste: str, lista_pos: list[int], banco_de_palavras: set[str]
) -> tuple[set[str], set[str]]:
    """
    Filtro para identificar todas as palavras que apresentam as letras com o
    posicionamento correto.

    Parameters:
        palavra_teste: Um string que foi a palavra teste da ia.

        lista_pos: Uma lista de inteiros que representa se uma determinada
        letra está na posição correta (2), incorreta (1) ou não existe (0).

        banco_de_palavras: Um conjunto de strings com todas as palavras
        disponíveis para serem analisadas.

    Returns:
        Uma tupla que o primeiro valor será o novo conjunto banco de palavras
        que foi construido baseado no filtro e o segundo valor um conjunto com
        as letras que já passaram no filtro para evitar inconsistência.

    Examples:
        >>> palavra_teste = 'speed'
        >>> lista_pos = [0, 1, 2, 1, 0]  # crepe
        >>> banco_de_palavras = {
        ... 'crepe', 'steal', 'arise', 'creep', 'wheel', 'prece', 'soelp'
        ... }
        >>> filtro_verde(palavra_teste, lista_pos, banco_de_palavras)
        ({...}, {'e'})

    """
    visitados = set()
    novo_banco_de_palavras = set()
    tipo = 2
    lista_indices = indices_tipo(lista_pos, tipo)
    if len(lista_indices) != 0:
        for palavra in banco_de_palavras:
            if all(
                palavra_teste[indice] == palavra[indice]
                for indice in lista_indices
            ):
                novo_banco_de_palavras.add(palavra)

        if len(lista_indices) != 0:
            visitados = {palavra_teste[indice] for indice in lista_indices}
    else:
        novo_banco_de_palavras = banco_de_palavras

    return novo_banco_de_palavras, visitados


def filtro_cinza(
    palavra_teste: str,
    lista_pos: list[int],
    banco_de_palavras: set[str],
    visitados: set[str],
) -> set[str]:
    """
    Filtro para identificar todas as palavras que não apresentam uma
    determinada letra, em especifico as que estão marcadas por 0 e remover do
    banco de palavras.

    Parameters:
        palavra_teste: Um string que foi a palavra teste da ia.

        lista_pos: Uma lista de inteiros que representa se uma determinada
        letra está na posição correta (2), incorreta (1) ou não existe (0).

        banco_de_palavras: Um conjunto de strings com todas as palavras
        disponíveis para serem analisadas.

        visitados: Um conjunto de char com as letras que já foram visitadas
        por um filtro anteriormente

    Returns:
        Uma tupla que o primeiro valor será o novo conjunto banco de palavras
        que foi construído baseado no filtro

    Examples:
        >>> palavra_teste = 'speed'
        >>> lista_pos = [0, 1, 2, 1, 0]  # crepe
        >>> banco_de_palavras = {
        ... 'creep', 'prece', 'soelp', 'crepe'
        ... }
        >>> visitados = {'e', 'p'}
        >>> filtro_cinza(
        ... palavra_teste, lista_pos, banco_de_palavras, visitados
        ... )
        {...}
    """
    tipo = 0
    palavras_rejeitadas = set()
    lista_indices = indices_tipo(lista_pos, tipo)
    if len(lista_indices) != 0:
        for indice in lista_indices:
            letra = palavra_teste[indice]
            if letra in visitados:
                for palavra in banco_de_palavras:
                    if palavra_teste[indice] == palavra[indice]:
                        palavras_rejeitadas.add(palavra)
            else:
                visitados.add(letra)
                for palavra in banco_de_palavras:
                    if letra in palavra:
                        palavras_rejeitadas.add(palavra)

    return banco_de_palavras - palavras_rejeitadas


def filtro_amarelo(
    palavra_teste: str,
    lista_pos: list[int],
    banco_de_palavras: set[str],
    visitados: set[str],
) -> tuple[set[str], set[str]]:
    """
    Filtro para identificar todas as palavras que apresentam as letras que
    estão presentes na palavra porém estão na posição errada.

    Parameters:
        palavra_teste: Um string que foi a palavra teste da ia.

        lista_pos: Uma lista de inteiros que representa se uma determinada
        letra está na posição correta (2), incorreta (1) ou não existe (0).

        banco_de_palavras: Um conjunto de strings com todas as palavras
        disponíveis para serem analisadas.

        visitados: Um conjunto de char com as letras que já foram visitadas
        por um filtro anteriormente

    Returns:
        Uma tupla que o primeiro valor será o novo conjunto banco de palavras
        que foi construído baseado no filtro e o segundo valor um conjunto com
        as letras que já passaram no filtro para evitar inconsistência.

    Examples:
        >>> palavra_teste = 'speed'
        >>> lista_pos = [0, 1, 2, 1, 0]  # crepe
        >>> banco_de_palavras = {
        ... 'crepe', 'creep', 'prece', 'soelp', 'steal', 'wheel'
        ... }
        >>> visitados = {'e'}
        >>> filtro_amarelo(
        ... palavra_teste, lista_pos, banco_de_palavras, visitados
        ... )
        ({...}, {...})

    """
    tipo = 1
    novo_banco_de_palavras = set()
    lista_indices = indices_tipo(lista_pos, tipo)
    rejeitados = set()

    if len(lista_indices) != 0:
        for indice in lista_indices:
            letra = palavra_teste[indice]
            if letra in visitados:
                for palavra in banco_de_palavras:
                    if palavra_teste[indice] == palavra[indice]:
                        rejeitados.add(palavra)
            else:
                visitados.add(letra)
                for palavra in banco_de_palavras:
                    if (
                        letra in palavra
                        and palavra_teste[indice] != palavra[indice]
                    ):
                        novo_banco_de_palavras.add(palavra)
    else:
        novo_banco_de_palavras = banco_de_palavras

    return novo_banco_de_palavras - rejeitados, visitados


def executa_filtros(
    palavra_teste: str, lista_pos: list[int], banco_de_palavras: set[str]
) -> set[str]:
    """
    Função responsável por rodar os três filtros de palavras na seguinte ordem
    filtro verde depois filtro amarelo e por último filtro cinza e diminuir o
    espaço de busca para encontrar a palavra certa.

    Parameters:
        palavra_teste: Uma string que foi a palavra teste da ia.

        lista_pos: Uma lista informativa que indica se uma determinada letra
        está na posição correta (2), se está na posição incorreta (1) ou se não
        existe (0) baseada na palavra correta.

        banco_de_palavras: Um conjunto de palavras formada por 5 letras.

    Returns:
        Um conjunto com o resultado das palavras que sobraram após a passagem
        pelo os três filtros.

    Examples:
        >>> lista_pos = [0, 1, 2, 1, 0]  # crepe
        >>> banco_de_palavras = {
        ... 'crepe', 'steal', 'arise', 'creep', 'wheel', 'prece', 'soelp'
        ... }
        >>> executa_filtros('speed', lista_pos, banco_de_palavras)
        {...}
    """
    novo_banco_de_palavras, verificados = filtro_verde(
        palavra_teste, lista_pos, banco_de_palavras
    )
    novo_banco_de_palavras, verificados = filtro_amarelo(
        palavra_teste, lista_pos, novo_banco_de_palavras, verificados
    )
    novo_banco_de_palavras = filtro_cinza(
        palavra_teste, lista_pos, novo_banco_de_palavras, verificados
    )

    return novo_banco_de_palavras
