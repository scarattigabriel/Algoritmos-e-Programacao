'''Criar um algoritmo que leia os elementos de matriz inteira 5 x 5 e escreva somente os elementos abaixo da diagonal principal.'''
def ler_matriz():
    matriz = []
    print("Digite os elementos da mat5riz 5x5:")
    for i in range(5):
        linha = []
        for j in range(5):
            elemento = int(input(f"Digite o elemento [{i}][{j}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def imprimir_matriz(matriz):
    print("Matriz Original:")
    for linha in matriz:
        for elemento in linha:
            print(elemento, end=" ")
        print()  # Para mudar de linha após imprimir uma linha completa

def elementos_abaixo_diagonal(matriz):
    print("Elementos abaixo da diagonal principal:")
    for i in range(1, 5):  # Começamos em 1 para estar abaixo da diagonal principal
        for j in range(i):
            print(matriz[i][j], end=" ")
        print()  # Para mudar de linha após imprimir uma linha completa

# Exemplo de uso:
matriz = ler_matriz()
imprimir_matriz(matriz)
elementos_abaixo_diagonal(matriz)