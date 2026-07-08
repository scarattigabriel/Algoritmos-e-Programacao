'''Crie duas matrizes 4x4 e crie uma função que faça a multiplicação da primeira matriz pela segunda e retorne a matriz resultante. Depois chame a função e imprima a matriz resultante.'''

import random

def criar_matriz2d(linhas, colunas, valor_inicial = 0):
    return [[valor_inicial for _ in range(colunas)] for _ in range(linhas)]

def criar_matriz2d_aleatoria(linhas, colunas):
    return [[random.randint(-9, 9) for _ in range(colunas)] for _ in range(linhas)]

def multMatriz(A, B):
    if(len(A[0]) != len(B)):
        print(f"Não é possível multiplicar a matriz A({len(A)}x{len(A[0])}) por B({len(B)}x{len(B[0])})")
        return None

    resultado = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]


    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                resultado[i][j]+=A[i][k] * B[k][j]

    return resultado

def imprimirMatriz(matriz):
    for l in range(len(matriz)):
        for c in range(len(matriz[0])):
            print(f'[{matriz[l][c]:^5}]', end='') #Reserva um espaço de 5 posicoes para o número. ^ centraliza o número dentro das posicoes. end para nao pular linha
        print()
    print()

A = criar_matriz2d_aleatoria(2, 3)
B = criar_matriz2d_aleatoria(3, 4)
C = multMatriz(A, B)

imprimirMatriz(A)
imprimirMatriz(B)
if C!= None:
    imprimirMatriz(C)