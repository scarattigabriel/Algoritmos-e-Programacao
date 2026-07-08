'''Faça um código que leia indefinidamente um valor informado pelo usuário e calcule os impostos em 10% do valor informado. O código só irá finalizar quando o usuário digitar o valor -1.

Use o comando break no programa.'''

valor=0
while True:
  valor=float(input("Digite o valor: (-1 para finalizar)"))
  if valor == -1:
    print("Fim do programa!")
    break
  else:
    print(f"O valor final com 10% de imposto é: {valor*1.10:.2f}")