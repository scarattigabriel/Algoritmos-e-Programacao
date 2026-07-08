'''Crie uma função que receba dois números. Se o segundo for zero, retorne -1. Caso contrário, retorne o resultado da divisão entre os 2.'''

def divisao(n1,n2):
  if n2==0:
    return 0
  else:
    quociente= n1 / n2
    return quociente

numero_1= int(input("Digite um número: "))
numero_2= int(input("Digite o segundo número: "))
divisao(numero_1,numero_2)