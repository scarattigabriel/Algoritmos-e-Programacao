# Resolução da atividade 4
import random

def criar_matriz2d_aleatoria(linhas, colunas):
    return [[random.randint(-9, 9) for _ in range(colunas)] for _ in range(linhas)]

def estender_matriz(matriz):
    for i in range(3):
        matriz[i].extend(matriz[i][:2])
    return matriz

# Regra de Sarrus
def determinante_sarrus(matriz):
    matriz_estendida = estender_matriz(matriz)
    imprimir_matriz(matriz_estendida)
    determinante = 0
    for i in range (3):
        direto = 1
        for j in range (3):
            direto *= matriz_estendida[j][j+i]
        indireto = 1
        for j in range(3):
            indireto *= matriz_estendida[j][-j+i+2]
        determinante += direto - indireto
    return determinante

# Regra do triângulo
def determinante_triangulo(matriz):
    determinante = 0
    for i in range (3):
        direto = 1
        for j in range (3):
            coluna = j+i
            if coluna > 2:
                coluna -= 3
            direto *= matriz[j][coluna]
        indireto = 1
        for j in range(3):
            coluna = -j+i+2
            if coluna > 2:
                coluna -= 3
            indireto *= matriz[j][coluna]
        determinante += direto - indireto
    return determinante

def imprimir_matriz(matriz):
    for l in range(len(matriz)):
        for c in range(len(matriz[0])):
            print(f'[{matriz[l][c]:^5}]', end='')
        print()
    print()

A = criar_matriz2d_aleatoria(3, 3)
imprimir_matriz(A)
print(determinante_triangulo(A), end='\n\n')
print(determinante_sarrus(A))