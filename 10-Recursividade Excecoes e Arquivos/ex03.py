'''Exercício 3: solicite ao usuário o nome de um arquivo e imprima o seu conteúdo. Crie um novo arquivo caso ele não exista e peça para o usuário informar o seu conteúdo e salve o arquivo.'''

import os
nome_arquivo = input('Informe o nome do arquivo: ')
if nome_arquivo in os.listdir():
    with open(nome_arquivo, 'r') as arquivo:
        print(arquivo.read())
else:
    conteudo = input('Informe o conteúdo do arquivo: ')
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(conteudo)