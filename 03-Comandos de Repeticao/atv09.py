'''Escreva um programa que recebe um número inteiro positivo e retorna a quantidade de divisores positivos que ele possui.'''
acumulador=0
num= int(input("Digite um número inteiro: "))
if num >=0:
  for i in range(num):
    if num%(i+1)==0:
      acumulador+=1
  print(acumulador)
else:
  print("Erro")