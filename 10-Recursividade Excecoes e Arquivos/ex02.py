'''Exercício 2: faça um programa que leia a idade de uma pessoa e a classifique em menor ou maior de idade. Antes de passar para a classificação, deve ser verificado se a idade está no intervalo entre 0 e 120. Em caso negativo, o programa deve repetir a leitura de dados até que um valor dentro deste intervalo seja digitado. Use o tratamento de exceções para verificar se o número digitado é do tipo inteiro.'''

while True:
    try:
        idade = int(input('Informe a idade de uma pessoa [0, 120] em anos: '))
    except ValueError:
        print('Valor digitado não é um número inteiro.')
        continue
    if 0 <= idade <= 120:
        break
    print('Valor de idade inválido.')
if idade < 18:
    print('A pessoa é menor de idade.')
else:
    print('A pessoa é maior de idade.')