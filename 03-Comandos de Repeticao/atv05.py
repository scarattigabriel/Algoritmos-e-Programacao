'''Faça um algoritmo usando o comando while ou for que leia um valor inteiro fornecido pelo usuário e calcule a soma de seus 10 sucessores e seus 10 antecessores. A soma deve ser exibida ao final do programa.

Exemplo de entrada e saída:

Entrada:

11
Saída:

Soma dos sucessores: 165
Soma dos antecessores: 55'''

antecessores=0
sucessores=0
numero= int(input("Digite um numero inteiro: "))

for i in range(numero-10, numero):
  antecessores += i

for i in range(numero+1,numero+11):
  sucessores += i
print(f"{sucessores},{antecessores}")