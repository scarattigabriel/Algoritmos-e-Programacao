'''Faça um programa que leia N números (um por vez) enquanto o usuário digitar um valor diferente de zero. Em seguida, imprima na tela qual foi o maior número digitado.

Exemplo de entrada e saída:

Entrada:
 5, 9, 29, 4, 0
Saida: O maior valor é: 29'''

num= float(input("Digite para descobrir o maior número: (0 para finalizar)"))
maior= num
while num != 0:
  num= float(input("Digite para descobrir o maior número: (0 para finalizar)"))
  if num > maior:
    maior= num
print("O maior número digitado foi: ", maior)