'''Faça um programa contendo:

uma função que recebe um número e retorna verdadeiro se o número for um número natural e falso caso contrário;
uma função que recebe um número e, se este for um número natural (chamando a função acima), retorna seu fatorial. Caso contrário, retorna a mensagem 'O fatorial só é definido para os números naturais!'.'''

def natural(num):
  if type(num)== int and num >= 0:
    return True
  else:
    return False
def fatorial(num):
  if natural(num)== True:
    fatorial=num
    for i in range(num-1, 1, -1):
      print(i, num)
      fatorial= fatorial * i
    return fatorial
  else:
    return ("O fatorial só é definido para números naturais")

numero= int(input("Digite um número natural: "))
print(fatorial(numero))