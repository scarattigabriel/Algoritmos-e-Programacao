'''Repita o exercício anterior, porém, ao invés de 10 devem ser lidos N valores. N será fornecido pelo usuário no início do programa.

Exemplo de entrada e saída:

Entrada:
Quantos valores serão digitados? 3
 -1, 5, -9
Saída: Foram digitados 2 valores negativos'''

contador=0
qtd_numeros= int(input("Digite a quantidade de números: "))
for i in range(qtd_numeros):
  numeros= int (input("Digite um número inteiro: "))
  if numeros < 0:
    contador+=1
print(f"{contador} números negativos foram inseridos")