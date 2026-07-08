'''Faça um programa que receba 5 notas, compute e imprima a média ponderada dessas notas sabendo que os pesos de cada nota são respectivamente 2, 4, 6, 8 e 10. Também imprima se o aluno seria aprovado (média maior ou igual a 6) ou não.'''

soma= 0
for i in range (5):
  notas= float(input("Digite sua nota: "))
  soma+= notas * (i*2 + 2)
media= soma/30
print(media)