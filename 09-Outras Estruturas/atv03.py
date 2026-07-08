'''Faça um programa, utilizando Dicionários, que peça para o usuário inserir o nome de três produtos de mercado e seus respectivos preços e os mostre na tela.'''

dicionario = {}
for i in range(3):
    nome_produto = input(f'Digite o nome do produto {i+1}: ')
    valor_produto = int(input(f'Digite o valor do produto {i+1}: '))
    dicionario.update({nome_produto: valor_produto})
print(dicionario)