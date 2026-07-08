'''A turma de Algoritmo e Programação, por ter muitos alunos, será dividida em dias de provas.

Após um estudo feito pelo coordenador, o professor Braúlio decidiu dividir a turma em três grupos.

Fazer um algoritmo que leia o nome do aluno e indique a sala em que ele deverá fazer as provas. Use a primeira letra do nome do aluno e a tabela a seguir:

A-K : sala 101

L-N : sala 102

O-Z : sala 103

Observação: a primeira letra de uma variável do tipo str pode ser obtida conforme o exemplo abaixo.'''

nome=input("Digite seu nome")
primeira_letra= nome[0].upper()
if primeira_letra in "ABCDEFGHIJK":
  print("Sala 101")
elif primeira_letra in "LN":
  print("Sala 102")
elif primeira_letra in "OPQRSTUVWXYZ":
  print("Sala 103")
else:
  print("Erro")