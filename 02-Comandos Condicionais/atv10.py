'''Escreva um programa que leia 3 valores inteiros a, b e c e informe se eles representam os lados de um triângulo.

Três valores podem representar os lados de um triângulo se e somente se a soma de quaisquer 2 lados for maior que o terceiro lado.'''

a= int (input("Digite um valor inteiro: "))
b= int (input("Digite um valor inteiro: "))
c= int (input("Digite um valor inteiro: "))
if a + b > c or a + c > b or b + c > a:
  print("Os valores representam lados de um triângulo")
else:
  print("Os valores não representam lados de um triângulo")