'''
Crie um programa que imprima a tabuada de todos os números de 1 a 9

Busque usar dois comandos de repetição aninhados para o código ficar mais enxuto ao invés de usar um comando de repetição para a tabuada de cada número em separado.
'''

for multiplicador in range (1,10):
  print(f"\n\nTabela do {multiplicador}\n")
  for multiplicando in range(1,10):
    produto= multiplicador * multiplicando
    print(f"{multiplicador} X {multiplicando} = {produto}")