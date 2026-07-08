'''Exercício 3: crie um algoritmo, usando o conceito de parada por sentinela, que continue debitando (subtraíndo) os valores digitados pelo usuário de uma conta corrente com R$1000 enquanto o valor armazenado na conta for positivo.'''

conta_corrente=1000
while conta_corrente != 0:
  debito=float(input("Débito: "))
  conta_corrente-= debito
  print(f"Saldo: {conta_corrente}")
print("Saldo zerado")