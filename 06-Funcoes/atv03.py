'''uponha que a função abs() não está mais disponível para uso, mas que seu programa precisa calcular o valor absoluto de um número. Escreva uma função que imite o comportamento de abs(). Chame esta função algumas vezes no programa principal, testando com diferentes valores de entrada.'''

def absoluto(numero):
  if numero < 0:
    numero= numero * -1
  return numero
numero=int(input("Digite um número: "))
absoluto(numero)
