# Wordle IA

## Setup inicial para começar o desenvolvimento
#### Poetry
- Ele é reposavel por garantir o versionamento do projeto
- Tem que entrar toda vez nele quando quiser mudar algo no codigo (não esquecer).
```bash
$ sudo apt install pip
```
```bash
$ pip install poetry
```
- Após ter instalado o poetry entra no repositorio e entra no ambiente de
desenvolvimento
```bash
$ poetry shell
```
- Se for a primeira vez usando tem que instalar os pacotes que foram adicionados
, serve também para quando uma lib nova é adicionada no repositório.
```bash
$ poetry install
```
- Para adicionar uma lib ao poetry tem que fazer o seguinte (Exemplo: numpy)
```bash 
$ poetry add numpy
```

#### Task
- É uma lib que eu adicionei para facilitar os testes de docstring. 
- Vou mostrar um exemplo de como uma função tem que ser criada para a gente não
se perder e ficar o mais padronizado possível
```py
def soma(a: int, b: int) -> int:
    """
    Faz a soma de dois inteiros 
    Parameter:
        a: inteiro a ser somado
        b: inteiro a ser somado
    Returns:
        Um inteiro como a soma dos dois parâmetros passados
    Examples:
        >>> soma(4, 5)
        9
        >>> soma(1, -1)
        0
    """
```
- Só tem que se lembrar de tipar a variavel de entrar e saida da função, a espe
cificação do `Parameter` e do `Returns` é mais para a criação da documentação, 
tem que discutir se vai querer fazer isso ainda (eu acho bom e é mais facil para
explicar no futuro)

- Para testar se a função está rodando da forma correta
```bash
$ task test
```

- Se der um problema de formatação (blue ou isort)
```bash
$ task format
```

