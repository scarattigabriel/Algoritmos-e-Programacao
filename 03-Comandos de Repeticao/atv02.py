'''Escreva um programa para ler 10 números inteiros digitados pelo usuário e contar quantos destes valores são negativos. Apresentar esta informação ao final do programa.'''
contador=0
for i in range(10):
  numeros= int (input("Digite um número inteiro: "))
  if numeros < 0:
    contador+=1
print(f"{contador} números negativos foram inseridos")