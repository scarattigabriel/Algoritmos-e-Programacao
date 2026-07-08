'''Faça um programa que leia 2 números e informe se o primeiro é ou não múltiplo do segundo.'''
numero_1= float (input("Informe um número: "))
numero_2= float (input("Informe o segundo número: "))
if numero_1 % numero_2==0 :
  print(f"O número {numero_1} é multiplo do número {numero_2}")
else :
  print(f"O número {numero_1} não é multiplo do número {numero_2}")
