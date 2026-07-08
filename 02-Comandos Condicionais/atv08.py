'''A prefeitura de Chapecó abriu uma linha de crédito para os funcionários. O valor máximo da prestação não poderá ultrapassar 30% do salário bruto.

Fazer um algoritmo que permita entrar com o salário bruto e o valor da prestação e informar se o empréstimo pode ou não ser concedido.'''

salario_bruto= float (input("Digite seu salário bruto: "))
prestacao_desejada= float (input("Digite a prestação desejada: "))
prestacao_max= salario_bruto * 0.30
if prestacao_desejada > prestacao_max:
  print("Empréstimo não concedido")
else:
  print("Empréstimo concedido")