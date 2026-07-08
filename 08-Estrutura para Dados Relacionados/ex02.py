'''Exercício 2: crie uma função que receba como parâmetro um usuário e imprima seus dados. Use esta função para imprimir os dados dos dois usuários criados anteriormente.'''

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

# Resolução do exercício 2
def imprimir_usuario(usuario):
    print(f'Nome: {usuario.nome} CPF: {usuario.cpf} Senha: {usuario.senha} Data de Nascimento: {usuario.data_nascimento}')

imprimir_usuario(u1)
imprimir_usuario(u2)