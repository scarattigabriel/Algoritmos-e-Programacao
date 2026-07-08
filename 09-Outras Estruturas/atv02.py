'''Crie um programa que gere automaticamente uma lista de 100 números inteiros aleatórios de 0 a 100. Em seguida, percorra a lista identificando quais valores estão duplicados. Insira os elementos duplicados em outra lista e imprima-a ao final do programa.'''

import random
num_sort=[]
for i in range(100):
  numero_sorteado = random.randint(0, 100) # Número inteiro gerado entre 0 e 100
  num_sort.append(numero_sorteado)


s = set()
asw = set()

for i in num_sort:
  if(i in s):
    asw.add(i)
  s.add(i)

print(asw)
print(num_sort)


import random
num_sort=[]
for i in range(100):
  numero_sorteado = random.randint(0, 100) # Número inteiro gerado entre 0 e 100
  num_sort.append(numero_sorteado)
d={}
for c in num_sort:
  if (c in d):
    d[c] += 1
  else:
    d[c] = 1

for k,v in d.items():
  if v >=2:
    print(k)