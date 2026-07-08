'''Exercício 3: faça um programa que pergunte quantos funcionários há em uma empresa. Depois, para cada funcionário, solicite o valor de seu salário e apresente o valor do salário com um aumento de 7,5%.'''

n_funcionarios = int (input("Digite o número de funcionários da empresa: "))
while n_funcionarios >= 1:
  salario_inicial= float(input("Digite seu salário"))
  salario_final= salario_inicial * 1.075
  print(f"Seu novo salario é {salario_final}")
  n_funcionarios -= 1