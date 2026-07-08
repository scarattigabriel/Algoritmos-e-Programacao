'''Exercício 2: Crie uma função que receba uma matriz (lista de listas) e retorne a soma de todos os elementos da matriz, e imprima o resultado.'''

matriz = [
    [1, 2, 0],
    [4, 5, 6],
    [7, 8, 9]]

def somar_matriz(matriz):
    soma = 0
    for linha in matriz:
        for elemento in linha:
            soma += elemento
    return soma

resultado = somar_matriz(matriz)
print("Soma dos elementos da matriz: ", resultado)