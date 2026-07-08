'''Exercício 4: use o comando while em conjunto com o comando if para imprimir todos os números múltiplos de 4 do 1 ao 100.'''

n= 1
while n <= 100:
  if n % 4== 0:
    print(f"{n}")
  n += 1