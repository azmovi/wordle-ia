from banco_palavras_possiveis import CONJUNTO_PALAVRAS_POSSIVEIS
lista = [2, 0, 2, 0, 0,]
print(lista.index(2))
cabou = False
valor = 2
lista_de_indices = []
while cabou == False:
    try:
        indice = lista.index(valor)
        lista_de_indices.append(indice)
        lista[indice] = 0
    except: 
        cabou = True
print(lista_de_indices)


for palavra in CONJUNTO_PALAVRAS_POSSIVEIS:
    print(palavra[::-1])
