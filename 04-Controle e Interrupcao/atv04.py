'''
Faça um programa que leia um conjunto de notas de alunos e, ao final, mostre a média geral da turma. A entrada será finalizada quando for lida a nota 999'''

num_notas=0
soma_notas_aluno=0
num_alunos=int(input("Digite o número de alunos"))
for i in range(num_alunos):
  i+=1
  while True:
    notas=int(input(f"Digite as notas do aluno {i}/{num_alunos}: "))
    if notas == 999:
      break
    else:
      num_notas+=1
      soma_notas_aluno+=notas
media_turma=soma_notas_aluno / num_notas
print("A média da turma é: ",media_turma)