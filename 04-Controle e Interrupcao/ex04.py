'''Exercício 4: crie um algoritmo que leia três notas de um aluno, compute e imprima sua média. O algoritmo deve ignorar notas que forem negativas ou maiores que 10 e pedir uma nova entrada para o usuário. Use o comando continue para fazer esse tratamento da entrada do usuário e garantir o comportamento adequado do algoritmo.'''

soma_notas=0
n_vezes=1
while n_vezes <=3:
  notas=float(input("Digite sua nota: "))
  if notas>10 or notas<0:
    continue
  n_vezes+=1
  soma_notas+= notas
print(f"A média das notas é: {soma_notas/3}")