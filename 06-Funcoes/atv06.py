'''
Crie um programa que declare uma lista de 10 inteiros. Em seguida, chame uma função que receba como parâmetro a lista e retorne qual o menor elemento do conjunto (sem usar a função min do Python).'''

def menor_elemento(lista):
  menor=lista[0]
  for i in lista:
    if menor > i:
      menor= i
  return menor
lista=[]
for i in range(10):
  numero=int(input("Digite um número: "))
  lista.append(numero)
menor_elemento(lista)