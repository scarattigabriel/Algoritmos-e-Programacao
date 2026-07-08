'''Faça um código capaz de carregar 5 valores inteiros definidos pelo usuário em uma lista. Depois imprima apenas os valores pares da lista.'''

lista=[]
for i in range(5):
  num=int(input("Digite um número"))
  lista.append(num)
print(lista)
lista_pares=[]
for i in lista:
  if i % 2==0:
    lista_pares.append(i)
print(lista_pares)