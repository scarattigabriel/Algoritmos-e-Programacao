'''Uma fruteira vende maçãs com 2 preços, R$ 0,30 cada, para compras de até 12 unidades, e R$ 0,25 cada, para compras acima de 12 unidades.

Faça um programa que leia a quantidade de maçãs compradas, calcule e apresente o valor a ser pago pelo cliente.'''

numero_macas= int (input("Qual a quantidade de maças desejadas: "))
if numero_macas <= 12:
  valor_unitario = 0.30
else:
  valor_unitario = 0.25
valor_total=valor_unitario * numero_macas
print(f"O valor total da {valor_total}")
