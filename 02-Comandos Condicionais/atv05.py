'''Escreva um programa para ler 2 valores inteiros e indicar qual dos dois valores é o maior, ou se eles são iguais.'''

numero1= int (input("Digite um número inteiro: "))
numero2= int (input("Digite um número inteiro: "))
if numero1 > numero2:
  print(f"O número {numero1} é maior que o número {numero2} ")
elif numero1 < numero2:
  print(f"O número {numero2} é maior que o número {numero1} ")
else:
  print (f"Os números {numero1} e {numero2} são iguais")