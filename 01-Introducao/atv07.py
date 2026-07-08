'''Faça um programa que leia um número inteiro e exiba True caso o número for um resultado possível da inequação abaixo e False caso contrário.

Inequação: 3 * número - 12 > 19'''

numero= int(input("Digite um número inteiro: "))
resultado = 3 * numero - 12 > 19
print (f"{resultado}")