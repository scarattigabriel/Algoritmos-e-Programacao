'''Exercício 10: faça um programa que peça para o usuário 10 notas e imprima quantas notas são maiores ou iguais a 6'''

contador = 0
for i in range(10):
  nota=float(input("Digite sua nota: "))
  if nota >= 6:
    contador += 1
print(f"Total de notas na média: {contador}")

i = 10
contador = 0
while i >= 1:
  nota=float(input("Digite sua nota: "))
  if nota >= 6:
      contador += 1
  i -= 1
print(f"Número de notas acima da média: {contador}")