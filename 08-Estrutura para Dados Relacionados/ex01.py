'''Exercício 1: crie uma classe para armazenar um usuário (nome, cpf, senha, data_nascimento) e instancie 2 usuários.'''
class Usuario:
    nome = None
    cpf = None
    senha = None
    data_nascimento = None

u1 = Usuario()
u1.nome = 'Fulano'
u1.cpf = '111.222.333-44'
u1.senha = '123'
u1.data_nascimento = '22/04/1991'

u2 = Usuario()
u2.nome = 'Ciclana'
u2.cpf = '999.222.333-44'
u2.senha = 'password'
u2.data_nascimento = '28/02/2000'