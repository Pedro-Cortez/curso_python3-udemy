listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

comparativo_a = list()
comparativo_b = list()
cont = 0
final = len(listas_de_inteiros) - 1

while cont <= final: 
    for numero in listas_de_inteiros[cont]:
        if numero not in comparativo_a:
            comparativo_a.append(numero)
        else:
            comparativo_b.append(numero)
    if len(comparativo_b) != 0:
        print(f'{comparativo_b[0]} -> {listas_de_inteiros[cont]}')
    elif len(comparativo_b) == 0:
        print(f'-1 -> {listas_de_inteiros[cont]}')
    comparativo_a.clear()
    comparativo_b.clear()
    cont += 1
