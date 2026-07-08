'''Exercício 1: Crie uma função que receba como parâmetro uma matriz de números inteiros e retorne uma lista contendo apenas os números pares dessa lista. Imprima a lista resultado.'''

matriz = [
    [1, 2, 0],
    [4, 5, 6],
    [7, 8, 9]]



def obter_pares(matriz):
    pares = []
    for linha in matriz:
        for coluna in linha:
            if coluna % 2 == 0:
                pares.append(coluna)
    return pares

resultado = obter_pares(matriz)
print("Números pares:", resultado)

