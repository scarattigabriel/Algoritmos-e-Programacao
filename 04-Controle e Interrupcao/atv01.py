'''Faça um programa que imprima todos os valores de 0 a 100 menos aqueles que são múltiplos de 5.

Use o comando continue no programa.'''

for i in range(0,101):
  if i % 5==0:
    continue
  else:
    print(i)