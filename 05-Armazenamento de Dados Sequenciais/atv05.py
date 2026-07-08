'''
Faça um programa que leia cinco (5) valores em uma lista e, ao final, imprima-os de forma ordenada sem usar a função sort().'''

lista_ordenada=[]
lista=[]
for i in range(5):
  num=int (input("Digite um valor: "))
  lista.append(num)
for i in range(len(lista)):
  lista_ordenada.append(min(lista))
  lista.remove(min(lista))
print(lista_ordenada)