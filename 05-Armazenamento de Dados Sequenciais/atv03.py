'''
Leia um número indefinido de valores, até que o usuário digite o valor 0. Em seguida, mostre qual é o menor e qual é o maior valor da lista.'''

lista_num=[]
while True:
  num=float(input("Digite um número: "))
  if num == 0:
    break
  else:
    lista_num.append(num)
print("O maior número da lista é: ", max(lista_num),"\nO menor número da lista é: ", min(lista_num))