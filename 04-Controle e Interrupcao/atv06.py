'''Escreva um programa para verificar se um número natural digitado pelo usuário é um número primo (um número é primo quando ele é maior que 1 e ele é divisível apenas por 1 e por ele mesmo).'''

cont=0
while True:
  num= int(input("Digite um número natural: "))
  if num < 1:
    print("Número inválido!")
    continue
  else:
    for i in range(num):
      i+=1
      if num % i == 0:
        cont+=1
    if cont==2:
          print("É um número primo!")
    else:
          print("Não é um número primo!")
  break