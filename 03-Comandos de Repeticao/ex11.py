'''Exercício 11: faça um programa que peça para o usuário 10 notas e imprima a média aritmética dessas notas com duas casas decimais.'''
acumulador=0
for i in range(10):
  nota= float(input("Digite sua nota: "))
  acumulador += nota
media= acumulador / 10
print(f"A média final das notas é: {media:.2f}")

acumulador= 0
i = 10
while i >=1:
    nota=float(input("Digite sua nota: "))
    acumulador+= nota
    i -= 1
media =acumulador / 10
print(f"A média final das notas é: {media:.2f}")