'''
Construir um programa que leia dois números e efetue a adição. Caso o valor somado seja maior que 20, este deverá ser apresentado somando-se a ele mais 8; caso o valor somado seja menor ou igual a 20, este deverá ser apresentado subtraindo-se 5.'''

numero1=float(input("Digite o primeiro número: "))
numero2=float(input("Digite o segundo número: "))
resultado = numero1 + numero2
if resultado > 20:
  resultado = resultado + 8
else:
  resultado = resultado - 5
print(f"Resultado {resultado}")