'''Defina uma classe que armazene os dados de um aluno. A classe deve conter CPF, nome do aluno, nota da primeira prova, nota da segunda prova e média final. Depois, instancie um aluno com todos os seus dados. A média deve ser calculada a partir das notas da prova. Imprima a média do aluno no final do programa.'''

class Aluno:
    cpf = None
    nome = None
    nota1 = None
    nota2 = None
    media_final = None

aluno1 = Aluno()

aluno1.cpf = "012.345.678-90"
aluno1.nome = "João da Silva"
aluno1.nota1 = 10
aluno1.nota2 = 7

aluno1.media_final = (aluno1.nota1 + aluno1.nota2)/2

print(f" A média final do aluno foi: {aluno1.media_final}.")