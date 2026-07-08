'''Exercício 2: use o operador ternário para identificar e imprimir se o número informado pelo usuário é par ou é ímpar'''

numero= int(input("Digite um número: "))
if numero % 2 == 0:
  print(f"O número é par")
else:
  print("O número é ímpar")

numero= int (input("Digite um número: "))
print("O número é","par" if numero % 2 == 0 else"ímpar")
