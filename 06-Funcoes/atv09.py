'''Criar uma função que calcule o número de combinações de n elementos p a p.'''
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
def combinacaoSimples(n, p):
    Cnp = fatorial(n) / (fatorial(p) * fatorial(n - p))
    return Cnp

n = int(input("Digite o valor de n: "))
p = int(input("Digite o valor de p: "))

print(f"A combinação de n elementos p a p é: {combinacaoSimples(n, p)}")