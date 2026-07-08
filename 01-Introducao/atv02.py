'''Em épocas de pouco dinheiro, os comerciantes estão procurando aumentar suas vendas oferecendo desconto.

Faça um algoritmo que recebe o valor de uma venda através de uma entrada do usuário e, que compute e imprima o valor a ser pago em reais tendo em vista que o desconto dado ao cliente foi de 9%.'''

preco_inicial= float(input("Digite o valor do produto: "))
preco_final= preco_inicial - ((preco_inicial/100)*9)
print (f"O valor final com desconto de 9% é {preco_final:.2f}")