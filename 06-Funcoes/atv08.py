'''Criar uma função que verifique quantas vezes um número é divisível por outro.

Exemplos:

o número 50 é divisível por 5 duas vezes pois 50/5 = 10, 10/5 = 2 e 2 não é divisível por 5.
o número 50 é divisível por 2 uma vez pois 50/2 = 25 e 25 não é divisível por 2.'''

def cont_divisao(dividendo, divisor):
  contador=0
  while dividendo % divisor == 0:
    dividendo= dividendo/divisor
    contador+=1
  return contador

dividendo=int(input())
divisor=int(input())
cont_divisao(dividendo, divisor)