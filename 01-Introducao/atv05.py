'''Adapte o programa anterior e para que ele também compute e imprima o valor máximo de desconto (em percentual) que a loja pode aplicar na mercadoria para que não tenha prejuízo na venda.

O valor final do produto, após desconto, deve ser maior ou igual ao custo de produção para que a empresa não tenha prejuízo na venda.'''

custo_producao= float(input("Digite o custo de produção da mercadoria: "))
percent_lucro= float (input("Digite o percentual de lucro desejado: "))

valor_final= custo_producao + (custo_producao/100)*percent_lucro
print(f"O valor final do produto é {valor_final:.2f}")
valor_lucro= valor_final - custo_producao
desconto_max= (valor_lucro/valor_final)*100
print (f"O percentual máximo de desconto é {desconto_max:.2f}")