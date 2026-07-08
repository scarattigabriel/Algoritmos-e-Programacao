'''
Crie uma função que receba 2 argumentos de entrada (base e expoente) e retorne o resultado da potenciação. No programa principal, solicite que o usuário digite os dois valores, chame sua função e mostre o resultado.'''

def potencia (base, expoente):
  resultado= base ** expoente
  return resultado

base=int(input("Digite a base:"))
expoente= int(input("Digite o expoente: "))
print(potencia(base,expoente))