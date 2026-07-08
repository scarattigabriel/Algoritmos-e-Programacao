'''Exercício 1: crie uma função recursiva que compute o fatorial de um número inteiro.'''

def fatorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fatorial(n-1) 
    
n = int(input("Digite o número que deseja calcular o fatorial: "))
print(fatorial(n))