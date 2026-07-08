'''Faça um programa que peça para o usuário um número inteiro e imprima quantos digitos ele possui.'''

digito= 0
num=(input("Digite um número inteiro: "))
for i in num:
  if i in '1234567890':
    digito += 1
print(digito)