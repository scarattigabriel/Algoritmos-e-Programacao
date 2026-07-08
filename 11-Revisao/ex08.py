'''Exercício 8: Crie uma função que receba uma matriz, e conte quantos elementos pares tem na diagonal principal e na adjacente.'''

def contar_pares_diagonais(matriz):
    pares_principal = 0
    pares_adjacente = 0
    n = len(matriz)
    for i in range(n):
        if matriz[i][i] % 2 == 0:
            pares_principal += 1
        if matriz[i][n - 1 - i] % 2 == 0:
            pares_adjacente += 1
    return (pares_principal, pares_adjacente)
matriz = [
    [2, 4, 3,  11],
    [5, 6, 8,   7],
    [9, 1, 10, 12],
    [4, 7, 5,  14]
]
print(contar_pares_diagonais(matriz))

