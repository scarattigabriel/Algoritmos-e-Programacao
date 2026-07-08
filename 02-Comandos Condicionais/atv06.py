'''Faça um programa que funcione como uma calculadora simples. Leia dois valores numéricos e a operação aritmética a ser executada (+, -, / ou *), calcule e exiba o resultado da referida operação.

O programa deve avisar o usuário se foi digitada uma operação inválida.'''

numero1=float(input("Digite o primeiro número: "))
numero2=float(input("Digite o segundo número: "))
operacao = input("Digite:\n(+)para soma\n(-)para subtração\n(/)para divisão\n(*)para multiplicação")
if operacao == '+':
  operacao=numero1 + numero2
elif operacao == '-':
  operacao=numero1 - numero2
elif operacao == '/':
  operacao=numero1 / numero2
elif operacao == '*':
  operacao=numero1 * numero2
else:
  print("Operação inválida")
print(f"Resultado: {operacao:.2f}")