'''Faça um programa que solicite o custo de produção de uma mercadoria e um valor percentual de lucro que será acrescido ao valor do produto para a venda.

Imprimira o valor final do produto (valor de venda) com duas casas decimais.'''

custo_producao= float(input("Digite o custo de produção da mercadoria: "))
percent_lucro= float (input("Digite o percentual de lucro desejado: "))
valor_final= custo_producao + (custo_producao/100)*percent_lucro
print(f"O valor final do produto é {valor_final:.2f}")